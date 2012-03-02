from aoi.models import ReportCache

'''
Checks to see if cache for a given report exists in ReportCache table
'''
def report_cache_exists(aoi, title):
    try:
        cache = ReportCache.objects.get(wkt_hash=aoi.hash, title=title)
        return True
    except:
        return False

'''
Retrieves cache for a given report exists in ReportCache table
'''
def get_report_cache(aoi, title):
    try:
        cache = ReportCache.objects.get(wkt_hash=aoi.hash, title=title)
        return cache.report
    except:
        from django.core.exceptions import ObjectDoesNotExist
        raise ObjectDoesNotExist("Cache object not found:  make sure report_cache_exists() is called prior to calling get_report_cache()")
    
    
'''
Creates and saves a cache entry for a given report in ReportCache table
'''
def create_report_cache(aoi, title, report):
    #first check to see if cache exists, but context does not
    try:
        cache = ReportCache.objects.get(wkt_hash=aoi.hash, title=title)
        for key,value in report.items():
            cache.report[key] = value
        cache.save()
    except:
        cache = ReportCache()
        cache.wkt_hash = aoi.hash
        cache.title = title
        cache.report = report
        cache.save()
    
'''
Remove a single geometry from the cache table
'''    
def remove_report_cache(hash=None, title=None):
    if hash is None and title is None:
        raise Exception("For clearing all cached data, use clear_report_cache instead.")
    elif hash is None:
        entries = ReportCache.objects.filter(title=title)
        for entry in entries:
            ReportCache.delete(entry)
    elif title is None:
        entries = ReportCache.objects.filter(wkt_hash=hash)
        #remove entries from ReportCache
        for entry in entries:
            ReportCache.delete(entry)
    else:
        entries = ReportCache.objects.filter(wkt_hash=hash, title=title)
        for entry in entries:
            ReportCache.delete(entry)
        
def remove_zonal_stats_cache(raster_name):         
    from madrona.raster_stats.models import RasterDataset, ZonalStatsCache
    try:
        raster_id = RasterDataset.objects.get(name=raster_name).id
    except:
        raise Exception("RasterDataset with name=%s was not found" %raster_name)
    cache_objects = ZonalStatsCache.objects.filter(raster__id=raster_id)
    cache_objects.delete()
    
    
       
'''
Clear all entries from cache table
'''    
def clear_report_cache(i_am_sure=False):
    if not i_am_sure:
        raise Exception("I don't believe you really want to do this...convince me.")
    entries = ReportCache.objects.all()
    for entry in entries:
        ReportCache.delete(entry)
        
