from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_cs_phy_analysis(request, cs, template='conservation/reports/physical/conservation_physical_report.html'):
    context = get_cs_phy_context(cs)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_cs_phy_context(cs, type='phy'): 
    #get context from cache or from running analysis
    context = run_cs_phy_analysis(cs)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_cs_phy_analysis(cs, type='phy'): 
    area = cs.geometry_final.area
    #compile context
    context = {'cs': cs, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS}
    return context