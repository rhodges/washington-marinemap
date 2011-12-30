from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value
    
'''
'''
def display_scenario_report(request, mos, scenario, template='multi_objective_scenario/reports/scenario_report.html'):
    context = get_scenario_context(mos, scenario)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_scenario_context(mos, scenario): 
    #get context from cache or from running analysis
    context = {'default_value': default_value, 'mos': mos, 'scenario': scenario}
    return context
   