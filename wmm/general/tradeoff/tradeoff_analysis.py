from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from aoi.models import AOI
from scenario.models import *
from settings import *
from general.utils import default_value, sq_meters_to_sq_miles

series_colors = [ "#4bb2c5", "#eaa228", "#c5b47f", "#579575", "#839557", "#958c12",
                "#953579", "#4b5de4", "#d8b83f", "#ff5800", "#0085cc" ]

#type_list elements complete the scoring fieldname <type_list[index]>_score
type_list = [ "conservation", "tidalenergy", "windenergy", "waveenergy" ]
objective_list = [ "Conservation", "Tidal Energy", "Wind Energy", "Wave Energy" ]
    
'''
'''
def display_tradeoff_analysis(request, folder, x_axis, y_axis, template='folder/reports/tradeoff_report.html'):
    context = get_tradeoff_context(folder, x_axis, y_axis)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_tradeoff_context(folder, x_axis, y_axis): 
    #get context from cache or from running analysis
    context = run_tradeoff_analysis(folder, x_axis, y_axis)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_tradeoff_analysis(folder, x_axis, y_axis): 
    x_label = '%s Score' %x_axis
    y_label = '%s Score' %y_axis
    x_type = get_type(x_axis)
    y_type = get_type(y_axis)
    sites, site_names, site_colors = get_chart_attributes(folder, x_type, y_type)
    legend_location = determine_legend_location(sites)
    #conservation_colors = [ "#4bb2c5", "#4bb2c5", "#4bb2c5", "#4bb2c5" ]
    #from general.utils import kmlcolor_to_htmlcolor
    #colors = [kmlcolor_to_htmlcolor('778B1A55')] * len(sites)
    context = { 'default_value': default_value, 'x_axis': x_axis, 'y_axis': y_axis, 'x_label': x_label, 'y_label': y_label, 
                'sites': sites, 'site_colors': site_colors, 'site_names': site_names, 'legend_location': legend_location}
    return context
    
'''
'''    
def get_chart_attributes(folder, x_axis, y_axis):
    attributes = []
    #the following is a temporary placeholder until we get actual sites and valuations in place...
    #objs = [ [],[],[],[] ]
    aois = folder.feature_set()
    names = []
    colors = []
    index = 0
    for aoi in aois:
        x_value = get_score(aoi, x_axis)
        y_value = get_score(aoi, y_axis)
        from math import log
        nlog_size = log(sq_meters_to_sq_miles(aoi.geometry_final.area))
        name = str(aoi.name)
        names.append(name)
        colors.append(series_colors[index%10])
        attribute_list = [x_value, y_value, nlog_size, name]
        attributes.append(attribute_list)
        index += 1
    return attributes, names, colors
     
'''
'''    
def get_score(aoi, type):
    try:
        score = getattr(aoi, '%s_score' %type)
        return score
    except:
        return -1
    
def determine_legend_location(sites):
    quadrants = {}
    for site in sites:
        quadrant = get_quadrant(site[0], site[1])
        if quadrant in quadrants.keys():
            quadrants[quadrant] += 1
        else:
            quadrants[quadrant] = 1
    if 'sw' not in quadrants.keys():
        return 'sw'
    elif 'se' not in quadrants.keys():
        return 'se'
    elif 'nw' not in quadrants.keys():
        return 'nw'
    elif 'ne' not in quadrants.keys():
        return 'ne'
    quadrant_tuples = [(count, quad) for quad, count in quadrants.items()]
    quadrant_tuples.sort()
    return quadrant_tuples[0][1]
    
    
def get_quadrant(x,y):
    if x >= 50 and y >= 50:
        return 'ne'
    elif x < 50 and y >= 50:
        return 'nw'
    elif x < 50 and y < 50:
        return 'sw'
    else:
        return 'se'
    
'''
'''
def display_tradeoff_table(request, folder, template='folder/reports/tradeoff_table.html'):
    context = get_tradeoff_table_context(folder)   
    return render_to_response(template, RequestContext(request, context))
    
'''
'''
def get_tradeoff_table_context(folder):
    threshold = 60
    sites = get_table_attributes(folder, threshold)
    context = {'default_value': default_value, 'sites': sites, 'objective_list': objective_list, 'threshold': threshold}
    return context

'''
'''    
def get_scores(aoi):
    scores_list = []
    for type in type_list:
        scores_list.append(getattr(aoi, '%s_score' %type))
    return scores_list
    
'''
'''    
def get_type(objective):
    try:
        type = type_list[objective_list.index(objective)]
        return type
    except: 
        return 'type not found'

'''
'''
def get_table_attributes(folder, threshold):
    sites = []
    #site = [name, color, valuations]
    aois = folder.feature_set()
    for aoi in aois:
        site = {}
        site['name'] = str(aoi.name)
        site['color'] = series_colors[0]
        scores = get_scores(aoi)
        site['scores'] = scores
        site['conflict'] = has_conflict(scores, threshold)
        sites.append(site)
    return sites

'''
'''
def has_conflict(scores, threshold):
    total = 0
    for score in scores:
        if score > threshold:
            total += 1
    if total > 1: 
        return 'true'
    return 'false'
  