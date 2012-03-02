from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
#from madrona.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from general.utils import default_value
from aoi.models import *
from aoi.report_caching import report_cache_exists, get_report_cache, create_report_cache
from aoi.report_utils import get_name_count_report, get_count_area_perc_report, get_tuple_report, get_cpue_report

'''
'''
def display_aoi_biological_analysis(request, aoi, template='aoi/reports/conservation/aoi_biological_conservation_report.html'):
    context = get_aoi_biological_context(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def get_aoi_biological_context(aoi): 
    #compile context
    area = aoi.geometry_final.area
    seabird_count, seabirds = get_name_count_report(aoi, Seabird, 'species', 'seabird_report')
    snowy_plover_count, snowy_plover_area, snowy_plover_perc = get_count_area_perc_report(aoi, SnowyPloverHabitat, 'snowy_plover_report')
    haulout_count, haulouts = get_name_count_report(aoi, Haulout, 'com_name', 'haulout_report')
    orca_count, orca_area, orca_perc = get_count_area_perc_report(aoi, OrcaHabitat, 'orca_report')
    kelp_count, kelp_area, kelp_perc = get_count_area_perc_report(aoi, Kelp, 'kelp_report')
    chlorophyll_count, chlorophyll = get_tuple_report(aoi, Chlorophyll, ChlorophyllArea, 'type', 'chlorophyll_report')
    coral_count, coral_tuples = get_cpue_report(aoi, Coral, 'coral_type', 'sum_cpuekg', 'coral_report')
    sponge_count, sponge_tuples = get_cpue_report(aoi, Sponge, 'target_nam', 'cpuekgkm', 'sponge_report')
    oyster_count, oyster_area, oyster_perc = get_count_area_perc_report(aoi, OlympiaOyster, 'oyster_report')
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'seabirds': seabirds, 'haulouts': haulouts, 
                'snowy_plover_count': snowy_plover_count, 'snowy_plover_area': snowy_plover_area, 'snowy_plover_perc': snowy_plover_perc,
                'orca_count': orca_count, 'orca_area': orca_area, 'orca_perc': orca_perc, 
                'kelp_count': kelp_count, 'kelp_area': kelp_area, 'kelp_perc': kelp_perc, 
                'oyster_count': oyster_count, 'oyster_area': oyster_area, 'oyster_perc': oyster_perc, 
                'chlorophyll_count': chlorophyll_count, 'chlorophyll': chlorophyll, 
                'coral_count': coral_count, 'coral_tuples': coral_tuples, 
                'sponge_count': sponge_count, 'sponge_tuples': sponge_tuples }
    return context
  