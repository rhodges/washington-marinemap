from madrona.analysistools.grass import Grass
from scenario.models import *

''' Helper Functions '''
def generate_stats(g, rast, model_class, param_name=None):
    area_stats = g.run('r.stats -an input=%s' %rast)
    area_dict = stats_to_dict(area_stats)
    if param_name is None:
        area_name_dict = dict( map( lambda(key, value): (model_class.objects.get(id=key).short_name, value), area_dict.items()))
    else:
        area_name_dict = dict( map( lambda(key, value): ('%s_%s' %(param_name, model_class.objects.get(id=key).short_name), value), area_dict.items()))
    return area_name_dict
    
def save_to_db(area_dict, area_model_class):
    for name, area in area_dict.items():
        wepa = area_model_class(name=name, area=area)
        wepa.save()
    
def stats_to_dict(area_stats):
    area_list = area_stats.split()
    #cast the area elements to integers (no need for the decimal value when dealing with meters)
    clean_list = clean_stats_list(area_list)
    area_ints = [int(float(x)+.5) for x in clean_list]
    #note: we are now dealing with int areas rather than float strings 
    area_dict = dict(zip(area_ints[::2], area_ints[1::2])) 
    return area_dict

def clean_stats_list(list):
    clean_list = []
    #note the following '-' search is taking care to remove possible range values in stats list
    for item in list:
        if '-' in item:
            clean_list.append( item[:item.find('-')] )
        else:
            clean_list.append(item)
    return clean_list
           
def setup_grass(cell_size=180):
    g = Grass('wa_marine_planner',
            gisbase=settings.GISBASE, #"/usr/local/grass-6.4.1RC2", 
            gisdbase=settings.GISDBASE,  #"/mnt/wmm/grass",
            autoclean=True)
    g.verbose = True
    g.run('g.region rast=bathy')  #sets extent 
    g.run('g.region nsres=%s ewres=%s' %(cell_size, cell_size))  #sets cell size
    outdir = settings.GRASS_TMP 
    outbase = 'wa_scenario_%s' % str(time.time()).split('.')[0]
    output = os.path.join(outdir,outbase+'.json')
    if os.path.exists(output):
        raise Exception(output + " already exists")
    extent_result = """r.mapcalc "extent = 1" """
    g.run(extent_result) 
    return g
    