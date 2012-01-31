from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import *
import settings

'''
'''
def scenario_report(request, mos_id, scenario_id):
    mos_obj = get_object_or_404(MOS, pk=mos_id)
    #check permissions
    viewable, response = mos_obj.is_viewable(request.user)
    if not viewable:
        return response
    scenario_obj = get_object_or_404(Scenario, pk=scenario_id)
    
    if scenario_obj.input_objective.short_name == 'offshore_conservation':
        from mos.offshore_conservation import display_offshore_conservation_report
        return display_offshore_conservation_report(request, mos_obj, scenario_obj)
    elif scenario_obj.input_objective.short_name == 'wind_energy':
        from mos.wind_energy import display_wind_energy_report
        return display_wind_energy_report(request, mos_obj, scenario_obj)
    else:
        return HttpResponse(scenario_obj.input_objective.name + ' Report coming soon...')
    
'''
'''
def overlap_report(request, mos_id):
    mos_obj = get_object_or_404(MOS, pk=mos_id)
    #check permissions
    viewable, response = mos_obj.is_viewable(request.user)
    if not viewable:
        return response
            
    return HttpResponse('Overlap Report coming soon...')
    
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
def get_objs(request, instance):
    context = {}
    return HttpResponse(context)
'''

def list_params(request, template='multi_objective_scenario/list_parameters.html'):
    if request.POST:
        
        initial_objs = getlist(request, 'initial_objs[]')
        initial_param_qs = Parameter.objects.filter(objectives__in=initial_objs)
        initial_param_set = set(initial_param_qs)
        initial_parameter_list = list(initial_param_set)
        initial_params = [param.id for param in initial_parameter_list]
        
        selected_objs = getlist(request, 'selected_objs[]')
        current_params = {}
        for obj_id in selected_objs:
            param_list = Parameter.objects.filter(objectives=obj_id)
            current_params[Objective.objects.get(pk=obj_id)] = param_list
        #param_qs = Parameter.objects.filter(objectives__in=selected_objs)
        #param_set = set(param_qs)
        #parameter_list = list(param_set)
        
        selected_params = getlist(request, 'selected_params[]')
                
        context = {'initial_params': initial_params, 'current_params': current_params, 'checked_list': selected_params}
        return render_to_response(template, RequestContext(request, context)) 
    #return HttpResponse(context)

    
'''
def post_params(request, template='multi_objective_scenario/input_parameters.html'):
    if request.POST:
        selected_params = {}
        selected_objs = getlist(request, 'selected_objs[]')
        for obj_id in selected_objs:
            selected_params[Objective.objects.get(pk=obj_id)] = getlist(request, 'selected_params[%s]'%obj_id)
        #form = request.POST
        context = {'selected_params': selected_params, 'selected_objs': selected_objs, 'form': form}
        return render_to_response(template, RequestContext(request, context))
'''
        
    
def getlist(request, param_string):
    string_list = request.POST.getlist(param_string)
    list = []
    for s in string_list:
        list.append(int(s))
    return list
    