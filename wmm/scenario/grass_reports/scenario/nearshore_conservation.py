from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats

def nearshore_conservation_report(g):
    nearshore_report = {}
    # Scenario 
    
    #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
    substrate_result = """nice -n 1 r.mapcalc "subresult = if(rresult==1,nearshore_substrate,null())" """
    g.run(substrate_result)
    #generate dictionary from stats
    substrate_name_dict, substrate_dict = get_dict_from_stats(g, NearshoreSubstrate, 'subresult')
    nearshore_report['substrate']=substrate_name_dict
    
    #exposure stats
    exposure_result = """nice -n 1 r.mapcalc "expresult = if(rresult==1,exposure,null())" """
    g.run(exposure_result)
    #generate dictionary from stats
    exposure_name_dict, exposure_dict = get_dict_from_stats(g, NearshoreExposure, 'expresult')
    nearshore_report['exposure']=exposure_name_dict
    
    #ecosystem stats
    ecosystem_result = """nice -n 1 r.mapcalc "ecoresult = if(rresult==1,vegetation,null())" """
    g.run(ecosystem_result)
    #generate dictionary from stats
    ecosystem_name_dict, ecosystem_dict = get_dict_from_stats(g, NearshoreEcosystem, 'ecoresult')
    nearshore_report['ecosystem']=ecosystem_name_dict
    
    # Substrate -- Drilling Down
    
    #substrate exposure stats -- collecting area (in meters) of each exposure in each substrate 
    sub_ids = substrate_dict.keys()
    substrate_exp_dict = {}
    for sub_id in sub_ids:
        #generate substrate raster
        sub_raster = 'subresult_%s' %sub_id
        substrate_result = """nice -n 1 r.mapcalc "%s = if(nearshore_substrate==%s,subresult,null())" """ % (sub_raster, sub_id)
        g.run(substrate_result)
        #generate exposure results for current substrate
        sub_exp_raster = 'substrate_%s_expresult' %sub_id
        exp_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,exposure,null())" """ %(sub_exp_raster, sub_raster, sub_id)
        g.run(exp_result)
        #generate dictionary from stats
        exp_name_dict, exp_dict = get_dict_from_stats(g, NearshoreExposure, sub_exp_raster)
        #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
        substrate_exp_dict[NearshoreSubstrate.objects.get(id=sub_id).short_name] = exp_name_dict
    nearshore_report['substrate_exposure']=substrate_exp_dict
    
    #substrate ecosystem stats -- collecting area (in meters) of each ecosystem in each substrate 
    substrate_eco_dict = {}
    for sub_id in sub_ids:
        #generate geomorphology results for current substrate
        sub_raster = 'subresult_%s' %sub_id
        sub_eco_raster = 'substrate_%s_ecoresult' %sub_id
        eco_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,vegetation,null())" """ %(sub_eco_raster, sub_raster, sub_id)
        g.run(eco_result)
        #generate dictionary from stats
        eco_name_dict, eco_dict = get_dict_from_stats(g, NearshoreEcosystem, sub_eco_raster)
        #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
        substrate_eco_dict[NearshoreSubstrate.objects.get(id=sub_id).short_name] = eco_name_dict
    nearshore_report['substrate_ecosystem']=substrate_eco_dict
    
    # Ecosystem -- Drilling Down
    
    #ecosystem exposure stats -- collecting area (in meters) of each exposure in each ecosystem
    ecosystem_exp_dict = {}
    eco_ids = ecosystem_dict.keys()
    for eco_id in eco_ids:
        #generate ecosystem raster
        eco_raster = 'ecoresult_%s' %eco_id
        ecosystem_result = """nice -n 1 r.mapcalc "%s = if(vegetation==%s,ecoresult,null())" """ % (eco_raster, eco_id)
        g.run(ecosystem_result)
        #generate exposure results for current ecosystem
        eco_exp_raster = 'ecosystem_%s_expresult' %eco_id
        eco_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,exposure,null())" """ %(eco_exp_raster, eco_raster, eco_id)
        g.run(eco_result)
        #generate dictionary from stats
        eco_name_dict, eco_dict = get_dict_from_stats(g, NearshoreExposure, eco_exp_raster)
        ecosystem_exp_dict[NearshoreEcosystem.objects.get(id=eco_id).short_name] = eco_name_dict
    nearshore_report['ecosystem_exposure']=ecosystem_exp_dict
    
    #ecosystem substrate stats -- collecting area (in meters) of each substrate in each ecosystem 
    nearshore_report['ecosystem_substrate']=transpose_nested_dict(substrate_eco_dict)
    
    # Exposure -- Drilling Down
    
    #exposure substrate stats -- collecting area (in meters) of each substrate in each exposure
    nearshore_report['exposure_substrate']=transpose_nested_dict(substrate_exp_dict)
    
    #exposure ecosystem stats -- collecting area (in meters) of each ecosystem in each exposure
    nearshore_report['exposure_ecosystem']=transpose_nested_dict(ecosystem_exp_dict)
    
    return simplejson.dumps(nearshore_report)
