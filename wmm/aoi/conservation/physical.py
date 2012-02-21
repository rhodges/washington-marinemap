from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from lingcod.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from general.utils import default_value, meters_to_miles, sq_meters_to_sq_miles
from aoi.models import *
from aoi.report_caching import report_cache_exists, get_report_cache, create_report_cache

'''
'''
def display_aoi_physical_analysis(request, aoi, template='aoi/reports/conservation/aoi_physical_conservation_report.html'):
    context = run_physical_analysis(aoi)
    return render_to_response(template, RequestContext(request, context)) 

'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_physical_analysis(aoi): 
    #compile context
    area = aoi.geometry_final.area
    benthic_depths = get_tuple_report(aoi, BenthicHabitat, BenthicDepthArea, 'depth', 'benthic_depth_report')
    benthic_geomorphs = get_tuple_report(aoi, BenthicHabitat, BenthicGeomorphArea, 'geomorph', 'benthic_geomorph_report')
    benthic_substrates = get_tuple_report(aoi, BenthicHabitat, BenthicSubstrateArea, 'substrate', 'benthic_substrate_report')
    canyon_count, canyon_area, canyon_perc = get_count_area_perc_report(aoi, Canyon, 'canyon_report')
    rocky_substrate_count, rocky_substrate_area, rocky_substrate_perc = get_count_area_perc_report(aoi, RockySubstrate, 'rocky_substrate_report')
    estuary_habitats = get_tuple_report(aoi, EstuaryHabitat, EstuaryHabitatArea, 'habitat', 'estuary_habitat_report')
    estuary_substrates = get_tuple_report(aoi, EstuaryHabitat, EstuarySubstrateArea, 'substrate', 'estuary_substrate_report')
    island_count, island_area, island_perc = get_count_area_perc_report(aoi, Island, 'island_report')
    upwellings = get_tuple_report(aoi, Upwelling, UpwellingArea, 'type', 'upwelling_report')
    context = { 'aoi': aoi, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'benthic_depths': benthic_depths, 'benthic_geomorphs': benthic_geomorphs, 'benthic_substrates': benthic_substrates,
                'canyon_area': canyon_area, 'canyon_perc': canyon_perc,
                'rocky_substrate_area': rocky_substrate_area, 'rocky_substrate_perc': rocky_substrate_perc,
                'estuary_habitats': estuary_habitats, 'estuary_substrates': estuary_substrates,
                'island_count': island_count, 'island_area': island_area, 'island_perc': island_perc, 
                'upwellings': upwellings }
    return context
    
def get_count_area_perc_report(aoi, model_class, report_title):
    if report_cache_exists(aoi, report_title):
        report_cache = get_report_cache(aoi, report_title)
        return report_cache[0], report_cache[1], report_cache[2]
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=aoi.geometry_final)
    area_of_overlap = 0.0
    count = 0 
    for object in overlapping_objs:
        intersection = aoi.geometry_final.intersection(object.geometry)
        #not sure what happens when intersection is empty geom...
        if intersection.area > 0:
            area_of_overlap += intersection.area
            count += 1
    create_report_cache(aoi, report_title, [count, sq_meters_to_sq_miles(area_of_overlap), area_of_overlap / aoi.geometry_final.area])
    return count, sq_meters_to_sq_miles(area_of_overlap), area_of_overlap / aoi.geometry_final.area
    
def get_tuple_report(aoi, model_class, area_class, field, report_title):  
    if report_cache_exists(aoi, report_title):
        report_cache = get_report_cache(aoi, report_title)
        return report_cache
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=aoi.geometry_final)
    report = {}
    for object in overlapping_objs:
        intersection = aoi.geometry_final.intersection(object.geometry)
        attr = getattr(object, field)
        if attr not in report.keys():
            report[attr] = intersection.area
        else:
            report[attr] += intersection.area
    report_tuples = []
    for attr, area in report.items():
        try:
            area_object = apply(area_class.objects.get, (), {field: attr})
            available_area = area_object.area
        except area_class.DoesNotExist:
            available_area = create_area_record(model_class, area_class, field, attr)
        report_tuples.append( (attr, sq_meters_to_sq_miles(area), area/available_area) )
    report_tuples.sort()
    create_report_cache(aoi, report_title, report_tuples)
    return report_tuples
    
def create_area_record(model_class, area_class, field, attr):
    objects = apply(model_class.objects.filter, (), {field: attr})
    total_area = 0.0
    for obj in objects:
        total_area += obj.geometry.area
    area_object = apply(area_class, (), {field: attr, 'area': total_area})
    area_object.save()
    return total_area
    
        