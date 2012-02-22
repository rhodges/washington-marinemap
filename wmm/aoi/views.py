from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import *
import settings

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
def admin_clear_aoi_report_cache(request, title=None, template='admin/aoi/reportcache/cache_is_cleared.html'):
    from aoi.report_caching import clear_report_cache, remove_report_cache
    if not request.user.is_staff:
        return HttpResponse('You do not have permission to view this feature', status=401)
    if request.method == 'POST':
        if title == 'all':
            clear_report_cache(i_am_sure=True)
            return render_to_response( template, RequestContext(request, {"title": "All"}) )  
        else:
            remove_report_cache(title=title)
            import re
            report_name = re.sub('_', ' ', title[:-7]).title()
            return render_to_response( template, RequestContext(request, {"title": report_name}) )  
                
    