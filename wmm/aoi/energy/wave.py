from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from madrona.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from general.utils import default_value, meters_to_miles
from aoi.models import *
from aoi.report_utils import get_tuple_report
from energy_report_utils import get_min_max_avg_report, get_depth_postscripts

'''
'''
def display_aoi_wave_analysis(request, aoi, template='aoi/reports/energy/aoi_wave_energy_report.html'):
    context = get_aoi_wave_context(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def get_aoi_wave_context(aoi): 
    #compile context
    area = aoi.geometry_final.area
    max_depth, min_depth, avg_depth = get_min_max_avg_report(aoi, 'depth_grid')
    max_depth_postscript, min_depth_postscript, avg_depth_postscript = get_depth_postscripts(max_depth, min_depth, avg_depth)
    substrate_count, substrates = get_tuple_report(aoi, BenthicHabitat, BenthicSubstrateArea, 'substrate', 'benthic_substrate_report')
    #from time import time as clock 
    #start = clock()
    #min_summer, max_summer, avg_summer = get_min_max_avg_report(aoi, 'wave_summer')
    #time = clock() - start
    #print 'Time spent on wave summer tif: %s' %time
    #start = clock()
    min_summer, max_summer, avg_summer = get_min_max_avg_report(aoi, 'wave_summer_grid')
    #time = clock() - start
    #print 'Time spent on wave summer grid: %s' %time
    #start = clock()
    #min_winter, max_winter, avg_winter = get_min_max_avg_report(aoi, 'wave_winter')
    #time = clock() - start
    #print 'Time spent on wave winter tif: %s' %time
    #start = clock()
    min_winter, max_winter, avg_winter = get_min_max_avg_report(aoi, 'wave_winter_grid')
    #time = clock() - start
    #print 'Time spent on wave winter grid: %s' %time
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'min_depth': min_depth, 'max_depth': max_depth, 'avg_depth': avg_depth,
                'max_depth_postscript': max_depth_postscript, 'min_depth_postscript': min_depth_postscript, 'avg_depth_postscript': avg_depth_postscript, 
                'substrate_count': substrate_count, 'substrates': substrates, 
                'min_summer': min_summer, 'max_summer': max_summer, 'avg_summer': avg_summer, 
                'min_winter': min_winter, 'max_winter': max_winter, 'avg_winter': avg_winter }
    return context
    