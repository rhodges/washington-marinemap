from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from scenario.models import *
from settings import *
from scenario.utils import default_value, sq_meters_to_sq_miles
from utils import get_scenario_stats, get_drill_down_stats
    
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
    substrate_jextent, substrate_list_reverse = get_scenario_stats(scenario, report['substrate'], Substrate, OffshoreConservationParameterArea)
    depth_class_jextent, depth_class_list_reverse = get_scenario_stats(scenario, report['depth_class'], DepthClass, OffshoreConservationParameterArea)
    geomorphology_jextent, geomorphology_list_reverse = get_scenario_stats(scenario, report['geomorphology'], Geomorphology, OffshoreConservationParameterArea)
    
    # Substrate Context
    #substrate_jpercs, substrate_percs, substrate_r = get_substrate_percs(scenario)
    substrate_dc_jstats = get_drill_down_stats(scenario, report['substrate_depth_class'], Substrate, DepthClass, OffshoreConservationParameterArea)
    substrate_geo_jstats = get_drill_down_stats(scenario, report['substrate_geomorphology'], Substrate, Geomorphology, OffshoreConservationParameterArea)
    #substrate_jcolors = get_substrate_colors(scenario, substrate_jpercs)
    
    #Depth Class Context
    depth_class_sub_jstats = get_drill_down_stats(scenario, report['depth_class_substrate'], DepthClass, Substrate, OffshoreConservationParameterArea)
    depth_class_geo_jstats = get_drill_down_stats(scenario, report['depth_class_geomorphology'], DepthClass, Geomorphology, OffshoreConservationParameterArea)
    
    #Geomorphology Context
    geomorphology_sub_jstats = get_drill_down_stats(scenario, report['geomorphology_substrate'], Geomorphology, Substrate, OffshoreConservationParameterArea)
    geomorphology_dc_jstats = get_drill_down_stats(scenario, report['geomorphology_depth_class'], Geomorphology, DepthClass, OffshoreConservationParameterArea)
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_list_reverse': substrate_list_reverse, 
                'depth_class_jextent': depth_class_jextent, 'depth_class_list_reverse': depth_class_list_reverse,
                'geomorphology_jextent': geomorphology_jextent, 'geomorphology_list_reverse': geomorphology_list_reverse,
                #'substrate_jpercs': substrate_jpercs, 'substrate_percs': substrate_percs, 'substrate_r': substrate_r, 
                'substrate_dc_jstats': substrate_dc_jstats, 'substrate_geo_jstats': substrate_geo_jstats,  #, 'substrate_jcolors': substrate_jcolors }
                'depth_class_sub_jstats': depth_class_sub_jstats, 'depth_class_geo_jstats': depth_class_geo_jstats,
                'geomorphology_sub_jstats': geomorphology_sub_jstats, 'geomorphology_dc_jstats': geomorphology_dc_jstats }
    return context
   
      
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
