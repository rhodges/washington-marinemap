from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from lingcod.raster_stats.models import RasterDataset, zonal_stats
from settings import *
from general.utils import default_value, meters_to_miles
from smp.models import *

'''
'''
def display_smp_beach_erosion_analysis(request, smp, template='smp/reports/smp_beach_erosion_report.html'):
    context = get_smp_beach_erosion_context(smp)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_smp_beach_erosion_context(smp): 
    #get context from cache or from running analysis
    context = run_beach_erosion_analysis(smp)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_beach_erosion_analysis(smp): 
    #compile context
    area = smp.geometry_final.area
    min_slope, max_slope, avg_slope = get_slope(smp)
    drift_cell_tuples = get_drift_cell_tuples(smp)
    structure_tuples = get_structures(smp)
    shoremod_perc = get_shoremod_avg(smp)
    sand, sand_mud, sand_gravel = get_sand_perc(smp)
    exposed, very_exposed = get_exposure_percs(smp)
    seagrass, saltmarsh, surfgrass    = get_vegetation_percs(smp)
    context = { 'smp': smp, 'default_value': default_value, 'area': area, 'area_units': settings.DISPLAY_AREA_UNITS,
                'min_slope': min_slope, 'max_slope': max_slope, 'avg_slope': avg_slope, 
                'drift_cell_tuples': drift_cell_tuples, 'structure_tuples': structure_tuples, 
                'shoremod_perc': shoremod_perc, 
                'sand': sand, 'sand_mud': sand_mud, 'sand_gravel': sand_gravel, 
                'exposed': exposed, 'very_exposed': very_exposed,
                'seagrass': seagrass, 'saltmarsh': saltmarsh, 'surfgrass': surfgrass }
    return context
    
def get_slope(smp):
    slope_geom = RasterDataset.objects.get(name='slope')
    slope_stats = zonal_stats(smp.geometry_final, slope_geom)
    min_slope = slope_stats.min 
    max_slope = slope_stats.max 
    avg_slope = slope_stats.avg 
    return min_slope, max_slope, avg_slope
    
def get_drift_cell_tuples(smp):
    drift_cells = DriftCell.objects.filter(geometry__bboverlaps=smp.geometry_final)
    dc_dict = {}
    for dc in drift_cells:
        if dc.geometry.intersects(smp.geometry_final):
            length = dc.geometry.intersection(smp.geometry_final).length
            description = dc.description
            if description not in dc_dict.keys():
                dc_dict[description] = length
            else:
                dc_dict[description] += length
    dc_list = [(meters_to_miles(length), description) for description, length in dc_dict.items()]
    dc_list.sort(reverse=True)
    return dc_list        
    
def get_structures(smp):
    #the following might be incorporated for all get_ functions 
    #if report_cache_exists(bioregion, 'structures'):
    #    structure_tuples = get_report_cache(smp, 'structures')
    #    return structure_tuples
    #else:
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
    #structure_tuples = [(structure_tuple[0], structure_tuple[1], convert_sq_km_to_sq_mi(structure_tuple[1])) for structure_tuple in structure_tuples]
    #create_report_cache(bioregion, dict(structures=structure_tuples))
    return structure_tuples    
    
def get_shoremod_avg(smp):
    shoremod_geom = RasterDataset.objects.get(name='shoremod')
    shoremod_stats = zonal_stats(smp.geometry_final, shoremod_geom)
    if shoremod_stats.avg:
        avg_modification = shoremod_stats.avg / 100
    else:
        avg_modification = default_value
    return avg_modification
    
def get_sand_perc(smp):
    substrate_geom = RasterDataset.objects.get(name='substrate')
    substrate_stats = zonal_stats(smp.geometry_final, substrate_geom)
    sand_perc, sand_mud_perc, sand_gravel_perc = [[],[],[]]
    if substrate_stats.pixels:
        total_pixels = 0.0
        categories = substrate_stats.categories.all()
        substrate_dict = {}
        for cat in categories:
            if cat.category in range(1,15):
                substrate_dict[cat.category] = cat.count
                total_pixels += cat.count
        sand_perc = []
        if 9 in substrate_dict.keys():
            sand_perc = [substrate_dict[9]/total_pixels]
        sand_mud_perc = []
        if 4 in substrate_dict.keys():
            sand_mud_perc = [substrate_dict[4]/total_pixels]
        sand_gravel_perc = []
        if 10 in substrate_dict.keys():
            sand_gravel_perc = [substrate_dict[10]/total_pixels]
    return sand_perc, sand_mud_perc, sand_gravel_perc
    
    
def get_exposure_percs(smp):
    exposure_geom = RasterDataset.objects.get(name='exposure')
    exposure_stats = zonal_stats(smp.geometry_final, exposure_geom)
    exposed, very_exposed = [[],[]]
    if exposure_stats.pixels:
        total_pixels = 0.0
        categories = exposure_stats.categories.all()
        exposure_dict = {}
        for cat in categories:
            if cat.category in range(1,6):
                exposure_dict[cat.category] = cat.count
                total_pixels += cat.count
        exposed = []
        very_exposed = []
        if 1 in exposure_dict.keys():
            exposed = [exposure_dict[1]/total_pixels]
        if 4 in exposure_dict.keys():
            very_exposed = [exposure_dict[4]/total_pixels]
    return exposed, very_exposed
    
def get_vegetation_percs(smp): 
    veg_geom = RasterDataset.objects.get(name='vegetation')
    veg_stats = zonal_stats(smp.geometry_final, veg_geom)
    seagrass,saltmarsh,surfgrass = [[],[],[]]
    if veg_stats.pixels:
        total_pixels = 0.0
        categories = veg_stats.categories.all()
        veg_dict = {}
        for cat in categories:
            if cat.category in range(1,11):
                veg_dict[cat.category] = cat.count
                total_pixels += cat.count
        seagrass,saltmarsh,surfgrass = [[],[],[]]
        if 7 in veg_dict.keys():
            seagrass = [veg_dict[7]/total_pixels]
        if 6 in veg_dict.keys():
            saltmarsh = [veg_dict[6]/total_pixels]
        if 9 in veg_dict.keys():
            surfgrass = [veg_dict[9]/total_pixels]
    return seagrass, saltmarsh, surfgrass   
    
  