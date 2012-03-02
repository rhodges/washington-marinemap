from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from settings import *
from general.utils import default_value, sq_meters_to_sq_miles, meters_to_miles, sq_meters_to_acres
from smp.models import *

'''
'''
def display_smp_aquaculture_analysis(request, smp, template='smp/reports/smp_aquaculture_report.html'):
    context = run_aquaculture_analysis(smp)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_aquaculture_analysis(smp): 
    #compile context
    area = smp.geometry_final.area
    oyster_tract = get_oyster_acres(smp, OysterTract)
    oyster_reserves = get_oyster_acres(smp, OysterReserve)
    growing_areas = get_commercial_acres(smp, CommercialGrowingArea, 'status')
    harvest_sites = get_harvest_site_data(smp)
    context = { 'smp': smp, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'oyster_tract': oyster_tract, 'oyster_reserves': oyster_reserves, 
                'growing_areas': growing_areas, 'harvest_sites': harvest_sites }
    return context


def get_oyster_acres(smp, model_class):
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=smp.geometry_final)
    area_of_overlap = 0.0
    for object in overlapping_objs:
        intersection = smp.geometry_final.intersection(object.geometry)
        if intersection.area > 0:
            area_of_overlap += intersection.area
    total_acres = sq_meters_to_acres(area_of_overlap)
    return total_acres
    
def get_commercial_acres(smp, model_class, field_name):
    commercial_objects = model_class.objects.filter(geometry__bboverlaps=smp.geometry_final)
    area_dict = {}
    for object in commercial_objects:
        intersection = smp.geometry_final.intersection(object.geometry)
        type = getattr(object, field_name)
        if type in area_dict.keys():
            area_dict[type] += intersection.area
        else:
            area_dict[type] = intersection.area
    areas_with_precision = []
    for type, acreage in area_dict.items():
        areas_with_precision.append( (type, sq_meters_to_acres(acreage)) )
    areas_with_precision.sort()
    return areas_with_precision
    
'''
HarvestSite is a point layer so we are limited in our ability to measure acreage more acccurately
'''    
def get_harvest_site_data(smp):
    harvest_sites = HarvestSite.objects.filter(geometry__bboverlaps=smp.geometry_final)
    site_dict = {}
    for site in harvest_sites:
        if site.company in site_dict.keys():
            site_dict[site.company] += site.acres
        else:
            site_dict[site.company] = site.acres
    sites_with_precision = []
    for company, acreage in site_dict.items():
        sites_with_precision.append( (company, acreage) )
    sites_with_precision.sort()
    return sites_with_precision
    