from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats, clean_stats_list, get_raster_area

def tidal_energy_report(g, max_query, mean_query, scenario):
    tidal_report = {}
    
    # Scenario 
    
    #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
    substrate_result = """r.mapcalc "subresult = if(rresult==1,tidal_substrate,null())" """
    g.run(substrate_result)
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    substrate_name_dict, substrate_dict = get_dict_from_stats(g, TidalSubstrate, 'subresult')
    tidal_report['substrate'] = substrate_name_dict    
    
    # Tidal Energy Potential
    
    result_area = get_raster_area(g, 'rresult')
    
    #Max Tidal 
    if max_query != 1:
        max_tidal = """r.mapcalc "maxresult = if(%s==1,1,null())" """ %max_query
        g.run(max_tidal)
        max_tidal_area = get_raster_area(g, 'maxresult')
        if max_tidal_area > 0:
            percent_max = result_area / max_tidal_area
            tidal_report['percent_max'] = percent_max    
        else:
            tidal_report['percent_max'] = 0.0
    
    #Mean Tidal
    if mean_query != 1: 
        mean_tidal = """r.mapcalc "meanresult = if(%s==1,1,null())" """ %mean_query
        g.run(mean_tidal)
        mean_tidal_area = get_raster_area(g, 'meanresult')
        if mean_tidal_area > 0:
            percent_mean = result_area / mean_tidal_area
            tidal_report['percent_mean'] = percent_mean
        else:
            tidal_report['percent_mean'] = 0.0
    
    # Substrate with Tidal Energy Potential
    
    # Max -- how much of the Sand/Max-Energy-Range did we capture?, etc
    max_sub_dict = {}
    mean_sub_dict = {}
    for name, area in substrate_name_dict.items():
        sub_id = TidalSubstrate.objects.get(short_name=name).id
        sub_name = TidalSubstrate.objects.get(short_name=name).name
        sub_result_area = area
        
        if max_query != 1:
            total_sub_max_tidal = """r.mapcalc "total_max_tidal_%s = if(tidal_substrate==%s,maxresult,null())" """ %(name, sub_id)
            g.run(total_sub_max_tidal)
            total_sub_max_area = get_raster_area(g, 'total_max_tidal_%s'%name)
            if total_sub_max_area > 0:
                sub_max_perc = sub_result_area / total_sub_max_area 
                max_sub_dict[sub_name] = sub_max_perc
            else:
                max_sub_dict[sub_name] = 0.0
        if mean_query != 1: 
            total_sub_mean_tidal = """r.mapcalc "total_mean_tidal_%s = if(tidal_substrate==%s,meanresult,null())" """ %(name, sub_id)
            g.run(total_sub_mean_tidal)
            total_sub_mean_area = get_raster_area(g, 'total_mean_tidal_%s'%name)  
            if total_sub_mean_area > 0:
                sub_mean_perc = sub_result_area / total_sub_mean_area 
                mean_sub_dict[sub_name] = sub_mean_perc
            else:
                mean_sub_dict[sub_name] = 0.0
    if max_query != 1:    
        tidal_report['sub_max_percs'] = max_sub_dict
    if mean_query != 1: 
        tidal_report['sub_mean_percs'] = mean_sub_dict
    return simplejson.dumps(tidal_report)
