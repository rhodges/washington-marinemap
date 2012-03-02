from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from madrona.analysistools.grass import Grass
from scenario.models import *
from utils import setup_grass, generate_stats, save_to_db, stats_to_dict


class Command(BaseCommand):
    help = "Populates the scenario.NearshoreConservationParameterArea table with areas measured in sq meters."
    #args = '[pk]'
                
    #def handle(self, pk, **options):
    def handle(self, **options):
    
        print """
            *****************
            And away we go...
            *****************
        """
        
        # GRASS setup
     
        g = setup_grass(cell_size=90) 
        
        # Clean NearshoreConservationParameterArea table
        
        NearshoreConservationParameterArea.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Substrate Stats -- determining area (in meters) for each substrate in data extent
        
        subextent_result = """r.mapcalc "sub_extent = if(extent==1,nearshore_substrate,null())" """
        g.run(subextent_result)
        stats_dict = generate_stats(g, 'sub_extent', NearshoreSubstrate)
        save_to_db(stats_dict, NearshoreConservationParameterArea)
        
        # Exposure Stats -- determining area (in meters) for each exposure class in data extent 
        
        expextent_result = """r.mapcalc "exp_extent = if(extent==1,exposure,null())" """
        g.run(expextent_result)
        stats_dict = generate_stats(g, 'exp_extent', NearshoreExposure)
        save_to_db(stats_dict, NearshoreConservationParameterArea)
        
        # Ecosystems Stats -- determining area (in meters) for each ecosystem in data extent
        
        ecoextent_result = """r.mapcalc "eco_extent = if(extent==1,vegetation,null())" """
        g.run(ecoextent_result)
        stats_dict = generate_stats(g, 'eco_extent', NearshoreEcosystem)
        save_to_db(stats_dict, NearshoreConservationParameterArea)
        
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
            stats_dict = generate_stats(g, raster_name, NearshoreExposure, sub_name)
            save_to_db(stats_dict, NearshoreConservationParameterArea)
        
        #substrate ecosystem stats -- collecting area (in meters) of each ecosystem in each substrate 
        
        for sub_id in sub_ids:
            #no need to recalculate substrate rasters...            
            sub_name = NearshoreSubstrate.objects.get(id=sub_id).short_name
            #generate geomorphology results for current substrate
            raster_name = '%s_ecoresult' %sub_name
            eco_result = """r.mapcalc "%s = if(%s==%s,vegetation,null())" """ %(raster_name, sub_name, sub_id)
            g.run(eco_result)
            stats_dict = generate_stats(g, raster_name, NearshoreEcosystem, sub_name)
            save_to_db(stats_dict, NearshoreConservationParameterArea)
        
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
            stats_dict = generate_stats(g, raster_name, NearshoreSubstrate, exp_name)
            save_to_db(stats_dict, NearshoreConservationParameterArea)
        
        #exposure ecosystem stats -- collecting area (in meters) of each exposure in each ecosystem
        
        for exp_id in exp_ids:
            #no need to recalculate substrate rasters...            
            exp_name = NearshoreExposure.objects.get(id=exp_id).short_name
            #generate ecosystem results for current exposure 
            raster_name = '%s_ecoresult' %exp_name
            eco_result = """r.mapcalc "%s = if(%s==%s,vegetation,null())" """ %(raster_name, exp_name, exp_id)
            g.run(eco_result)
            stats_dict = generate_stats(g, raster_name, NearshoreEcosystem, exp_name)
            save_to_db(stats_dict, NearshoreConservationParameterArea)
        
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
            stats_dict = generate_stats(g, raster_name, NearshoreSubstrate, eco_name)
            save_to_db(stats_dict, NearshoreConservationParameterArea)
        
        #ecosystem exposure stats -- collecting area (in meters) of each ecosystem in each exposure  
        
        for eco_id in eco_ids:
            #no need to recalculate substrate rasters...            
            eco_name = NearshoreEcosystem.objects.get(id=eco_id).short_name
            #generate exposure results for current ecosystem 
            raster_name = '%s_exposure' %eco_name
            exp_result = """r.mapcalc "%s = if(%s==%s,exposure,null())" """ %(raster_name, eco_name, eco_id)
            g.run(exp_result)
            stats_dict = generate_stats(g, raster_name, NearshoreExposure, eco_name)
            save_to_db(stats_dict, NearshoreConservationParameterArea)
        
        