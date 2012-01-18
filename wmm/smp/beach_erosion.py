from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from lingcod.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from scenario.utils import default_value
from smp.models import *

'''
'''
def display_smp_beach_erosion_analysis(request, smp_obj, template='reports/smp_beach_erosion_report.html'):
    context = get_smp_beach_erosion_context(smp_obj)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_smp_beach_erosion_context(smp_obj, type='beach_erosion'): 
    #get context from cache or from running analysis
    context = run_beach_erosion_analysis(smp_obj)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_beach_erosion_analysis(smp_obj, type='beach_erosion'): 
    area = smp_obj.geometry_final.area
    min_slope, max_slope, avg_slope = get_slope(smp_obj)
    structure_tuples = get_structures(smp_obj)
    #compile context
    context = { 'smp_obj': smp_obj, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'min_slope': min_slope, 'max_slope': max_slope, 'avg_slope': avg_slope,
                'structure_tuples': structure_tuples }
    return context
    
def get_slope(smp):
    slope_geom = RasterDataset.objects.get(name='slope')
    slope_stats = zonal_stats(smp.geometry_final, slope_geom)
    min_slope = slope_stats.min / 100
    max_slope = slope_stats.max / 100
    avg_slope = slope_stats.avg / 100
    return min_slope, max_slope, avg_slope
    
def get_structures(smp):
    #the following might be incorporated for all get_ functions 
    #if report_cache_exists(bioregion, 'structures'):
    #    structure_tuples = get_report_cache(smp, 'structures')
    #    return structure_tuples
    #else:
    structures = OverwaterStructure.objects.filter(geometry__bboverlaps=smp.geometry_final)
    structure_list = [structure.os_detail for structure in structures if structure.geometry.intersects(smp.geometry_final)]
    structure_dict = {}
    for type in structure_list:
        if type in structure_dict.keys():
            structure_dict[type] += 1
        else:
            structure_dict[type] = 1
    structure_tuples = [(type, count) for type, count in structure_dict.items()]
    structure_tuples.sort()
    #structure_tuples = [(structure_tuple[0], structure_tuple[1], convert_sq_km_to_sq_mi(structure_tuple[1])) for structure_tuple in structure_tuples]
    #create_report_cache(bioregion, dict(structures=structure_tuples))
    return structure_tuples    
    
'''   
def get_watersheds(bioregion):
    if report_cache_exists(bioregion, 'watersheds'):
        watershed_tuples = get_report_cache(bioregion, 'watersheds')
        return watershed_tuples
    else:
        watersheds = Watersheds.objects.filter(geometry__bboverlaps=bioregion.output_geom)
        watershed_tuples = [(watershed.geometry.intersection(bioregion.output_geom).area, watershed.maj_name) for watershed in watersheds if watershed.geometry.intersects(bioregion.output_geom)]
        watershed_dict = {}
        for area,name in watershed_tuples:
            if name in watershed_dict.keys():
                watershed_dict[name] += area
            else:
                watershed_dict[name] = area
        watershed_tuples = [(name, convert_float_to_area_display_units(area)) for name,area in watershed_dict.items()]
        watershed_tuples.sort()
        watershed_tuples = [(watershed_tuple[0], watershed_tuple[1], convert_sq_km_to_sq_mi(watershed_tuple[1])) for watershed_tuple in watershed_tuples]
        create_report_cache(bioregion, dict(watersheds=watershed_tuples))
        return watershed_tuples    
'''    