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
        
        from tradeoff.tradeoff_analysis import display_tradeoff_analysis
        folder_obj = get_object_or_404(Folder, pk=folder_id)
        #check permissions
        viewable, response = folder_obj.is_viewable(request.user)
        if not viewable:
            return response
        return display_tradeoff_analysis(request, folder_obj, x_axis, y_axis)
    

'''
'''
def wind_analysis(request, ws_id, type):
    from wind.wind_analysis import display_wind_analysis
    wind_obj = get_object_or_404(WindEnergySite, pk=ws_id)
    #check permissions
    viewable, response = wind_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_wind_analysis(request, wind_obj, type)
    
'''
'''
def conservation_analysis(request, cs_id, type):
    from conservation.conservation_analysis import display_conservation_analysis
    cs_object = get_object_or_404(ConservationSite, pk=cs_id)
    #check permissions
    viewable, response = cs_object.is_viewable(request.user)
    if not viewable:
        return response
    return display_conservation_analysis(request, cs_object, type)
    
'''
'''
def get_params(request, template='scenario/input_parameters.html'):
    if (request.POST):
        is_edit = request.POST.getlist('is_edit')[0] == 'true'
        
        previous_objs = getlist(request, 'initial_objs[]')
        previous_param_qs = Parameter.objects.filter(objectives__in=previous_objs)
        previous_param_set = set(previous_param_qs)
        previous_parameter_list = list(previous_param_set)
        previous_params = [param.id for param in previous_parameter_list]
        
        selected_objs = getlist(request, 'selected_objs[]')
        param_qs = Parameter.objects.filter(objectives__in=selected_objs)
        param_set = set(param_qs)
        parameter_list = list(param_set)
        
        selected_params = getlist(request, 'selected_params[]')
                
        context = {'previous_params': previous_params, 'parameter_list': parameter_list, 'checked_list': selected_params}
        return render_to_response(template, RequestContext(request, context)) 
    #return HttpResponse(context)
    
def getlist(request, param_string):
    string_list = request.POST.getlist(param_string)
    list = []
    for s in string_list:
        list.append(int(s))
    return list
    