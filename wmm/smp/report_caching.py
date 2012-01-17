from analysis.models import ReportCache

'''
Checks to see if cache for a given report exists in ReportCache table
'''
def report_cache_exists(smp, report):
    try:
        cache = ReportCache.objects.get(wkt_hash=smp.hash)
        if report in cache.context.keys():
            return True
        else:
            return False
    except:
        return False

'''
Retrieves cache for a given report exists in ReportCache table
'''
def get_report_cache(smp, report):
    try:
        cache = ReportCache.objects.get(wkt_hash=smp.hash)
        return cache.context[report]
    except:
        from django.core.exceptions import ObjectDoesNotExist
        raise ObjectDoesNotExist("Cache object (or context key) not found:  make sure report_cache_exists() is called prior to calling get_report_cache()")
    
    
'''
Creates and saves a cache entry for a given report in ReportCache table
'''
def create_report_cache(smp, context):
    #first check to see if cache exists, but context does not
    try:
        cache = ReportCache.objects.get(wkt_hash=smp.hash)
        for key,value in context.items():
            cache.context[key] = value
        cache.save()
    except:
        cache = ReportCache()
        cache.wkt_hash = smp.hash
        cache.context = context
        cache.save()
    
'''
Remove a single geometry from the cache table
'''    
def remove_report_cache(smp=None, data_layer=None):
    if smp is None and data_layer is None:
        raise Exception("For clearing all cached data, use clear_report_cache instead.")
    elif smp is None:
        entries = ReportCache.objects.all()
        for entry in entries:
            if data_layer in entry.context.keys():
                del entry.context[data_layer]
                entry.save()
    elif data_layer is None:
        entries = ReportCache.objects.filter(wkt_hash=smp.hash)
        #remove entries from ReportCache
        for entry in entries:
            ReportCache.delete(entry)
    else:
        entries = ReportCache.objects.filter(wkt_hash=smp.hash)
        for entry in entries:
            if data_layer in entry.context.keys():
                del entry.context[data_layer]
                entry.save()
        
       
'''
Clear all entries from cache table
'''    
def clear_report_cache(i_am_sure=False):
    if not i_am_sure:
        raise Exception("I don't believe you really want to do this...convince me.")
    entries = ReportCache.objects.all()
    for entry in entries:
        ReportCache.delete(entry)
        
