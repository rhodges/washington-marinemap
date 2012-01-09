from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_smp_beach_erosion_analysis(request, smp_obj, template='smp/reports/smp_beach_erosion_report.html'):
    context = get_smp_beach_erosion_context(smp_obj)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_smp_beach_erosion_context(smp_obj, type='beach_erosion'): 
    #get context from cache or from running analysis
    context = run_beach_erosion_analysis(smp_obj)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_beach_erosion_analysis(smp_obj, type='beach_erosion'): 
    area = smp_obj.geometry_final.area
    #compile context
    context = {'smp_obj': smp_obj, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS}
    return context