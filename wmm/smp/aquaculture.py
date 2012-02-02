from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from settings import *
from scenario.utils import default_value, sq_meters_to_sq_miles, meters_to_miles
from smp.models import *

'''
'''
def display_smp_aquaculture_analysis(request, smp, template='smp/reports/smp_aquaculture_report.html'):
    context = get_smp_aquaculture_context(smp)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_smp_aquaculture_context(smp): 
    #get context from cache or from running analysis
    context = run_aquaculture_analysis(smp)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_aquaculture_analysis(smp): 
    #compile context
    area = smp.geometry_final.area
    oyster_tract = get_oyster_trace_areas(smp)
    oyster_reserves = get_oyster_reserve_areas(smp)
    growing_areas = get_commercial_growing_area_data(smp)
    harvest_sites = get_harvest_site_data(smp)
    context = { 'smp': smp, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'oyster_tract': oyster_tract, 'oyster_reserves': oyster_reserves, 
                'growing_areas': growing_areas, 'harvest_sites': harvest_sites }
    return context


#TODO:  will need to improve the accuracy here to account for tracts that are only partially overlapped  
def get_oyster_trace_areas(smp):
    oyster_tracts = OysterTract.objects.all()
    total_acres = sum([tract.area_acres for tract in oyster_tracts if tract.geometry.intersects(smp.geometry_final)])
    acres_with_precision = generate_precision(total_acres, 2)
    return acres_with_precision
    
#TODO:  will need to improve the accuracy here to account for tracts that are only partially overlapped  
def get_oyster_reserve_areas(smp):
    oyster_reserves = OysterReserve.objects.all()
    total_acres = sum([reserve.area_acres for reserve in oyster_reserves if reserve.geometry.intersects(smp.geometry_final)])
    acres_with_precision = generate_precision(total_acres, 2)
    return acres_with_precision
    
def get_commercial_growing_area_data(smp):
    growing_areas = CommercialGrowingArea.objects.all()
    area_dict = {}
    for area in growing_areas:
        if area.geometry.intersects(smp.geometry_final):
            if area.status in area_dict.keys():
                area_dict[area.status] += area.acres
            else:
                area_dict[area.status] = area.acres
    areas_with_precision = []
    for status, acreage in area_dict.items():
        areas_with_precision.append( (status, generate_precision(acreage, 2)) )
    areas_with_precision.sort()
    return areas_with_precision
    
    
def get_harvest_site_data(smp):
    harvest_sites = HarvestSite.objects.all()
    site_dict = {}
    for site in harvest_sites:
        if site.geometry.intersects(smp.geometry_final):
            if site.company in site_dict.keys():
                site_dict[site.company] += site.acres
            else:
                site_dict[site.company] = site.acres
    sites_with_precision = []
    for company, acreage in site_dict.items():
        sites_with_precision.append( (company, generate_precision(acreage, 2)) )
    sites_with_precision.sort()
    return sites_with_precision
    
    
def generate_precision(val, prec):
    conversion = (10. ** prec)
    new_val = int(val * conversion) / conversion
    return new_val
    
            