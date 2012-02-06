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
def display_wave_energy_report(request, mos, scenario, template='mos/reports/wave_energy_report.html'):
    if scenario.input_objective.short_name == 'wave_energy':
        context = get_wave_energy_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_wave_energy_context(mos, scenario): 
    #get report dictionary from scenario
    report = simplejson.loads(scenario.output_report)
    #get context from cache or from running analysis -- generating the report data at creation time so report cache is no longer necessary
    
    # Scenario Context
    substrate_jextent, substrate_list_reverse = get_scenario_stats(scenario, report['substrate'], Substrate, WaveEnergyParameterArea)
    #wave_potential_jextent, wave_potential_list_reverse = get_scenario_stats(scenario, report['wave_potential'], WavePotential, WaveEnergyParameterArea)
    
    # Substrate Context
    #substrate_wave_jstats = get_drill_down_stats(scenario, report['substrate_wave_potential'], Substrate, WavePotential, WaveEnergyParameterArea)
    
    # Wave Potential Context
    if 'sub_summer_percs' in report.keys():
        summer_percentage = report['percent_summer']
        substrate_summer_percs = report['sub_summer_percs']
    else:
        summer_percentage = default_value
        substrate_summer_percs = default_value
    if 'sub_winter_percs' in report.keys():
        winter_percentage = report['percent_winter']
        substrate_winter_percs = report['sub_winter_percs']
    else:
        winter_percentage = default_value
        substrate_winter_percs = default_value
    #wave_substrate_jstats = get_drill_down_stats(scenario, report['wave_potential_substrate'], WavePotential, Substrate, WaveEnergyParameterArea)    
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_list_reverse': substrate_list_reverse,
                'summer_percentage': summer_percentage, 'winter_percentage': winter_percentage,
                'substrate_summer_percs': substrate_summer_percs, 'substrate_winter_percs': substrate_winter_percs }
                #'wave_potential_jextent': wave_potential_jextent, 'wave_potential_list_reverse': wave_potential_list_reverse,
                #'substrate_wave_jstats': substrate_wave_jstats, 'wave_substrate_jstats': wave_substrate_jstats }
    return context
   
    
        