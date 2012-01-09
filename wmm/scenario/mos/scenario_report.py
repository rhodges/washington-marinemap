from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value
from django.utils import simplejson
    
#areas (in meters) of each substrate in our current dataset   
#why no 2?  (Cobble)?  maybe there is none in this region...check dataset in arcmap  
#TODO:  is this really the right place for these values?  should they be in a db table?  should the related calculations be done in S.run?
substrate_area_extent = {'Boulder': 377037332., 'Island/Rock': 1393314., 'Mud': 28679009641., 'Rock': 531533207., 'Sand': 11587320229., 'Shell': 5443646., 'Gravel': 88588867.}
#substrate_names = {'1': 'Boulder', '2': 'Cobble', '3': 'Island/Rock', '4': 'Mud', '5': 'Rock', '6': 'Sand', '7': 'Shell', '8': 'Gravel'}
depth_class_area_extent = {'Bathybenthal': 20434120826., 'Innershelf': 3204946935., 'Mesobenthal': 4479278682., 'Midshelf': 13152077003.}
#depth_class_names = {'1': 'Bathybenthal', '2': 'Innershelf', '3': 'Mesobenthal', '4': 'Midshelf'}
geomorphology_area_extent = {'Basin': 4666468839., 'Flat': 4993444064., 'Ridge': 25186067878., 'Slope': 6424313054.}
#geomorphology_names = {'1': 'Basin', '2': 'Flat', '3': 'Ridge', '4': 'Slope'}
bar_height = 32
 
'''
'''
def display_scenario_report(request, mos, scenario, template='multi_objective_scenario/reports/scenario_report.html'):
    if scenario.input_objective.short_name == 'offshore_conservation':
        context = get_scenario_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_scenario_context(mos, scenario): 
    #get context from cache or from running analysis
    
    # Scenario Context
    substrate_jextent, substrate_names_reverse = get_substrate_scenario_stats(scenario)
    depth_class_jextent = get_depth_class_scenario_stats(scenario)
    geomorphology_jextent = get_geomorphology_scenario_stats(scenario)
    
    # Substrate Context
    #substrate_jpercs, substrate_percs, substrate_r = get_substrate_percs(scenario)
    substrate_dc_jstats = get_substrate_dc_stats(scenario)
    substrate_geo_jstats = get_substrate_geo_stats(scenario)
    #substrate_jcolors = get_substrate_colors(scenario, substrate_jpercs)
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_names_reverse': substrate_names_reverse, 
                'depth_class_jextent': depth_class_jextent, 
                'geomorphology_jextent': geomorphology_jextent, 
                #'substrate_jpercs': substrate_jpercs, 'substrate_percs': substrate_percs, 'substrate_r': substrate_r, 
                'substrate_dc_jstats': substrate_dc_jstats, 'substrate_geo_jstats': substrate_geo_jstats } #, 'substrate_jcolors': substrate_jcolors }
    return context
   
def get_substrate_scenario_stats(scenario):    
    substrate_dict = simplejson.loads(scenario.output_substrate_stats)
    scenario_area = scenario.output_area
    substrate_stats = {} 
    for key,value in substrate_dict.items():
        perc = int(value / scenario_area * 100 + .5)
        if perc > 0:
            substrate_stats[key] = perc
    #arrays not dicts as ordering matters for coloration (at least for now...)
    sorted_substrate_tuples, substrate_names_reverse = sort_substrate_dict(substrate_stats)
    substrate_jstats = simplejson.dumps(sorted_substrate_tuples) 
    return substrate_jstats, substrate_names_reverse
    
def sort_substrate_dict(substrate_dict):
    substrates = Substrate.objects.order_by('id')
    sorted_tuples = []
    substrate_names = []
    for substrate in substrates:        
        if substrate.name in substrate_dict.keys():
            sorted_tuples.append( (substrate_dict[substrate.name], substrate.name) )
            substrate_names.append(substrate.name)
    substrate_names.reverse()
    return sorted_tuples, substrate_names
    
def get_depth_class_scenario_stats(scenario):   
    depth_class_dict = simplejson.loads(scenario.output_depth_class_stats)
    scenario_area = scenario.output_area
    depth_class_stats = {}
    for key,value in depth_class_dict.items():
        perc = int(value / scenario_area * 100 + .5)
        if perc > 0:
            depth_class_stats[key] = perc
    depth_class_jstats = simplejson.dumps(depth_class_stats)
    return depth_class_jstats
    
def get_geomorphology_scenario_stats(scenario):   
    geomorphology_dict = simplejson.loads(scenario.output_geomorphology_stats)
    scenario_area = scenario.output_area
    geomorphology_stats = {}
    for key,value in geomorphology_dict.items():
        perc = int(value / scenario_area * 100 + .5)
        if perc > 0:
            geomorphology_stats[key] = perc
    geomorphology_jstats = simplejson.dumps(geomorphology_stats)
    return geomorphology_jstats
    
def get_substrate_percs(scenario):
    substrate_dict = simplejson.loads(scenario.output_substrate_stats)    
    substrate_percs = []
    for key,value in substrate_dict.items():
        perc = int(value / scenario.output_area * 100 + .5)
        if perc > 0:
            substrate_percs.append( (perc, key) )
    substrate_percs.sort()
    substrate_jpercs = simplejson.dumps(substrate_percs)  
    substrate_r = [y for x,y in substrate_percs]
    substrate_r.reverse()
    return substrate_jpercs, substrate_percs, substrate_r

def get_substrate_colors(scenario, substrate_percs):
    substrate_dict = simplejson.loads(substrate_percs)
    substrate_colors = []
    for key,value in substrate_dict:
        substrate_colors.append( (value, Substrate.objects.get(name=value).color) )
    substrate_jcolors = simplejson.dumps(substrate_colors)
    return substrate_jcolors
    
def get_substrate_dc_stats(scenario):
    substrate_dc_dict = simplejson.loads(scenario.output_substrate_depth_class_stats)
    substrate_dc_stats = {}
    for sub, dc_dict in substrate_dc_dict.items():
        substrate = sub
        substrate_area = float( sum( [area for dc, area in dc_dict.items()] ) )
        dc_perc_dict = {}
        for dc, area in dc_dict.items():
            dc_perc_dict[dc] = int(area / substrate_area * 100 + .5)
        substrate_dc_stats[sub] = dc_perc_dict
    substrate_dc_jstats = simplejson.dumps(substrate_dc_stats)
    return substrate_dc_jstats
        
def get_substrate_geo_stats(scenario):
    substrate_geo_dict = simplejson.loads(scenario.output_substrate_geomorphology_stats)
    substrate_geo_stats = {}
    for sub, geo_dict in substrate_geo_dict.items():
        substrate = sub
        substrate_area = float( sum( [area for geo, area in geo_dict.items()] ) )
        geo_perc_dict = {}
        for geo, area in geo_dict.items():
            geo_perc_dict[geo] = int(area / substrate_area * 100 + .5)
        substrate_geo_stats[sub] = geo_perc_dict
    substrate_geo_jstats = simplejson.dumps(substrate_geo_stats)
    return substrate_geo_jstats
        