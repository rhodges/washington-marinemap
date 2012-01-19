from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value, sq_meters_to_sq_miles
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
def display_offshore_conservation_report(request, mos, scenario, template='multi_objective_scenario/reports/offshore_conservation_report.html'):
    if scenario.input_objective.short_name == 'offshore_conservation':
        context = get_offshore_conservation_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_offshore_conservation_context(mos, scenario): 
    #get report dictionary from scenario
    report = simplejson.loads(scenario.output_report)
    #get context from cache or from running analysis -- actually generating the report data at creation time so report cache is no longer necessary
    
    # Scenario Context
    substrate_jextent, substrate_list_reverse = get_scenario_stats(scenario, report['substrate'], Substrate)
    depth_class_jextent, depth_class_list_reverse = get_scenario_stats(scenario, report['depth_class'], DepthClass)
    geomorphology_jextent, geomorphology_list_reverse = get_scenario_stats(scenario, report['geomorphology'], Geomorphology)
    
    # Substrate Context
    #substrate_jpercs, substrate_percs, substrate_r = get_substrate_percs(scenario)
    substrate_dc_jstats = get_drill_down_stats(scenario, report['substrate_depth_class'])
    substrate_geo_jstats = get_drill_down_stats(scenario, report['substrate_geomorphology'])
    #substrate_jcolors = get_substrate_colors(scenario, substrate_jpercs)
    
    #Depth Class Context
    depth_class_sub_jstats = get_drill_down_stats(scenario, report['depth_class_substrate'])
    depth_class_geo_jstats = get_drill_down_stats(scenario, report['depth_class_geomorphology'])
    
    #Geomorphology Context
    geomorphology_sub_jstats = get_drill_down_stats(scenario, report['geomorphology_substrate'])
    geomorphology_dc_jstats = get_drill_down_stats(scenario, report['geomorphology_depth_class'])
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_list_reverse': substrate_list_reverse, 
                'depth_class_jextent': depth_class_jextent, 'depth_class_list_reverse': depth_class_list_reverse,
                'geomorphology_jextent': geomorphology_jextent, 'geomorphology_list_reverse': geomorphology_list_reverse,
                #'substrate_jpercs': substrate_jpercs, 'substrate_percs': substrate_percs, 'substrate_r': substrate_r, 
                'substrate_dc_jstats': substrate_dc_jstats, 'substrate_geo_jstats': substrate_geo_jstats,  #, 'substrate_jcolors': substrate_jcolors }
                'depth_class_sub_jstats': depth_class_sub_jstats, 'depth_class_geo_jstats': depth_class_geo_jstats,
                'geomorphology_sub_jstats': geomorphology_sub_jstats, 'geomorphology_dc_jstats': geomorphology_dc_jstats }
    return context
   

def get_scenario_stats(scenario, param_dict, model_class):  
    scenario_area = scenario.output_area
    stats = {} 
    for key,value in param_dict.items():
        perc = value / scenario_area * 100
        if perc > 0:
            stats[key] = (int(perc*10 + .5) / 10., sq_meters_to_sq_miles(value))
    #arrays not dicts as ordering matters for coloration (at least for now...)
    sorted_tuples, list_reverse = sort_dict(stats, model_class)
    jstats = simplejson.dumps(sorted_tuples) 
    return jstats, list_reverse
     
def sort_dict(param_dict, model_class):
    params = model_class.objects.order_by('id')
    sorted_tuples = []
    ordered_list = []
    for param in params:        
        if param.name in param_dict.keys():
            tooltip_text = "Total Area: %.2f sq miles" %param_dict[param.name][1]
            sorted_tuples.append( [param_dict[param.name][0], param.name, tooltip_text] )
            ordered_list.append(param)
    ordered_list.reverse()
    return sorted_tuples, ordered_list
      
