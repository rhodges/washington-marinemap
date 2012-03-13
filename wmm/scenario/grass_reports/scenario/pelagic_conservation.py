from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats

def pelagic_conservation_report(g):
    pelagic_report = {}
    
    # Scenario 
    
    #upwelling stats -- collecting area (in meters) for each upwelling type represented in the resulting scenario
    upwelling_result = """nice -n 1 r.mapcalc "upwresult = if(rresult==1,upwelling,null())" """
    g.run(upwelling_result)
    #generate dictionary from stats
    upwelling_name_dict, upwelling_dict = get_dict_from_stats(g, Upwelling, 'upwresult')
    pelagic_report['upwelling']=upwelling_name_dict
    
    #exposure stats
    chlorophyll_result = """nice -n 1 r.mapcalc "chlresult = if(rresult==1,chlorophyll,null())" """
    g.run(chlorophyll_result)
    #generate dictionary from stats
    chlorophyll_name_dict, chlorophyll_dict = get_dict_from_stats(g, Chlorophyl, 'chlresult')
    pelagic_report['chlorophyll']=chlorophyll_name_dict
        
    # Upwelling -- Drilling Down
    
    #upwelling chlorophyll stats -- collecting area (in meters) of each chlorophyll type within each upwelling type
    upw_ids = upwelling_dict.keys()
    upwelling_chl_dict = {}
    for upw_id in upw_ids:
        #generate upwelling raster
        upw_raster = 'upwresult_%s' %upw_id
        upwelling_result = """nice -n 1 r.mapcalc "%s = if(upwelling==%s,upwresult,null())" """ % (upw_raster, upw_id)
        g.run(upwelling_result)
        #generate chlorophyll results for current upwelling type
        upw_chl_raster = 'upwelling_%s_chlresult' %upw_id
        chl_result = """nice -n 1 r.mapcalc "%s = if(%s==%s,chlorophyll,null())" """ %(upw_chl_raster, upw_raster, upw_id)
        g.run(chl_result)
        #generate dictionary from stats
        chl_name_dict, chl_dict = get_dict_from_stats(g, Chlorophyl, upw_chl_raster)
        #NEXT:  create short_name field for Chlorophyl and Upwelling? 
        upwelling_chl_dict[Upwelling.objects.get(id=upw_id).short_name] = chl_name_dict
    pelagic_report['upwelling_chlorophyll']=upwelling_chl_dict
    
    # Chlorophyll -- Drilling Down
    
    #chlorophyll upwelling stats -- collecting area (in meters) of each upwelling type within each chlorophyll type
    pelagic_report['chlorophyll_upwelling']=transpose_nested_dict(upwelling_chl_dict)
    
    return simplejson.dumps(pelagic_report)
