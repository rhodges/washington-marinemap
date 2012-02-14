from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from lingcod.analysistools.grass import Grass
from scenario.models import *


class Command(BaseCommand):
    help = "Populates the scenario.NearshoreConservationParameterArea table with areas measured in sq meters."
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
                ocpa = NearshoreConservationParameterArea(name=name, area=area)
                ocpa.save()
        
        def clean_stats_list(list):
            clean_list = []
            #note the following '-' search is taking care to remove possible range values in stats list
            for item in list:
                if '-' in item:
                    clean_list.append( item[:item.find('-')] )
                else:
                    clean_list.append(item)
            return clean_list    
            
        def stats_to_dict(area_stats):
            area_split = area_stats.split()
            clean_list = clean_stats_list(area_split)
            #cast the area elements to integers (no need for the decimal value when dealing with meters)
            area_ints = [int(float(x)+.5) for x in clean_list]
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
            '''NOTE the use of 90m cell size here as we are determining nearshore conservation areas'''
            g.run('g.region nsres=90 ewres=90')  #sets cell size
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
        
        # Clean NearshoreConservationParameterArea table
        
        NearshoreConservationParameterArea.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Substrate Stats -- determining area (in meters) for each substrate in data extent
        
        subextent_result = """r.mapcalc "sub_extent = if(extent==1,nearshore_substrate,null())" """
        g.run(subextent_result)
        generate_stats_and_save_to_db('sub_extent', NearshoreSubstrate)
        
        # Exposure Stats -- determining area (in meters) for each exposure class in data extent 
        
        expextent_result = """r.mapcalc "exp_extent = if(extent==1,exposure,null())" """
        g.run(expextent_result)
        generate_stats_and_save_to_db('exp_extent', NearshoreExposure)
        
        # Ecosystems Stats -- determining area (in meters) for each ecosystem in data extent
        
        ecoextent_result = """r.mapcalc "eco_extent = if(extent==1,vegetation,null())" """
        g.run(ecoextent_result)
        generate_stats_and_save_to_db('eco_extent', NearshoreEcosystem)
        
        ''' Substrate -- Drilling Down '''
        
        #substrate exposure stats -- collecting area (in meters) of each exposure in each substrate 
        
        substrate_stats = g.run('r.stats -an input=sub_extent')
        substrate_dict = stats_to_dict(substrate_stats)
        sub_ids = substrate_dict.keys()
        for sub_id in sub_ids:
            #generate substrate raster
            sub_name = NearshoreSubstrate.objects.get(id=sub_id).short_name
            substrate_result = """r.mapcalc "%s = if(nearshore_substrate==%s,sub_extent,null())" """ % (sub_name, sub_id)
            g.run(substrate_result)
            #generate exposure results for current substrate
            raster_name = '%s_expresult' %sub_name
            exp_result = """r.mapcalc "%s = if(%s==%s,exposure,null())" """ %(raster_name, sub_name, sub_id)
            g.run(exp_result)
            generate_stats_and_save_to_db(raster_name, NearshoreExposure, sub_name)
        
        #substrate ecosystem stats -- collecting area (in meters) of each ecosystem in each substrate 
        
        for sub_id in sub_ids:
            #no need to recalculate substrate rasters...            
            sub_name = NearshoreSubstrate.objects.get(id=sub_id).short_name
            #generate geomorphology results for current substrate
            raster_name = '%s_ecoresult' %sub_name
            eco_result = """r.mapcalc "%s = if(%s==%s,vegetation,null())" """ %(raster_name, sub_name, sub_id)
            g.run(eco_result)
            generate_stats_and_save_to_db(raster_name, NearshoreEcosystem, sub_name)
        
        ''' Exposure -- Drilling Down '''
        
        #exposure substrate stats -- collecting area (in meters) of each substrate in each exposure
        
        exposure_stats = g.run('r.stats -an input=exp_extent')
        exposure_dict = stats_to_dict(exposure_stats)
        exp_ids = exposure_dict.keys()
        for exp_id in exp_ids:
            #generate exposure raster
            exp_name = NearshoreExposure.objects.get(id=exp_id).short_name
            exposure_result = """r.mapcalc "%s = if(exposure==%s,exp_extent,null())" """ % (exp_name, exp_id)
            g.run(exposure_result)
            #generate substrate results for current exposure
            raster_name = '%s_subresult' %exp_name
            sub_result = """r.mapcalc "%s = if(%s==%s,nearshore_substrate,null())" """ %(raster_name, exp_name, exp_id)
            g.run(sub_result)
            generate_stats_and_save_to_db(raster_name, NearshoreSubstrate, exp_name)
        
        #exposure ecosystem stats -- collecting area (in meters) of each exposure in each ecosystem
        
        for exp_id in exp_ids:
            #no need to recalculate substrate rasters...            
            exp_name = NearshoreExposure.objects.get(id=exp_id).short_name
            #generate ecosystem results for current exposure 
            raster_name = '%s_ecoresult' %exp_name
            eco_result = """r.mapcalc "%s = if(%s==%s,vegetation,null())" """ %(raster_name, exp_name, exp_id)
            g.run(eco_result)
            generate_stats_and_save_to_db(raster_name, NearshoreEcosystem, exp_name)
        
        ''' Ecosystem -- Drilling Down '''
        
        #ecosystem substrate stats -- collecting area (in meters) of each substrate in each ecosystem
        
        ecosystem_stats = g.run('r.stats -an input=eco_extent')
        ecosystem_dict = stats_to_dict(ecosystem_stats)
        eco_ids = ecosystem_dict.keys()
        for eco_id in eco_ids:
            #generate ecosystem raster
            eco_name = NearshoreEcosystem.objects.get(id=eco_id).short_name
            ecosystem_result = """r.mapcalc "%s = if(vegetation==%s,eco_extent,null())" """ % (eco_name, eco_id)
            g.run(ecosystem_result)
            #generate substrate results for current ecosystem
            raster_name = '%s_subresult' %eco_name
            sub_result = """r.mapcalc "%s = if(%s==%s,nearshore_substrate,null())" """ %(raster_name, eco_name, eco_id)
            g.run(sub_result)
            generate_stats_and_save_to_db(raster_name, NearshoreSubstrate, eco_name)
        
        #ecosystem exposure stats -- collecting area (in meters) of each ecosystem in each exposure  
        
        for eco_id in eco_ids:
            #no need to recalculate substrate rasters...            
            eco_name = NearshoreEcosystem.objects.get(id=eco_id).short_name
            #generate exposure results for current ecosystem 
            raster_name = '%s_exposure' %eco_name
            exp_result = """r.mapcalc "%s = if(%s==%s,exposure,null())" """ %(raster_name, eco_name, eco_id)
            g.run(exp_result)
            generate_stats_and_save_to_db(raster_name, NearshoreExposure, eco_name)
        
        