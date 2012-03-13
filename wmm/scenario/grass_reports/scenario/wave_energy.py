from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats, clean_stats_list, get_raster_area

def wave_energy_report(g, summer_query, winter_query, scenario):
    wave_report = {}
    
    # Scenario 
    
    #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
    substrate_result = """nice -n 1 r.mapcalc "subresult = if(rresult==1,substrate,null())" """
    g.run(substrate_result)
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    substrate_name_dict, substrate_dict = get_dict_from_stats(g, Substrate, 'subresult')
    wave_report['substrate'] = substrate_name_dict    
    
    # Wave Potential
    
    result_area = get_raster_area(g, 'rresult')
    
    #Summer 
    if summer_query != 1:
        summer_wave = """nice -n 1 r.mapcalc "summerresult = if(%s==1,1,null())" """ %summer_query
        g.run(summer_wave)
        summer_wave_area = get_raster_area(g, 'summerresult')
        if summer_wave_area > 0:
            percent_summer = result_area / summer_wave_area
            wave_report['percent_summer'] = percent_summer    
        else:
            wave_report['percent_summer'] = 0.0
    #Winter
    if winter_query != 1: 
        winter_wave = """nice -n 1 r.mapcalc "winterresult = if(%s==1,1,null())" """ %winter_query
        g.run(winter_wave)
        winter_wave_area = get_raster_area(g, 'winterresult')
        if winter_wave_area > 0:
            percent_winter = result_area / winter_wave_area
            wave_report['percent_winter'] = percent_winter
        else:
            wave_report['percent_winter'] = 0.0
    
    # Substrate with Wave Potential
    
    # Summer -- how much of the Sand/Summer-Energy-Range did we capture?, etc
    summer_sub_dict = {}
    winter_sub_dict = {}
    for name, area in substrate_name_dict.items():
        sub_id = Substrate.objects.get(short_name=name).id
        sub_name = Substrate.objects.get(short_name=name).name
        sub_result_area = area
        
        #resulting_sand_summer_wave_area / total_sand_summer_wave_area
        #assuming resulting_sand_area == resulting_sand_summer_wave_area?
        if summer_query != 1:
            total_sub_summer_wave = """nice -n 1 r.mapcalc "total_summer_wave_%s = if(substrate==%s,summerresult,null())" """ %(name, sub_id)
            g.run(total_sub_summer_wave)
            total_sub_summer_area = get_raster_area(g, 'total_summer_wave_%s'%name) 
            if total_sub_summer_area > 0:
                sub_summer_perc = sub_result_area / total_sub_summer_area 
                summer_sub_dict[sub_name] = sub_summer_perc
            else:
                summer_sub_dict[sub_name] = 0.0
        if winter_query != 1: 
            total_sub_winter_wave = """nice -n 1 r.mapcalc "total_winter_wave_%s = if(substrate==%s,winterresult,null())" """ %(name, sub_id)
            g.run(total_sub_winter_wave)
            total_sub_winter_area = get_raster_area(g, 'total_winter_wave_%s'%name) 
            if total_sub_winter_area > 0:
                sub_winter_perc = sub_result_area / total_sub_winter_area 
                winter_sub_dict[sub_name] = sub_winter_perc
            else:
                winter_sub_dict[sub_name] = 0.0
    if summer_query != 1:    
        wave_report['sub_summer_percs'] = summer_sub_dict
    if winter_query != 1: 
        wave_report['sub_winter_percs'] = winter_sub_dict
    return simplejson.dumps(wave_report)

