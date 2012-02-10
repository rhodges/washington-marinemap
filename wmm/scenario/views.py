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
    elif scenario_obj.input_objective.short_name == 'nearshore_conservation':
        from mos.nearshore_conservation import display_nearshore_conservation_report
        return display_nearshore_conservation_report(request, mos_obj, scenario_obj)
    elif scenario_obj.input_objective.short_name == 'pelagic_conservation':
        from mos.pelagic_conservation import display_pelagic_conservation_report
        return display_pelagic_conservation_report(request, mos_obj, scenario_obj)
    elif scenario_obj.input_objective.short_name == 'wind_energy':
        from mos.wind_energy import display_wind_energy_report
        return display_wind_energy_report(request, mos_obj, scenario_obj)
    elif scenario_obj.input_objective.short_name == 'wave_energy':
        from mos.wave_energy import display_wave_energy_report
        return display_wave_energy_report(request, mos_obj, scenario_obj)
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
 
def list_params(request, template='mos/list_parameters.html'):
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
    
def getlist(request, param_string):
    string_list = request.POST.getlist(param_string)
    list = []
    for s in string_list:
        list.append(int(s))
    return list
    