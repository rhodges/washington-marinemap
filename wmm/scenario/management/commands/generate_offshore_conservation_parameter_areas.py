from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from lingcod.analysistools.grass import Grass
from scenario.models import *


class Command(BaseCommand):
    help = "Populates the scenario.OffshoreConservationParameterArea table with areas measured in sq meters."
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
                ocpa = OffshoreConservationParameterArea(name=name, area=area)
                ocpa.save()
            
        def stats_to_dict(area_stats):
            area_split = area_stats.split()
            #cast the area elements to integers (no need for the decimal value when dealing with meters)
            area_ints = [int(float(x)+.5) for x in area_split]
            #note: we are now dealing with int areas rather than float strings 
            area_dict = dict(zip(area_ints[::2], area_ints[1::2])) 
            return area_dict
            
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
        
        # Clean OffshoreConservationParameterArea table
        
        OffshoreConservationParameterArea.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Substrate Stats -- determining area (in meters) for each substrate in data extent
        
        subextent_result = """r.mapcalc "sub_extent = if(extent==1,substrate,null())" """
        g.run(subextent_result)
        generate_stats_and_save_to_db('sub_extent', Substrate)
        
        # Depth Class Stats -- determining area (in meters) for each depth class in data extent 
        
        dcextent_result = """r.mapcalc "dc_extent = if(extent==1,depth_class,null())" """
        g.run(dcextent_result)
        generate_stats_and_save_to_db('dc_extent', DepthClass)
        
        # Geomorphology Stats -- determining area (in meters) for each geomorphology in data extent
        
        geoextent_result = """r.mapcalc "geo_extent = if(extent==1,geomorphology,null())" """
        g.run(geoextent_result)
        generate_stats_and_save_to_db('geo_extent', Geomorphology)
        
        ''' Substrate -- Drilling Down '''
        
        #substrate depth_class stats -- collecting area (in meters) of each depth class in each substrate 
        
        substrate_stats = g.run('r.stats -an input=sub_extent')
        substrate_dict = stats_to_dict(substrate_stats)
        sub_ids = substrate_dict.keys()
        for sub_id in sub_ids:
            #generate substrate raster
            sub_name = Substrate.objects.get(id=sub_id).short_name
            substrate_result = """r.mapcalc "%s = if(substrate==%s,sub_extent,null())" """ % (sub_name, sub_id)
            g.run(substrate_result)
            #generate depthclass results for current substrate
            raster_name = '%s_dcresult' %sub_name
            dc_result = """r.mapcalc "%s = if(%s==%s,depth_class,null())" """ %(raster_name, sub_name, sub_id)
            g.run(dc_result)
            generate_stats_and_save_to_db(raster_name, DepthClass, sub_name)
        
        #substrate geomorphology stats -- collecting area (in meters) of each geomorphology in each substrate 
        
        for sub_id in sub_ids:
            #no need to recalculate substrate rasters...            
            sub_name = Substrate.objects.get(id=sub_id).short_name
            #generate geomorphology results for current substrate
            raster_name = '%s_georesult' %sub_name
            geo_result = """r.mapcalc "%s = if(%s==%s,geomorphology,null())" """ %(raster_name, sub_name, sub_id)
            g.run(geo_result)
            generate_stats_and_save_to_db(raster_name, Geomorphology, sub_name)
        
        ''' Depth Class -- Drilling Down '''
        
        #depthclass substrate stats -- collecting area (in meters) of each substrate in each depth class 
        
        depthclass_stats = g.run('r.stats -an input=dc_extent')
        depthclass_dict = stats_to_dict(depthclass_stats)
        dc_ids = depthclass_dict.keys()
        for dc_id in dc_ids:
            #generate depthclass raster
            dc_name = DepthClass.objects.get(id=dc_id).short_name
            depthclass_result = """r.mapcalc "%s = if(depth_class==%s,dc_extent,null())" """ % (dc_name, dc_id)
            g.run(depthclass_result)
            #generate substrate results for current depthclass
            raster_name = '%s_subresult' %dc_name
            dc_result = """r.mapcalc "%s = if(%s==%s,substrate,null())" """ %(raster_name, dc_name, dc_id)
            g.run(dc_result)
            generate_stats_and_save_to_db(raster_name, Substrate, dc_name)
        
        #depth class geomorphology stats -- collecting area (in meters) of each geomorphology in each depthclass  
        
        for dc_id in dc_ids:
            #no need to recalculate substrate rasters...            
            dc_name = DepthClass.objects.get(id=dc_id).short_name
            #generate geomorphology results for current depthclass 
            raster_name = '%s_georesult' %dc_name
            geo_result = """r.mapcalc "%s = if(%s==%s,geomorphology,null())" """ %(raster_name, dc_name, dc_id)
            g.run(geo_result)
            generate_stats_and_save_to_db(raster_name, Geomorphology, dc_name)
        
        ''' Geomorphology -- Drilling Down '''
        
        #geomorphology substrate stats -- collecting area (in meters) of each substrate in each depth class 
        
        geomorphology_stats = g.run('r.stats -an input=geo_extent')
        geomorphology_dict = stats_to_dict(geomorphology_stats)
        geo_ids = geomorphology_dict.keys()
        for geo_id in geo_ids:
            #generate geomorphology raster
            geo_name = Geomorphology.objects.get(id=geo_id).short_name
            geomorphology_result = """r.mapcalc "%s = if(geomorphology==%s,geo_extent,null())" """ % (geo_name, geo_id)
            g.run(geomorphology_result)
            #generate substrate results for current depthclass
            raster_name = '%s_subresult' %geo_name
            geo_result = """r.mapcalc "%s = if(%s==%s,substrate,null())" """ %(raster_name, geo_name, geo_id)
            g.run(geo_result)
            generate_stats_and_save_to_db(raster_name, Substrate, geo_name)
        
        #geomorphology depthclass stats -- collecting area (in meters) of each geomorphology in each depthclass  
        
        for geo_id in geo_ids:
            #no need to recalculate substrate rasters...            
            geo_name = Geomorphology.objects.get(id=geo_id).short_name
            #generate geomorphology results for current depthclass 
            raster_name = '%s_depthclass' %geo_name
            geo_result = """r.mapcalc "%s = if(%s==%s,depth_class,null())" """ %(raster_name, geo_name, geo_id)
            g.run(geo_result)
            generate_stats_and_save_to_db(raster_name, DepthClass, geo_name)
        
        