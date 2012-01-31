from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats

def wind_energy_report(g):
    wind_report = {}
    
    # Scenario 
    
    #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
    substrate_result = """r.mapcalc "subresult = if(rresult==1,substrate,null())" """
    g.run(substrate_result)
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    substrate_name_dict, substrate_dict = get_dict_from_stats(g, Substrate, 'subresult')
    wind_report['substrate'] = substrate_name_dict
            
    #wind stats -- collecting area (in meters) for each wind energy class represented in the resulting scenario
    wind_result = """r.mapcalc "windresult = if(rresult==1,wind,null())" """
    g.run(wind_result)
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    wind_name_dict, wind_dict = get_dict_from_stats(g, WindPotential, 'windresult')
    wind_report['wind_potential'] = wind_name_dict
    
    # Substrate -- Drilling Down
    
    #substrate depth_class stats -- collecting area (in meters) of each depth class in each substrate 
    sub_ids = substrate_dict.keys()
    substrate_wind_dict = {}
    for sub_id in sub_ids:
        #generate substrate raster
        sub_raster = 'subresult_%s' %sub_id
        substrate_result = """r.mapcalc "%s = if(substrate==%s,subresult,null())" """ % (sub_raster, sub_id)
        g.run(substrate_result)
        #generate wind class results for current substrate
        sub_wind_raster = 'substrate_%s_windresult' %sub_id
        wind_result = """r.mapcalc "%s = if(%s==%s,wind,null())" """ %(sub_wind_raster, sub_raster, sub_id)
        g.run(wind_result)
        wind_name_dict, wind_dict = get_dict_from_stats(g, WindPotential, sub_wind_raster)
        #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
        substrate_wind_dict[Substrate.objects.get(id=sub_id).short_name] = wind_name_dict
    wind_report['substrate_wind_potential'] = substrate_wind_dict
    
    # Wind Potential -- Drilling Down
    
    #wind potential substrate stats -- collecting area (in meters) of each substrate in each wind class 
    wind_report['wind_potential_substrate']=transpose_nested_dict(substrate_wind_dict)

    return simplejson.dumps(wind_report)
