from general.utils import default_value, sq_meters_to_sq_miles
from aoi.report_caching import report_cache_exists, get_report_cache, create_report_cache

CACHING = 'ON' #set to ON to enable caching
    
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
    if CACHING is 'ON':
        create_report_cache(aoi, report_title, [count, sq_meters_to_sq_miles(area_of_overlap), area_of_overlap / aoi.geometry_final.area])
    return count, sq_meters_to_sq_miles(area_of_overlap), area_of_overlap / aoi.geometry_final.area
    
def get_tuple_report(aoi, model_class, area_class, field_name, report_title):  
    if report_cache_exists(aoi, report_title):
        report_cache = get_report_cache(aoi, report_title)
        return report_cache[0], report_cache[1]
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=aoi.geometry_final)
    report = {}
    for object in overlapping_objs:
        intersection = aoi.geometry_final.intersection(object.geometry)
        attr = getattr(object, field_name)
        if attr not in report.keys():
            report[attr] = intersection.area
        else:
            report[attr] += intersection.area
    report_tuples = []
    for attr, area in report.items():
        try:
            area_object = apply(area_class.objects.get, (), {field_name: attr})
            available_area = area_object.area
        except area_class.DoesNotExist:
            available_area = create_area_record(model_class, area_class, field_name, attr)
        report_tuples.append( (attr, sq_meters_to_sq_miles(area), area/available_area) )
    report_tuples.sort()
    if CACHING is 'ON':
        create_report_cache(aoi, report_title, (len(report_tuples), report_tuples) )
    return len(report_tuples), report_tuples
    
def create_area_record(model_class, area_class, field_name, attr):
    objects = apply(model_class.objects.filter, (), {field_name: attr})
    total_area = 0.0
    for obj in objects:
        total_area += obj.geometry.area
    area_object = apply(area_class, (), {field_name: attr, 'area': total_area})
    area_object.save()
    return total_area    
          
'''
assumes the use of a field called count
'''    
def get_name_count_report(aoi, model_class, field_name, report_title):
    if report_cache_exists(aoi, report_title):
        report_cache = get_report_cache(aoi, report_title)
        return report_cache[0], report_cache[1]
    intersecting_objs = model_class.objects.filter(geometry__bboverlaps=aoi.geometry_final)
    obj_dict = {}
    for object in intersecting_objs:
        key_field = getattr(object, field_name)
        count = object.count
        if key_field not in obj_dict.keys():
            obj_dict[key_field] = count
        else:
            obj_dict[key_field] += count
    tuple_list = [(key, value) for key, value in obj_dict.items()]
    tuple_list.sort()
    if CACHING is 'ON':
        create_report_cache(aoi, report_title, (len(tuple_list), tuple_list) )
    return len(tuple_list), tuple_list
    
def get_cpue_report(aoi, model_class, type_field, cpue_field, report_name):
    if report_cache_exists(aoi, report_name):
        report_cache = get_report_cache(aoi, report_name)
        return report_cache[0], report_cache[1]
    overlapping_objs = model_class.objects.filter(geometry__bboverlaps=aoi.geometry_final)
    count = 0 
    object_tuples = []
    for object in overlapping_objs:
        intersection = aoi.geometry_final.intersection(object.geometry)
        #not sure what happens when intersection is empty geom...
        if intersection.area > 0:
            type = getattr(object, type_field)
            cpue = getattr(object, cpue_field)
            object_tuples.append( (type, cpue, sq_meters_to_sq_miles(intersection.area)) )
            count += 1
    object_tuples.sort()
    if CACHING is 'ON':
        create_report_cache(aoi, report_name, (count, object_tuples))
    return count, object_tuples