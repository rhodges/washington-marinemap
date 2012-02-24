from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from settings import *
from general.utils import default_value, meters_to_miles
from aoi.models import *
from aoi.report_utils import get_tuple_report
from energy_report_utils import get_min_max_avg_report, get_wind_report, get_depth_postscripts

'''
'''
def display_aoi_wind_analysis(request, aoi, template='aoi/reports/energy/aoi_wind_energy_report.html'):
    context = get_aoi_wind_context(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def get_aoi_wind_context(aoi): 
    #compile context
    area = aoi.geometry_final.area
    max_depth, min_depth, avg_depth = get_min_max_avg_report(aoi, 'depth_grid')
    max_depth_postscript, min_depth_postscript, avg_depth_postscript = get_depth_postscripts(max_depth, min_depth, avg_depth)
    substrate_count, substrates = get_tuple_report(aoi, BenthicHabitat, BenthicSubstrateArea, 'substrate', 'benthic_substrate_report')
    wind_power_count, wind_power_tuples = get_wind_report(aoi, WindPower, 'potential', 'wind_power_report')
    wind_power_tuples = add_wind_details(wind_power_tuples)
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'min_depth': min_depth, 'max_depth': max_depth, 'avg_depth': avg_depth,
                'max_depth_postscript': max_depth_postscript, 'min_depth_postscript': min_depth_postscript, 'avg_depth_postscript': avg_depth_postscript, 
                'substrate_count': substrate_count, 'substrates': substrates, 
                'wind_power_count': wind_power_count, 'wind_power_tuples': wind_power_tuples }
    return context
    
def add_wind_details(orig_tuples):
    updated_tuples = []
    for tuple in orig_tuples:
        if tuple[0] == 'Poor':
            updated_tuples.append( (tuple[0], tuple[1], '0 - 200 W/m2, < 12.5 mph') ) #might need a &lt; for less than...
        elif tuple[0] == 'Marginal':
            updated_tuples.append( (tuple[0], tuple[1], '200 - 300 W/m2, 12.5 - 14.3 mph') ) 
        elif tuple[0] == 'Fair':
            updated_tuples.append( (tuple[0], tuple[1], '300 - 400 W/m2, 14.3 - 15.7 mph') ) 
        elif tuple[0] == 'Good':
            updated_tuples.append( (tuple[0], tuple[1], '400 - 500 W/m2, 15.7 - 16.8 mph') ) 
        elif tuple[0] == 'Excellent':
            updated_tuples.append( (tuple[0], tuple[1], '500 - 600 W/m2, 16.8 - 17.9 mph') ) 
        elif tuple[0] == 'Outstanding':
            updated_tuples.append( (tuple[0], tuple[1], '600 - 800 W/m2, 17.9 - 19.7 mph') ) 
    return updated_tuples
            
