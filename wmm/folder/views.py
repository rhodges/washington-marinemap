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
        
        folder_obj = get_object_or_404(Folder, pk=folder_id)
        #check permissions
        viewable, response = folder_obj.is_viewable(request.user)
        if not viewable:
            return response
        
        from tradeoff.tradeoff_analysis import display_tradeoff_analysis
        return display_tradeoff_analysis(request, folder_obj, x_axis, y_axis)
    
'''
'''
def tradeoff_table(request):
    if (request.POST):
        folder_id = getlist(request, 'folder_id')[0]
        
        folder_obj = get_object_or_404(Folder, pk=folder_id)
        #check permissions
        viewable, response = folder_obj.is_viewable(request.user)
        if not viewable:
            return response
            
        from tradeoff.tradeoff_analysis import display_tradeoff_table
        return display_tradeoff_table(request, folder_obj)        
    
def getlist(request, param_string):
    string_list = request.POST.getlist(param_string)
    list = []
    for s in string_list:
        list.append(int(s))
    return list
    