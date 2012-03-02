from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from madrona.analysistools.grass import Grass
from scenario.models import *
from utils import setup_grass, generate_stats, save_to_db 


class Command(BaseCommand):
    help = "Populates the scenario.TidalEnergyParameterArea table with areas measured in sq meters."
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
        
        # Clean WaveEnergyParameterArea table
        
        TidalEnergyParameterArea.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Substrate Stats -- determining area (in meters) for each substrate in data extent
        
        subextent_result = """r.mapcalc "sub_extent = if(extent==1,tidal_substrate,null())" """
        g.run(subextent_result)
        stats_dict = generate_stats(g, 'sub_extent', TidalSubstrate)
        save_to_db(stats_dict, TidalEnergyParameterArea)
        
        
        