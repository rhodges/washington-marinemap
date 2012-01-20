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
    substrate_dc_jstats = get_drill_down_stats(scenario, report['substrate_depth_class'], Substrate, DepthClass)
    substrate_geo_jstats = get_drill_down_stats(scenario, report['substrate_geomorphology'], Substrate, Geomorphology)
    #substrate_jcolors = get_substrate_colors(scenario, substrate_jpercs)
    
    #Depth Class Context
    depth_class_sub_jstats = get_drill_down_stats(scenario, report['depth_class_substrate'], DepthClass, Substrate)
    depth_class_geo_jstats = get_drill_down_stats(scenario, report['depth_class_geomorphology'], DepthClass, Geomorphology)
    
    #Geomorphology Context
    geomorphology_sub_jstats = get_drill_down_stats(scenario, report['geomorphology_substrate'], Geomorphology, Substrate)
    geomorphology_dc_jstats = get_drill_down_stats(scenario, report['geomorphology_depth_class'], Geomorphology, DepthClass)
    
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
            #stats[key] = (int(perc*10 + .5) / 10., sq_meters_to_sq_miles(value))
            stats[key] = (int(perc*10 + .5) / 10., value)
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
            try:
                total_param_area = OffshoreConservationParameterArea.objects.get(name=param.short_name).area
            except:
                total_param_area = None
            if total_param_area is not None:
                perc = param_dict[param.name][1] / total_param_area * 100
                tooltip_text = "%.2f%s of available %s" %(perc, '%', param.name)
            else:
                tooltip_text = "Data Unavailable"
            #tooltip_text = "Total Area: %.2f sq miles" %param_dict[param.name][1]
            sorted_tuples.append( [param_dict[param.name][0], param.name, tooltip_text] )
            ordered_list.append(param)
    ordered_list.reverse()
    return sorted_tuples, ordered_list
      
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
    
def get_drill_down_stats(scenario, dictionary, outer_class, inner_class):  #add model_class to this method call 
    stats = {}
    for outer_short_name, param_dict in dictionary.items():
        outer_name = outer_class.objects.get(short_name=outer_short_name).name
        total_area = float( sum( [area for param, area in param_dict.items()] ) )
        param_perc_dict = {}
        for inner_short_name, area in param_dict.items():
            inner_name = inner_class.objects.get(short_name=inner_short_name).name
            drill_down_name = '%s_%s' %(outer_short_name, inner_short_name)
            total_param_area = OffshoreConservationParameterArea.objects.get(name=drill_down_name).area
            if total_param_area is not None:
                perc = param_dict[inner_short_name] / total_param_area * 100
                tooltip_text = "%.2f%s of available %s/%s" %(perc, '%', inner_name, outer_name)
            else:
                tooltip_text = "Data Unavailable"
            #tooltip_text = "Total Area: %.2f sq miles" %sq_meters_to_sq_miles(area)
            param_perc_dict[inner_name] = [int(area / total_area * 1000 + .5) / 10., tooltip_text]
        stats[outer_short_name] = param_perc_dict
    jstats = simplejson.dumps(stats)
    return jstats
              