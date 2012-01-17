from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from lingcod.raster_stats.models import RasterDataset, zonal_stats
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
    min_slope, max_slope, avg_slope = get_slope(smp_obj)
    #compile context
    context = { 'smp_obj': smp_obj, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'min_slope': min_slope, 'max_slope': max_slope, 'avg_slope': avg_slope }
    return context
    
    

def get_slope(smp):
    slope_geom = RasterDataset.objects.get(name='slope')
    slope_stats = zonal_stats(smp.geometry_final, slope_geom)
    min_slope = slope_stats.min / 100
    max_slope = slope_stats.max / 100
    avg_slope = slope_stats.avg / 100
    return min_slope, max_slope, avg_slope