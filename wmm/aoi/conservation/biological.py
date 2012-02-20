from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from lingcod.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from general.utils import default_value, meters_to_miles
from aoi.models import *

'''
'''
def display_aoi_biological_analysis(request, aoi, template='aoi/reports/conservation/aoi_biological_conservation_report.html'):
    context = get_aoi_biological_context(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_aoi_biological_context(aoi): 
    #get context from cache or from running analysis
    context = run_biological_analysis(aoi)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_biological_analysis(aoi): 
    #compile context
    area = aoi.geometry_final.area
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS }
    return context
    