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
def display_wind_energy_report(request, mos, scenario, template='mos/reports/wind_energy_report.html'):
    if scenario.input_objective.short_name == 'wind_energy':
        context = get_wind_energy_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_wind_energy_context(mos, scenario): 
    #get report dictionary from scenario
    report = simplejson.loads(scenario.output_report)
    #get context from cache or from running analysis -- generating the report data at creation time so report cache is no longer necessary
    
    # Scenario Context
    substrate_jextent, substrate_list_reverse = get_scenario_stats(scenario, report['substrate'], Substrate, WindEnergyParameterArea)
    wind_potential_jextent, wind_potential_list_reverse = get_scenario_stats(scenario, report['wind_potential'], WindPotential, WindEnergyParameterArea)
    
    # Substrate Context
    substrate_wind_jstats = get_drill_down_stats(scenario, report['substrate_wind_potential'], Substrate, WindPotential, WindEnergyParameterArea)
    
    # Wind Potential Context
    wind_substrate_jstats = get_drill_down_stats(scenario, report['wind_potential_substrate'], WindPotential, Substrate, WindEnergyParameterArea)    
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_list_reverse': substrate_list_reverse,
                'wind_potential_jextent': wind_potential_jextent, 'wind_potential_list_reverse': wind_potential_list_reverse,
                'substrate_wind_jstats': substrate_wind_jstats, 'wind_substrate_jstats': wind_substrate_jstats }
    return context
   
