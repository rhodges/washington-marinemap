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
def display_nearshore_conservation_report(request, mos, scenario, template='mos/reports/nearshore_conservation_report.html'):
    if scenario.input_objective.short_name == 'nearshore_conservation':
        context = get_nearshore_conservation_context(mos, scenario)
        return render_to_response(template, RequestContext(request, context)) 
    else:
        return HttpResponse(scenario.input_objective.name + ' Report coming soon...')

'''
'''    
def get_nearshore_conservation_context(mos, scenario): 
    #get report dictionary from scenario
    report = simplejson.loads(scenario.output_report)
    #get context from cache or from running analysis -- actually generating the report data at creation time so report cache is no longer necessary
    
    # Scenario Context
    substrate_jextent, substrate_list_reverse = get_scenario_stats(scenario, report['substrate'], NearshoreSubstrate, NearshoreConservationParameterArea)
    exposure_jextent, exposure_list_reverse = get_scenario_stats(scenario, report['exposure'], NearshoreExposure, NearshoreConservationParameterArea)
    ecosystem_jextent, ecosystem_list_reverse = get_scenario_stats(scenario, report['ecosystem'], NearshoreEcosystem, NearshoreConservationParameterArea)
    
    # Substrate Context
    #substrate_jpercs, substrate_percs, substrate_r = get_substrate_percs(scenario)
    substrate_exp_jstats = get_drill_down_stats(scenario, report['substrate_exposure'], NearshoreSubstrate, NearshoreExposure, NearshoreConservationParameterArea)
    substrate_eco_jstats = get_drill_down_stats(scenario, report['substrate_ecosystem'], NearshoreSubstrate, NearshoreEcosystem, NearshoreConservationParameterArea)
    #substrate_jcolors = get_substrate_colors(scenario, substrate_jpercs)
    
    #Ecosystem Context
    ecosystem_sub_jstats = get_drill_down_stats(scenario, report['ecosystem_substrate'], NearshoreEcosystem, NearshoreSubstrate, NearshoreConservationParameterArea)
    ecosystem_exp_jstats = get_drill_down_stats(scenario, report['ecosystem_exposure'], NearshoreEcosystem, NearshoreExposure, NearshoreConservationParameterArea)
    
    #Exposure Context
    exposure_sub_jstats = get_drill_down_stats(scenario, report['exposure_substrate'], NearshoreExposure, NearshoreSubstrate, NearshoreConservationParameterArea)
    exposure_eco_jstats = get_drill_down_stats(scenario, report['exposure_ecosystem'], NearshoreExposure, NearshoreEcosystem, NearshoreConservationParameterArea)
    
    context = { 'default_value': default_value, 'bar_height': bar_height, 'mos': mos, 'scenario': scenario, 
                'substrate_jextent': substrate_jextent, 'substrate_list_reverse': substrate_list_reverse,
                'exposure_jextent': exposure_jextent, 'exposure_list_reverse': exposure_list_reverse,
                'ecosystem_jextent': ecosystem_jextent, 'ecosystem_list_reverse': ecosystem_list_reverse,
                'substrate_exp_jstats': substrate_exp_jstats, 'substrate_eco_jstats': substrate_eco_jstats,
                'ecosystem_sub_jstats': ecosystem_sub_jstats, 'ecosystem_exp_jstats': ecosystem_exp_jstats, 
                'exposure_sub_jstats': exposure_sub_jstats, 'exposure_eco_jstats': exposure_eco_jstats }
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
