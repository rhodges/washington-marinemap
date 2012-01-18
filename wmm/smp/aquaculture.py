from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_smp_aquaculture_analysis(request, smp, template='reports/smp_aquaculture_report.html'):
    context = get_smp_aquaculture_context(smp)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_smp_aquaculture_context(smp): 
    #get context from cache or from running analysis
    context = run_aquaculture_analysis(smp)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_aquaculture_analysis(smp): 
    area = smp.geometry_final.area
    #compile context
    context = {'smp': smp, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS}
    return context