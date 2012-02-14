from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from settings import *
from scenario.models import *
from scenario.utils import default_value, sq_meters_to_sq_miles
from utils import get_scenario_stats, get_drill_down_stats
    
bar_height = 32
 
'''
'''
def display_tidal_energy_report(request, mos, scenario, template='mos/reports/tidal_energy_report.html'):
    if scenario.input_objective.short_name == 'tidal_energy':
        context = get_tidal_energy_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_tidal_energy_context(mos, scenario): 
    #get report dictionary from scenario
    report = simplejson.loads(scenario.output_report)
    #get context from cache or from running analysis -- generating the report data at creation time so report cache is no longer necessary
    
    # Scenario Context
    substrate_jextent, substrate_list_reverse = get_scenario_stats(scenario, report['substrate'], TidalSubstrate, TidalEnergyParameterArea)
    
    # Tidal Potential Context
    if 'sub_max_percs' in report.keys():
        max_percentage = report['percent_max']
        substrate_max_percs = report['sub_max_percs']
    else:
        max_percentage = default_value
        substrate_max_percs = default_value
        
    if 'sub_mean_percs' in report.keys():
        mean_percentage = report['percent_mean']
        substrate_mean_percs = report['sub_mean_percs']
    else:
        mean_percentage = default_value
        substrate_mean_percs = default_value
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_list_reverse': substrate_list_reverse,
                'max_percentage': max_percentage, 'mean_percentage': mean_percentage,
                'substrate_max_percs': substrate_max_percs, 'substrate_mean_percs': substrate_mean_percs }
    return context
   
    
        