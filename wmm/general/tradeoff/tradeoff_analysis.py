from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from math import log
from aoi.models import AOI
from scenario.models import *
from settings import *
from general.utils import default_value, sq_meters_to_sq_miles

THRESHOLD = 60

series_colors = [ "#4bb2c5", "#eaa228", "#c5b47f", "#579575", "#839557", "#958c12",
                "#953579", "#4b5de4", "#d8b83f", "#ff5800", "#0085cc" ]

#type_list elements complete the scoring fieldname <type_list[index]>_score
type_list = [ "conservation", "tidalenergy", "windenergy", "waveenergy" ]
objective_list = [ "Conservation", "Tidal Energy", "Wind Energy", "Wave Energy" ]
    
'''
'''
def display_tradeoff_analysis(request, folder, x_axis, y_axis, smp_ids, aoi_ids, template='folder/reports/tradeoff_report.html'):
    context = run_tradeoff_analysis(folder, x_axis, y_axis, smp_ids, aoi_ids)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_tradeoff_analysis(folder, x_axis, y_axis, smp_ids, aoi_ids): 
    x_label = '%s Score' %x_axis
    y_label = '%s Score' %y_axis
    x_type = get_type(x_axis)
    y_type = get_type(y_axis)
    sites, site_names, site_colors = get_chart_attributes(folder, x_type, y_type, smp_ids, aoi_ids)
    legend_location = determine_legend_location(sites)
    #conservation_colors = [ "#4bb2c5", "#4bb2c5", "#4bb2c5", "#4bb2c5" ]
    #from general.utils import kmlcolor_to_htmlcolor
    #colors = [kmlcolor_to_htmlcolor('778B1A55')] * len(sites)
    context = { 'default_value': default_value, 'x_axis': x_axis, 'y_axis': y_axis, 'x_label': x_label, 'y_label': y_label, 
                'sites': sites, 'site_colors': site_colors, 'site_names': site_names, 'legend_location': legend_location}
    return context
    
'''
'''    
def get_chart_attributes(folder, x_axis, y_axis, smp_ids, aoi_ids):
    aoi_attributes, aoi_names, aoi_colors, color_index = get_chart_attributes_from_feature_set(folder.aoi_set, x_axis, y_axis, aoi_ids)
    smp_attributes, smp_names, smp_colors, color_index = get_chart_attributes_from_feature_set(folder.smp_set, x_axis, y_axis, smp_ids, color_index=color_index)
    attributes = aoi_attributes + smp_attributes
    names = aoi_names + smp_names
    colors = aoi_colors + smp_colors
    return attributes, names, colors
    
def get_chart_attributes_from_feature_set(feature_set, x_axis, y_axis, requested_ids, color_index=0):
    attributes = []
    names = []
    colors = []
    for feature in feature_set:
        if feature.id in requested_ids:
            x_value = get_score(feature, x_axis)
            y_value = get_score(feature, y_axis)
            nlog_size = log(sq_meters_to_sq_miles(feature.geometry_final.area))
            name = str(feature.name)
            names.append(name)
            colors.append(series_colors[color_index%10])
            attribute_list = [x_value, y_value, nlog_size, name]
            attributes.append(attribute_list)
            color_index += 1
    return attributes, names, colors, color_index
    
     
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
    
'''   Tradeoffs Table  '''    
    
'''
'''
def display_tradeoff_table(request, folder, smp_ids, aoi_ids, template='folder/reports/tradeoff_table.html'):  
    context = get_tradeoff_table_context(folder, smp_ids, aoi_ids)   
    return render_to_response(template, RequestContext(request, context))
    
'''
'''
def get_tradeoff_table_context(folder, smp_ids, aoi_ids): 
    sites = get_table_attributes(folder, smp_ids, aoi_ids)
    context = {'default_value': default_value, 'sites': sites, 'objective_list': objective_list, 'threshold': THRESHOLD}
    return context

'''
'''    
def get_scores(site):
    scores_list = []
    for type in type_list:
        scores_list.append(getattr(site, '%s_score' %type))
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
def get_table_attributes(folder, smp_ids, aoi_ids):
    aoi_sites = get_table_attributes_from_feature_set(folder.aoi_set, aoi_ids)
    smp_sites = get_table_attributes_from_feature_set(folder.smp_set, smp_ids)
    sites = aoi_sites + smp_sites
    return sites
    
'''
'''    
def get_table_attributes_from_feature_set(feature_set, requested_ids): 
    sites = [] 
    for feature in feature_set:
        if feature.id in requested_ids:
            site = {}
            site['name'] = str(feature.name)
            site['color'] = series_colors[0]
            scores = get_scores(feature)
            site['scores'] = scores 
            site['conflict'] = has_conflict(scores)
            sites.append(site)      
    return sites

'''
'''
def has_conflict(scores):
    total = 0
    for score in scores:
        if score > THRESHOLD:
            total += 1
    if total > 1: 
        return 'true'
    return 'false'
  