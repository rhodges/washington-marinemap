from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from lingcod.raster_stats.models import RasterDataset, zonal_stats
from settings import *
import scenario
from general.utils import default_value, meters_to_miles
from aoi.models import *
from energy_report_utils import get_min_max_avg_report
from aoi.report_utils import get_tuple_report

'''
'''
def display_aoi_tidal_analysis(request, aoi, template='aoi/reports/energy/aoi_tidal_energy_report.html'):
    context = get_aoi_tidal_context(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def get_aoi_tidal_context(aoi): 
    #compile context
    area = aoi.geometry_final.area
    max_depth, min_depth, avg_depth = get_min_max_avg_report(aoi, 'depth')
    substrate_count, substrates = get_tuple_report(aoi, TidalSubstrate, TidalSubstrateArea, 'gridcode', 'tidal_substrate_report')
    substrates = get_substrate_names(substrates)
    min_tidal_mean, max_tidal_mean, avg_tidal_mean = get_min_max_avg_report(aoi, 'tidal_mean_grid')
    min_tidal_max, max_tidal_max, avg_tidal_max = get_min_max_avg_report(aoi, 'tidal_max_grid')
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'min_depth': min_depth, 'max_depth': max_depth, 'avg_depth': avg_depth, 
                'substrate_count': substrate_count, 'substrates': substrates, 
                'min_tidal_mean': min_tidal_mean, 'max_tidal_mean': max_tidal_mean, 'avg_tidal_mean': avg_tidal_mean, 
                'min_tidal_max': min_tidal_max, 'max_tidal_max': max_tidal_max, 'avg_tidal_max': avg_tidal_max }
    return context
    
def get_substrate_names(substrate_tuples):
    updated_tuples = []
    for tuple in substrate_tuples:
        try:
            name = scenario.models.TidalSubstrate.objects.get(id=tuple[0]).name
        except:
            name = tuple[0]
        updated_tuples.append( (name, tuple[1], tuple[2]) )
    return updated_tuples