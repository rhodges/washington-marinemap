from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from settings import *
from general.utils import default_value, sq_meters_to_sq_miles
from smp.models import *

'''
'''
def display_smp_public_access_analysis(request, smp, template='smp/reports/smp_public_access_report.html'):
    context = run_public_access_analysis(smp)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_public_access_analysis(smp): 
    #compile context
    area = smp.geometry_final.area
    undeveloped_area = get_landuse_area(smp, LandUseUndeveloped)
    access_sites = get_public_access_sites(smp)
    context = { 'smp': smp, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'undeveloped_area': undeveloped_area, 'access_sites': access_sites }
    return context
     
def get_landuse_area(smp, model_class):
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=smp.geometry_final)
    area_of_overlap = 0.0
    for object in overlapping_objs:
        intersection = smp.geometry_final.intersection(object.geometry)
        if intersection.area > 0:
            area_of_overlap += intersection.area
    area_in_miles = sq_meters_to_sq_miles(area_of_overlap)
    #total_area = sum([area.geometry.area for area in areas if area.geometry.intersects(smp.geometry_final)])
    #area_in_miles = sq_meters_to_sq_miles(total_area)
    return area_in_miles    

def get_public_access_sites(smp):
    access_sites = PublicAccess.objects.all()
    existing_sites = [(site.beach_name, site.class_desc, site.rep_name) for site in access_sites if site.geometry.intersects(smp.geometry_final)]
    return existing_sites
        