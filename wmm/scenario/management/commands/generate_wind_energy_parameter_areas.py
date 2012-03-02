from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from madrona.analysistools.grass import Grass
from scenario.models import *


class Command(BaseCommand):
    help = "Populates the scenario.WindEnergyParameterArea table with areas measured in sq meters."
    #args = '[pk]'
                
    #def handle(self, pk, **options):
    def handle(self, **options):
        ''' Helper Functions have been factored to utils.py '''
        ''' Might factor these out when we get a chance '''
        def generate_stats_and_save_to_db(rast, model_class, param_name=None):
            area_stats = g.run('r.stats -an input=%s' %rast)
            area_dict = stats_to_dict(area_stats)
            if param_name is None:
                area_name_dict = dict( map( lambda(key, value): (model_class.objects.get(id=key).short_name, value), area_dict.items()))
            else:
                area_name_dict = dict( map( lambda(key, value): ('%s_%s' %(param_name, model_class.objects.get(id=key).short_name), value), area_dict.items()))
            save_to_db(area_name_dict)    
            
        def save_to_db(area_dict):
            for name, area in area_dict.items():
                wepa = WindEnergyParameterArea(name=name, area=area)
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
                   
        def setup_grass():
            g = Grass('wa_marine_planner',
                    gisbase=settings.GISBASE, #"/usr/local/grass-6.4.1RC2", 
                    gisdbase=settings.GISDBASE,  #"/mnt/wmm/grass",
                    autoclean=True)
            g.verbose = True
            g.run('g.region rast=bathy')  #sets extent 
            g.run('g.region nsres=180 ewres=180')  #sets cell size
            outdir = settings.GRASS_TMP 
            outbase = 'wa_scenario_%s' % str(time.time()).split('.')[0]
            output = os.path.join(outdir,outbase+'.json')
            if os.path.exists(output):
                raise Exception(output + " already exists")
            extent_result = """r.mapcalc "extent = 1" """
            g.run(extent_result) 
            return g
    
        print """
            *****************
            And away we go...
            *****************
        """
        
        # GRASS setup
     
        g = setup_grass() 
        
        # Clean WindEnergyParameterArea table
        
        WindEnergyParameterArea.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Substrate Stats -- determining area (in meters) for each substrate in data extent
        
        subextent_result = """r.mapcalc "sub_extent = if(extent==1,substrate,null())" """
        g.run(subextent_result)
        generate_stats_and_save_to_db('sub_extent', Substrate)
        
        # Wind Potential Stats -- determining area (in meters) for each wind class in data extent 
        
        windextent_result = """r.mapcalc "wind_extent = if(extent==1,wind,null())" """
        g.run(windextent_result)
        generate_stats_and_save_to_db('wind_extent', WindPotential)
        
        ''' Substrate -- Drilling Down '''
        
        #substrate wind potential stats -- collecting area (in meters) of each wind potential in each substrate 
        
        substrate_stats = g.run('r.stats -an input=sub_extent')
        substrate_dict = stats_to_dict(substrate_stats)
        sub_ids = substrate_dict.keys()
        for sub_id in sub_ids:
            #generate substrate raster
            sub_name = Substrate.objects.get(id=sub_id).short_name
            substrate_result = """r.mapcalc "%s = if(substrate==%s,sub_extent,null())" """ % (sub_name, sub_id)
            g.run(substrate_result)
            #generate depthclass results for current substrate
            raster_name = '%s_windresult' %sub_name
            wind_result = """r.mapcalc "%s = if(%s==%s,wind,null())" """ %(raster_name, sub_name, sub_id)
            g.run(wind_result)
            generate_stats_and_save_to_db(raster_name, WindPotential, sub_name)
        
        ''' Wind Potential -- Drilling Down '''
        
        #wind potential substrate stats -- collecting area (in meters) of each substrate in each wind class 
        
        wind_stats = g.run('r.stats -an input=wind_extent')
        wind_dict = stats_to_dict(wind_stats)
        wind_ids = wind_dict.keys()
        for wind_id in wind_ids:
            #generate wind raster
            wind_name = WindPotential.objects.get(id=wind_id).short_name
            wind_result = """r.mapcalc "%s = if(wind==%s,wind_extent,null())" """ % (wind_name, wind_id)
            g.run(wind_result)
            #generate substrate results for current depthclass
            raster_name = '%s_subresult' %wind_name
            sub_result = """r.mapcalc "%s = if(%s==%s,substrate,null())" """ %(raster_name, wind_name, wind_id)
            g.run(sub_result)
            generate_stats_and_save_to_db(raster_name, Substrate, wind_name)
        
        
        