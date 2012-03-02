from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from settings import *
from general.utils import default_value, sq_meters_to_sq_miles, meters_to_miles
from smp.models import *

'''
'''
def display_smp_shoreline_use_analysis(request, smp, template='smp/reports/smp_shoreline_use_report.html'):
    context = run_shoreline_use_analysis(smp)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_shoreline_use_analysis(smp): 
    #compile context
    area = smp.geometry_final.area
    undeveloped_area = get_landuse_area(smp, LandUseUndeveloped)
    service_area = get_landuse_area(smp, LandUseServices)
    residential_area = get_landuse_area(smp, LandUseResidential)
    manufacturing_area = get_landuse_area(smp, LandUseManufacturing)
    transportation_area = get_landuse_area(smp, LandUseTransportation)
    trade_area = get_landuse_area(smp, LandUseTrade)
    cultural_area = get_landuse_area(smp, LandUseCultural)
    structure_tuples = get_structures(smp)
    access_sites = get_nearest_access_sites(smp)
    context = { 'smp': smp, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'undeveloped_area': undeveloped_area, 'service_area': service_area, 'residential_area': residential_area,
                'manufacturing_area': manufacturing_area, 'transportation_area': transportation_area, 'trade_area': trade_area,
                'cultural_area': cultural_area, 'structure_tuples': structure_tuples, 'access_sites': access_sites }
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

def get_structures(smp):
    structures = OverwaterStructure.objects.filter(geometry__bboverlaps=smp.geometry_final)
    structure_list = []
    for structure in structures:
        if structure.geometry.intersects(smp.geometry_final):
            type = structure.complexity
            if type in ['Other', 'Fill']:
                type = structure.os_detail
            structure_list.append(type)
    structure_dict = {}
    for type in structure_list:
        if type in structure_dict.keys():
            structure_dict[type] += 1
        else:
            structure_dict[type] = 1
    structure_tuples = [(type, count) for type, count in structure_dict.items()]
    structure_tuples.sort()
    return structure_tuples    

def get_nearest_access_sites(smp):
    #return get_nearest_geometries_with_distances(aes, 'urbangrowthboundaries')
    access_sites = PublicAccess.objects.all()
    existing_sites = [(0.0, site.beach_name) for site in access_sites if site.geometry.intersects(smp.geometry_final)]
    if len(existing_sites) > 0:
        return existing_sites
    else:
        nearest_sites = [(meters_to_miles(site.geometry.distance(smp.geometry_final)), site.beach_name) for site in access_sites]
        nearest_sites.sort()
        return nearest_sites[:1]
        
        