from django.http import HttpResponse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404, render_to_response
from madrona.shapes.views import ShpResponder
from models import *
import settings
import re

'''
'''
def aoi_analysis(request, aoi_id, type):
    from aoi.aoi_analysis import display_aoi_analysis
    aoi_obj = get_object_or_404(AOI, pk=aoi_id)
    #check permissions
    viewable, response = aoi_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_aoi_analysis(request, aoi_obj, type)
    
'''
Empties ReportCache table
Handles POST requests
'''
def admin_clear_aoi_report_cache(request, title, template='admin/aoi/reportcache/cache_is_cleared.html'):
    from aoi.report_caching import clear_report_cache, remove_report_cache
    if not request.user.is_staff:
        return HttpResponse('You do not have permission to view this feature', status=401)
    if request.method == 'POST':
        if title == 'all':
            clear_report_cache(i_am_sure=True)
            return render_to_response( template, RequestContext(request, {"title": "All"}) )  
        else:
            remove_report_cache(title=title)
            report_name = re.sub('_', ' ', title[:-7]).title()
            return render_to_response( template, RequestContext(request, {"title": report_name}) )  
         
'''
Empties ZonalStatsCache table
Handles POST requests
'''
def admin_clear_aoi_zonal_cache(request, raster_dataset, template='admin/aoi/zonalcache/zonal_stats_is_cleared.html'):
    from aoi.report_caching import remove_zonal_stats_cache
    if not request.user.is_staff:
        return HttpResponse('You do not have permission to view this feature', status=401)
    if request.method == 'POST':
        raster_title = raster_dataset
        if raster_title.endswith("_grid"):
            raster_title = raster_title[:raster_title.find("_grid")]
        raster_title = re.sub('_', ' ', raster_title).title()
        if raster_dataset == 'all': #not currently implementing the following as it would also clear zonal cache not related to aoi reports
            clear_zonal_cache(i_am_sure=True)
            return render_to_response( template, RequestContext(request, {"title": raster_title, "raster_dataset": raster_dataset}) )  
        else:
            remove_zonal_stats_cache(raster_dataset)
            return render_to_response( template, RequestContext(request, {"title": raster_title, "raster_dataset": raster_dataset}) )  

def aoi_shapefile(request, instances):
    aois = []
    for inst in instances:
        viewable, response = inst.is_viewable(request.user)
        if not viewable:
            return response

        if isinstance(inst, AOI):
            inst.convert_to_shp()
            aois.append(inst)
        #elif isinstance(inst, AOIArray):
        #    for aoi in inst.feature_set(recurse=True,feature_classes=[AOI]):
        #        aoi.convert_to_shp()
        #        aois.append(aoi)
        else:
            pass # ignore anything else

    filename = '_'.join([slugify(inst.name) for inst in instances])
    pks = [aoi.pk for aoi in aois]
    qs = AOIShapefile.objects.filter(aoi_id_num__in=pks)
    if len(qs) == 0:
        return HttpResponse(
            "Nothing in the query set; you don't want an empty shapefile", 
            status=404
        )
    shp_response = ShpResponder(qs)
    shp_response.file_name = slugify(filename[0:8])
    return shp_response()
