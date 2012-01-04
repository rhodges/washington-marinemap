from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value
from django.utils import simplejson
    
#areas (in meters) of each substrate in our current dataset   
#why no 2?  (cobble)?  maybe there is none...check dataset in arcmap  
#TODO:  is this really the right place for these values?  should they be in a db table?  should the related calculations be done in S.run?
substrate_extent = {'1': 377037332., '3': 1393314., '4': 28679009641., '5': 531533207., '6': 11587320229., '7': 5443646., '8': 88588867.}
substrate_names = {'1': 'Boulder', '2': 'Cobble', '3': 'Island/Rock', '4': 'Mud', '5': 'Rock', '6': 'Sand', '7': 'Shell', '8': 'Gravel'}
depth_class_extent = {'1': 20434120826., '2': 3204946935., '3': 4479278682., '4': 13152077003.}
depth_class_names = {'1': 'Bathybenthal', '2': 'Innershelf', '3': 'Mesobenthal', '4': 'Midshelf'}
geomorphology_extent = {'1': 4666468839., '3': 4993444064., '2': 25186067878., '4': 6424313054.}
geomorphology_names = {'1': 'Basin', '2': 'Flat', '3': 'Ridge', '4': 'Slope'}
 
'''
'''
def display_scenario_report(request, mos, scenario, template='multi_objective_scenario/reports/scenario_report.html'):
    context = get_scenario_context(mos, scenario)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_scenario_context(mos, scenario): 
    #get context from cache or from running analysis
    substrate_stats, substrate_table_height = get_substrate_stats(scenario)
    depth_class_stats, depth_class_table_height = get_depth_class_stats(scenario)
    geomorphology_stats, geomorphology_table_height = get_geomorphology_stats(scenario)
    context = {'default_value': default_value, 'mos': mos, 'scenario': scenario, 'substrate_stats': substrate_stats, 'substrate_table_height': substrate_table_height, 'depth_class_stats': depth_class_stats, 'depth_class_table_height': depth_class_table_height, 'geomorphology_stats': geomorphology_stats, 'geomorphology_table_height': geomorphology_table_height}
    return context
   
def get_substrate_stats(scenario):    
    substrate_dict = simplejson.loads(scenario.output_substrate_stats)
    substrate_stats = {}
    for key,value in substrate_dict.items():
        if int(value / substrate_extent[key] * 100) > 0:
            substrate_stats[substrate_names[key]] = int(value / substrate_extent[key] * 100)
    substrate_jstats = simplejson.dumps(substrate_stats)
    substrate_table_height = 40 * len(substrate_stats.keys()) + 40     
    return substrate_jstats, substrate_table_height
    
def get_depth_class_stats(scenario):   
    depth_class_dict = simplejson.loads(scenario.output_depth_class_stats)
    depth_class_stats = {}
    for key,value in depth_class_dict.items():
        if int(value / depth_class_extent[key] * 100) > 0:
            depth_class_stats[depth_class_names[key]] = int(value / depth_class_extent[key] * 100)
    depth_class_jstats = simplejson.dumps(depth_class_stats)
    depth_class_table_height = 40 * len(depth_class_stats.keys()) + 40   
    return depth_class_jstats, depth_class_table_height
    
def get_geomorphology_stats(scenario):   
    geomorphology_dict = simplejson.loads(scenario.output_geomorphology_stats)
    geomorphology_stats = {}
    for key,value in geomorphology_dict.items():
        if int(value / geomorphology_extent[key] * 100) > 0:
            geomorphology_stats[geomorphology_names[key]] = int(value / geomorphology_extent[key] * 100)
    geomorphology_jstats = simplejson.dumps(geomorphology_stats)
    geomorphology_table_height = 40 * len(geomorphology_stats.keys()) + 40   
    return geomorphology_jstats, geomorphology_table_height
    