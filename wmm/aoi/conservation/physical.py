from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
#from madrona.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from general.utils import default_value
from aoi.models import *
#from aoi.report_caching import report_cache_exists, get_report_cache, create_report_cache
from aoi.report_utils import get_count_area_perc_report, get_tuple_report

'''
'''
def display_aoi_physical_analysis(request, aoi, template='aoi/reports/conservation/aoi_physical_conservation_report.html'):
    context = get_aoi_physical_analysis(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def get_aoi_physical_analysis(aoi): 
    #compile context
    area = aoi.geometry_final.area
    benthic_depth_count, benthic_depths = get_tuple_report(aoi, BenthicHabitat, BenthicDepthArea, 'depth', 'benthic_depth_report')
    benthic_geomorph_count, benthic_geomorphs = get_tuple_report(aoi, BenthicHabitat, BenthicGeomorphArea, 'geomorph', 'benthic_geomorph_report')
    benthic_substrate_count, benthic_substrates = get_tuple_report(aoi, BenthicHabitat, BenthicSubstrateArea, 'substrate', 'benthic_substrate_report')
    canyon_count, canyon_area, canyon_perc = get_count_area_perc_report(aoi, Canyon, 'canyon_report')
    rocky_substrate_count, rocky_substrate_area, rocky_substrate_perc = get_count_area_perc_report(aoi, RockySubstrate, 'rocky_substrate_report')
    estuary_habitat_count, estuary_habitats = get_tuple_report(aoi, EstuaryHabitat, EstuaryHabitatArea, 'habitat', 'estuary_habitat_report')
    estuary_substrate_count, estuary_substrates = get_tuple_report(aoi, EstuaryHabitat, EstuarySubstrateArea, 'substrate', 'estuary_substrate_report')
    island_count, island_area, island_perc = get_count_area_perc_report(aoi, Island, 'island_report')
    upwelling_count, upwellings = get_tuple_report(aoi, Upwelling, UpwellingArea, 'type', 'upwelling_report')
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'benthic_depth_count': benthic_depth_count, 'benthic_depths': benthic_depths, 
                'benthic_geomorph_count': benthic_geomorph_count, 'benthic_geomorphs': benthic_geomorphs, 
                'benthic_substrate_count': benthic_substrate_count, 'benthic_substrates': benthic_substrates,
                'canyon_area': canyon_area, 'canyon_perc': canyon_perc,
                'rocky_substrate_area': rocky_substrate_area, 'rocky_substrate_perc': rocky_substrate_perc,
                'estuary_habitat_count': estuary_habitat_count, 'estuary_habitats': estuary_habitats, 
                'estuary_substrate_count': estuary_substrate_count, 'estuary_substrates': estuary_substrates,
                'island_count': island_count, 'island_area': island_area, 'island_perc': island_perc, 
                'upwelling_count': upwelling_count, 'upwellings': upwellings }
    return context
