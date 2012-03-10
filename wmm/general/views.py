from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import *
import settings

'''
'''
def tradeoff_analysis(request):
    if (request.POST):
        x_axis = request.POST.getlist('selected_x')[0]
        y_axis = request.POST.getlist('selected_y')[0]
        folder_id = getlist(request, 'folder_id')[0]
        smp_ids = getlist(request, 'smps[]')
        aoi_ids = getlist(request, 'aois[]')
        
        folder_obj = get_object_or_404(AnalysisFolder, pk=folder_id)
        #check permissions
        viewable, response = folder_obj.is_viewable(request.user)
        if not viewable:
            return response
        
        from tradeoff.tradeoff_analysis import display_tradeoff_analysis
        return display_tradeoff_analysis(request, folder_obj, x_axis, y_axis, smp_ids, aoi_ids)
    
'''
'''
def tradeoff_table(request):
    if (request.POST):
        folder_id = getlist(request, 'folder_id')[0]
        smp_ids = getlist(request, 'smps[]')
        aoi_ids = getlist(request, 'aois[]')
        folder_obj = get_object_or_404(AnalysisFolder, pk=folder_id)
        #check permissions
        viewable, response = folder_obj.is_viewable(request.user)
        if not viewable:
            return response
            
        from tradeoff.tradeoff_analysis import display_tradeoff_table
        return display_tradeoff_table(request, folder_obj, smp_ids, aoi_ids)        
    
def getlist(request, param_string):
    string_list = request.POST.getlist(param_string)
    list = []
    for s in string_list:
        list.append(int(s))
    return list
    