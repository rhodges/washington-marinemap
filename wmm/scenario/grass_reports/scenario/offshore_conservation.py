from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats

def offshore_conservation_report(g):
    offshore_report = {}
    
    # Scenario 
    
    #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
    substrate_result = """nice -n 1 r.mapcalc "subresult = if(rresult==1,substrate,null())" """
    g.run(substrate_result)
    #generate dictionary from stats
    substrate_name_dict, substrate_dict = get_dict_from_stats(g, Substrate, 'subresult')
    offshore_report['substrate']=substrate_name_dict
    
    #depth class stats
    depth_class_result = """nice -n 1 r.mapcalc "dcresult = if(rresult==1,depth_class,null())" """
    g.run(depth_class_result)
    #generate dictionary from stats
    depth_class_name_dict, depth_class_dict = get_dict_from_stats(g, DepthClass, 'dcresult')
    offshore_report['depth_class']=depth_class_name_dict
    
    #geomorphology stats
    geomorphology_result = """nice -n 1 r.mapcalc "georesult = if(rresult==1,geomorphology,null())" """
    g.run(geomorphology_result)
    #generate dictionary from stats
    geomorphology_name_dict, geomorphology_dict = get_dict_from_stats(g, Geomorphology, 'georesult')
    offshore_report['geomorphology']=geomorphology_name_dict
    
    # Substrate -- Drilling Down
    
    #substrate depth_class stats -- collecting area (in meters) of each depth class in each substrate 
    sub_ids = substrate_dict.keys()
    substrate_dc_dict = {}
    for sub_id in sub_ids:
        #generate substrate raster
        sub_raster = 'subresult_%s' %sub_id
        substrate_result = """nice -n 1 r.mapcalc "%s = if(substrate==%s,subresult,null())" """ % (sub_raster, sub_id)
        g.run(substrate_result)
        #generate depthclass results for current substrate
        sub_dc_raster = 'substrate_%s_dcresult' %sub_id
        dc_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,depth_class,null())" """ %(sub_dc_raster, sub_raster, sub_id)
        g.run(dc_result)
        #generate dictionary from stats
        dc_name_dict, dc_dict = get_dict_from_stats(g, DepthClass, sub_dc_raster)
        #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
        substrate_dc_dict[Substrate.objects.get(id=sub_id).short_name] = dc_name_dict
    offshore_report['substrate_depth_class']=substrate_dc_dict
    
    #substrate geomorphology stats -- collecting area (in meters) of each geomorphology in each substrate 
    substrate_geo_dict = {}
    for sub_id in sub_ids:
        #generate geomorphology results for current substrate
        sub_raster = 'subresult_%s' %sub_id
        sub_geo_raster = 'substrate_%s_georesult' %sub_id
        geo_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,geomorphology,null())" """ %(sub_geo_raster, sub_raster, sub_id)
        g.run(geo_result)
        #generate dictionary from stats
        geo_name_dict, geo_dict = get_dict_from_stats(g, Geomorphology, sub_geo_raster)
        #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
        substrate_geo_dict[Substrate.objects.get(id=sub_id).short_name] = geo_name_dict
    offshore_report['substrate_geomorphology']=substrate_geo_dict
    
    # Depth Class -- Drilling Down
    
    #depth class geomorphology stats -- collecting area (in meters) of each geomorphology in each depth class 
    depth_class_geo_dict = {}
    dc_ids = depth_class_dict.keys()
    for dc_id in dc_ids:
        #generate depthclass raster
        dc_raster = 'dcresult_%s' %dc_id
        depth_class_result = """nice -n 1 r.mapcalc "%s = if(depth_class==%s,dcresult,null())" """ % (dc_raster, dc_id)
        g.run(depth_class_result)
        #generate geomorphology results for current depthclass
        dc_geo_raster = 'depth_class_%s_georesult' %dc_id
        dc_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,geomorphology,null())" """ %(dc_geo_raster, dc_raster, dc_id)
        g.run(dc_result)
        #generate dictionary from stats
        dc_name_dict, dc_dict = get_dict_from_stats(g, Geomorphology, dc_geo_raster)
        depth_class_geo_dict[DepthClass.objects.get(id=dc_id).short_name] = dc_name_dict
    offshore_report['depth_class_geomorphology']=depth_class_geo_dict
    
    #depth class substrate stats -- collecting area (in meters) of each substrate in each depth class 
    offshore_report['depth_class_substrate']=transpose_nested_dict(substrate_dc_dict)
    
    # Geomorphology -- Drilling Down
    
    #geomorphology substrate stats -- collecting area (in meters) of each substrate in each geomorphology
    offshore_report['geomorphology_substrate']=transpose_nested_dict(substrate_geo_dict)
    
    #geomorphology depth_class stats -- collecting area (in meters) of each depth_class in each geomorphology
    offshore_report['geomorphology_depth_class']=transpose_nested_dict(depth_class_geo_dict)
    
    return simplejson.dumps(offshore_report)
