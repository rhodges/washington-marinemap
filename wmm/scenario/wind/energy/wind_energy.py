from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_wind_energy_analysis(request, wind_obj, template='wind/reports/energy/wind_energy_report.html'):
    context = get_wind_energy_context(wind_obj)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_wind_energy_context(wind_obj, type='energy'): 
    #get context from cache or from running analysis
    context = run_wind_energy_analysis(wind_obj)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_wind_energy_analysis(wind_obj, type='energy'): 
    area = wind_obj.geometry_final.area
    #compile context
    context = {'wind_obj': wind_obj, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS}
    return context