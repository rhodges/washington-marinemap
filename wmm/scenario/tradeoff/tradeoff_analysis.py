from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_tradeoff_analysis(request, folder_obj, x_axis, y_axis, template='folder/reports/tradeoff_report.html'):
    context = get_tradeoff_context(folder_obj, x_axis, y_axis)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_tradeoff_context(folder_obj, x_axis, y_axis): 
    #get context from cache or from running analysis
    context = run_tradeoff_analysis(folder_obj, x_axis, y_axis)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_tradeoff_analysis(folder_obj, x_axis, y_axis): 
    x_label = get_label(x_axis)
    y_label = get_label(y_axis)
    conservation_sites = get_conservation_site_attributes(folder_obj, x_axis, y_axis)
    conservation_colors = [ "#4bb2c5", "#4bb2c5", "#4bb2c5", "#4bb2c5" ]
    windenergy_sites = get_windenergy_sites(folder_obj, x_axis, y_axis)
    windenergy_colors = [ "#c5b47f", "#c5b47f", "#c5b47f" ]
    context = {'default_value': default_value, 'x_axis': x_axis, 'y_axis': y_axis, 'x_label': x_label, 'y_label': y_label, 'conservation_sites': conservation_sites, 'conservation_colors': conservation_colors, 'windenergy_sites': windenergy_sites, 'windenergy_colors': windenergy_colors}
    return context
    
def get_conservation_site_attributes(folder_obj, x_axis, y_axis):
    conservation_attributes = []
    #the following is a temporary placeholder until we get actual sites and valuations in place...
    conservation_objs = [ [],[],[],[] ]
    size_list = [16, 17, 26, 10]
    name_list = ['Crab Cape', 'OK Coral', 'Pelican Point', 'Barracuda Bay']
    index = 0
    for conservation_site in conservation_objs:
        x_value = get_valuation(conservation_site, x_axis, index)
        y_value = get_valuation(conservation_site, y_axis, index)
        size = size_list[index]
        name = name_list[index]
        attribute_list = [x_value, y_value, size, name]
        conservation_attributes.append(attribute_list)
        index += 1
    return conservation_attributes
    
def get_valuation(site, axis, index):
    conservation_valuation_list = [75, 65, 84, 50, 18, 67, 12]
    wind_valuation_list = [23, 82, 10, 33, 67, 89, 73]
    if axis == 'conservation':
        return conservation_valuation_list[index]
    elif axis == 'wind':
        return wind_valuation_list[index]            
    
def get_windenergy_sites(folder_obj, x_axis, y_axis):
    windenergy_attributes = []
    #the following is a temporary placeholder until we get actual sites and valuations in place...
    windenergy_objs = [ [],[],[] ]
    size_list = [None, None, None, None, 9, 14, 16]
    name_list = [None, None, None, None, 'Blustery Ave', 'Breeze Way', 'Wind Alley']
    index = 4
    for windenergy_site in windenergy_objs:
        x_value = get_valuation(windenergy_site, x_axis, index)
        y_value = get_valuation(windenergy_site, y_axis, index)
        size = size_list[index]
        name = name_list[index]
        attribute_list = [x_value, y_value, size, name]
        windenergy_attributes.append(attribute_list)
        index += 1
    return windenergy_attributes
    
def get_label(selection):
    if selection == 'conservation':
        return 'Conservation Value'
    elif selection == 'wind':
        return 'Wind Energy Value'
    