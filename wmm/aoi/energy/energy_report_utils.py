from lingcod.raster_stats.models import RasterDataset, zonal_stats
from general.utils import sq_meters_to_sq_miles
from aoi.report_caching import report_cache_exists, get_report_cache, create_report_cache
from aoi.report_utils import CACHING

'''
'''    
def get_min_max_avg_report(aoi, raster):
    raster_geom = RasterDataset.objects.get(name=raster)
    raster_stats = zonal_stats(aoi.geometry_final, raster_geom)
    min = raster_stats.min 
    max = raster_stats.max 
    avg = raster_stats.avg 
    return min, max, avg
        
'''
'''        
def get_wind_report(aoi, model_class, type_field, report_name):
    if report_cache_exists(aoi, report_name):
        report_cache = get_report_cache(aoi, report_name)
        return report_cache[0], report_cache[1]
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=aoi.geometry_final)
    type_areas = {}
    for object in overlapping_objs:
        intersection = aoi.geometry_final.intersection(object.geometry)
        #not sure what happens when intersection is empty geom...
        if intersection.area > 0:
            type = getattr(object, type_field)
            if type in type_areas.keys():
                type_areas[type] += intersection.area
            else:
                type_areas[type] = intersection.area
    wind_potential_list = ['Poor', 'Marginal', 'Fair', 'Good', 'Excellent', 'Outstanding']    
    tuple_list = [(wp, sq_meters_to_sq_miles(type_areas[wp])) for wp in wind_potential_list if wp in type_areas.keys()]
    count = len(tuple_list)
    if CACHING is 'ON':
        create_report_cache(aoi, report_name, (count, tuple_list))
    return count, tuple_list