from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from madrona.analysistools.grass import Grass
from scenario.models import *
from utils import setup_grass, generate_stats, save_to_db, stats_to_dict


class Command(BaseCommand):
    help = "Populates the scenario.PelagicConservationParameterArea table with areas measured in sq meters."
    #args = '[pk]'
                
    #def handle(self, pk, **options):
    def handle(self, **options):        
    
        print """
            *****************
            And away we go...
            *****************
        """
        
        # GRASS setup
     
        g = setup_grass() 
        
        # Clean PelagicConservationParameterArea table
        
        PelagicConservationParameterArea.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Upwelling Stats -- determining area (in meters) for each upwelling type in data extent
        
        upwextent_result = """r.mapcalc "upw_extent = if(extent==1,upwelling,null())" """
        g.run(upwextent_result)
        stats_dict = generate_stats(g, 'upw_extent', Upwelling)
        save_to_db(stats_dict, PelagicConservationParameterArea)
        
        # Chlorophyll Stats -- determining area (in meters) for each chlorophyll type in data extent 
        
        chlextent_result = """r.mapcalc "chl_extent = if(extent==1,chlorophyll,null())" """
        g.run(chlextent_result)
        stats_dict = generate_stats(g, 'chl_extent', Chlorophyl)
        save_to_db(stats_dict, PelagicConservationParameterArea)
        
        ''' Upwelling -- Drilling Down '''
        
        #upwelling chlorophyll stats -- collecting area (in meters) of each chlorophyll type in each upwelling type 
        
        upwelling_stats = g.run('r.stats -an input=upw_extent')
        upwelling_dict = stats_to_dict(upwelling_stats)
        upw_ids = upwelling_dict.keys()
        for upw_id in upw_ids:
            #generate upwelling raster
            upw_name = Upwelling.objects.get(id=upw_id).short_name
            upwelling_result = """r.mapcalc "%s = if(upwelling==%s,upw_extent,null())" """ % (upw_name, upw_id)
            g.run(upwelling_result)
            #generate chlorophyll results for current upwelling
            raster_name = '%s_chlresult' %upw_name
            chl_result = """r.mapcalc "%s = if(%s==%s,chlorophyll,null())" """ %(raster_name, upw_name, upw_id)
            g.run(chl_result)
            stats_dict = generate_stats(g, raster_name, Chlorophyl, upw_name)
            save_to_db(stats_dict, PelagicConservationParameterArea)
        
        ''' Chlorophyl -- Drilling Down '''
        
        #chlorophyll upwelling stats -- collecting area (in meters) of each upwelling type in each chlorophyll
        
        chlorophyll_stats = g.run('r.stats -an input=chl_extent')
        chlorophyll_dict = stats_to_dict(chlorophyll_stats)
        chl_ids = chlorophyll_dict.keys()
        for chl_id in chl_ids:
            #generate chlorophyll raster
            chl_name = Chlorophyl.objects.get(id=chl_id).short_name
            chlorophyll_result = """r.mapcalc "%s = if(chlorophyll==%s,chl_extent,null())" """ % (chl_name, chl_id)
            g.run(chlorophyll_result)
            #generate upweeling results for current chlorophyll type
            raster_name = '%s_upwresult' %chl_name
            upw_result = """r.mapcalc "%s = if(%s==%s,upwelling,null())" """ %(raster_name, chl_name, chl_id)
            g.run(upw_result)
            stats_dict = generate_stats(g, raster_name, Upwelling, chl_name)
            save_to_db(stats_dict, PelagicConservationParameterArea)
        
        