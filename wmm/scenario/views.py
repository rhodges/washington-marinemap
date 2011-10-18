from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import *
import settings

'''
'''
def get_params(request, template='scenario/input_parameters.html'):
    if (request.POST):
        is_edit = request.POST.getlist('is_edit')[0] == 'true'
        
        #previous_objs = getlist(request, 'previous_objs[]')
        #param_qs = Parameter.objects.filter(objectives__in=previous_objs)
        #param_set = set(param_qs)
        #prev_params_list = list(param_set)
        
        selected_objs = getlist(request, 'selected_objs[]')
        param_qs = Parameter.objects.filter(objectives__in=selected_objs)
        param_set = set(param_qs)
        parameter_list = list(param_set)
        
        selected_params = getlist(request, 'selected_params[]')
        
        #ensure that any newly appearing parameters will be checked
        #for param in parameter_list:
        #    if param not in prev_params_list:
        #        selected_params.append(param.id) 
                
        context = {'parameter_list': parameter_list, 'checked_list': selected_params}
        return render_to_response(template, RequestContext(request, context)) 
    #return HttpResponse(context)
    
def getlist(request, param_string):
    string_list = request.POST.getlist(param_string)
    list = []
    for s in string_list:
        list.append(int(s))
    return list
    