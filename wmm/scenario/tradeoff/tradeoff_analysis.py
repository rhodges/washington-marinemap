from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_tradeoff_analysis(request, folder_obj, template='folder/reports/tradeoff_report.html'):
    context = get_tradeoff_context(folder_obj)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_tradeoff_context(folder_obj): 
    #get context from cache or from running analysis
    context = run_tradeoff_analysis(folder_obj)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_tradeoff_analysis(folder_obj): 
    #compile context
    context = {'default_value': default_value}
    return context