'''   
def get_substrate_scenario_stats(scenario, report):   
    substrate_dict = report['substrate']
    #substrate_dict = simplejson.loads(scenario.output_substrate_stats)
    scenario_area = scenario.output_area
    substrate_stats = {} 
    for key,value in substrate_dict.items():
        perc = value / scenario_area * 100
        if perc > 0:
            substrate_stats[key] = (int(perc*10 + .5) / 10., sq_meters_to_sq_miles(value))
    #arrays not dicts as ordering matters for coloration (at least for now...)
    sorted_substrate_tuples, substrate_list_reverse = sort_substrate_dict(substrate_stats)
    substrate_jstats = simplejson.dumps(sorted_substrate_tuples) 
    return substrate_jstats, substrate_list_reverse
    
def sort_substrate_dict(substrate_dict):
    substrates = Substrate.objects.order_by('id')
    sorted_tuples = []
    substrate_list = []
    for substrate in substrates:        
        if substrate.name in substrate_dict.keys():
            tooltip_text = "Total Area: %.2f sq miles" %substrate_dict[substrate.name][1]
            sorted_tuples.append( [substrate_dict[substrate.name][0], substrate.name, tooltip_text] )
            substrate_list.append(substrate)
    substrate_list.reverse()
    return sorted_tuples, substrate_list
    
def get_tooltip_text(area):
    return "%.2f sq miles" %area
    
def get_depth_class_scenario_stats(scenario, report):  
    depth_class_dict = report['depth_class'] 
    #depth_class_dict = simplejson.loads(scenario.output_depth_class_stats)
    scenario_area = scenario.output_area
    depth_class_stats = {}
    for key,value in depth_class_dict.items():
        perc = value / scenario_area * 100 
        if perc > 0:
            tooltip_text = "Total Area: %.2f sq miles" %sq_meters_to_sq_miles(value)
            depth_class_stats[key] = (int(perc*10 + .5) / 10., tooltip_text)
    depth_class_list_reverse = dict_to_rsorted_array(depth_class_stats, DepthClass.objects.order_by('id'))
    depth_class_jstats = simplejson.dumps(depth_class_stats)
    return depth_class_jstats, depth_class_list_reverse
    
def dict_to_rsorted_array(some_dict, objects):
    #sorted_tuples = []
    object_list = []
    for object in objects:        
        if object.name in some_dict.keys():
            #tooltip_text = "Total Area: %.2f sq miles" %some_dict[object.name][1]
            #sorted_tuples.append( [some_dict[object.name][0], object.name] )
            object_list.append(object)
    object_list.reverse()
    return object_list
    
def get_geomorphology_scenario_stats(scenario, report):   
    geomorphology_dict = report['geomorphology']  
    #geomorphology_dict = simplejson.loads(scenario.output_geomorphology_stats)
    scenario_area = scenario.output_area
    geomorphology_stats = {}
    for key,value in geomorphology_dict.items():
        perc = value / scenario_area * 100 
        if perc > 0:
            tooltip_text = "Total Area: %.2f sq miles" %sq_meters_to_sq_miles(value)
            geomorphology_stats[key] = [int(perc*10 + .5) / 10., tooltip_text]
    geomorphology_list_reverse = dict_to_rsorted_array(geomorphology_stats, Geomorphology.objects.order_by('id'))
    geomorphology_jstats = simplejson.dumps(geomorphology_stats)
    return geomorphology_jstats, geomorphology_list_reverse
'''    
def get_substrate_percs(scenario, report):  
    substrate_dict = report['substrate']
    #substrate_dict = simplejson.loads(scenario.output_substrate_stats)    
    substrate_percs = []
    for key,value in substrate_dict.items():
        perc = value / scenario.output_area * 100
        if perc > 0:
            substrate_percs.append( (int(perc*10 + .5) / 10., key) )
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
    
def get_drill_down_stats(scenario, dictionary):  
    stats = {}
    for name, param_dict in dictionary.items():
        total_area = float( sum( [area for param, area in param_dict.items()] ) )
        param_perc_dict = {}
        for param, area in param_dict.items():
            tooltip_text = "Total Area: %.2f sq miles" %sq_meters_to_sq_miles(area)
            param_perc_dict[param] = [int(area / total_area * 1000 + .5) / 10., tooltip_text]
        stats[name] = param_perc_dict
    jstats = simplejson.dumps(stats)
    return jstats
              