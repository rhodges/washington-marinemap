from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from general.utils import default_value, sq_meters_to_sq_miles
from scenario.models import *
from settings import *
from utils import get_scenario_stats, get_drill_down_stats
    
bar_height = 32
 
'''
'''
def display_pelagic_conservation_report(request, mos, scenario, template='mos/reports/pelagic_conservation_report.html'):
    if scenario.input_objective.short_name == 'pelagic_conservation':
        context = get_pelagic_conservation_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_pelagic_conservation_context(mos, scenario): 
    #get report dictionary from scenario
    report = simplejson.loads(scenario.output_report)
    #get context from cache or from running analysis -- actually generating the report data at creation time so report cache is no longer necessary
    
    # Scenario Context
    upwelling_jextent, upwelling_list_reverse = get_scenario_stats(scenario, report['upwelling'], Upwelling, PelagicConservationParameterArea)
    chlorophyll_jextent, chlorophyll_list_reverse = get_scenario_stats(scenario, report['chlorophyll'], Chlorophyl, PelagicConservationParameterArea)
    
    # Upwelling Context
    upwelling_chl_jstats = get_drill_down_stats(scenario, report['upwelling_chlorophyll'], Upwelling, Chlorophyl, PelagicConservationParameterArea)
    
    #Chlorophyll Context
    chlorophyll_upw_jstats = get_drill_down_stats(scenario, report['chlorophyll_upwelling'], Chlorophyl, Upwelling, PelagicConservationParameterArea)
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'upwelling_jextent': upwelling_jextent, 'upwelling_list_reverse': upwelling_list_reverse,
                'chlorophyll_jextent': chlorophyll_jextent, 'chlorophyll_list_reverse': chlorophyll_list_reverse,
                'upwelling_chl_jstats': upwelling_chl_jstats, 'chlorophyll_upw_jstats': chlorophyll_upw_jstats }
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
