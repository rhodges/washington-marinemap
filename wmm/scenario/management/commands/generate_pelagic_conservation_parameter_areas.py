from django.core.management.base import BaseCommand, AppCommand
from optparse import make_option
from lingcod.analysistools.grass import Grass
from scenario.models import *


class Command(BaseCommand):
    help = "Populates the scenario.PelagicConservationParameterArea table with areas measured in sq meters."
    #args = '[pk]'
    model_class = PelagicConservationParameterArea
                
    #def handle(self, pk, **options):
    def handle(self, **options):
        ''' Helper Functions '''
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
                ocpa = self.model_class(name=name, area=area)
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
            '''IN THE CASE OF UPWELLING AND CHLOROPHYL MODELS WE NEED TO REMOVE THE SUPERFLUOUS 0'''
            #del(area_dict[0])
            ''''''
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
        
        # Clean PelagicConservationParameterArea table
        
        self.model_class.objects.all().delete()    

        ''' Top-Level Parameters '''
        
        # Upwelling Stats -- determining area (in meters) for each upwelling type in data extent
        
        upwextent_result = """r.mapcalc "upw_extent = if(extent==1,upwelling,null())" """
        g.run(upwextent_result)
        generate_stats_and_save_to_db('upw_extent', Upwelling)
        
        # Chlorophyll Stats -- determining area (in meters) for each chlorophyll type in data extent 
        
        chlextent_result = """r.mapcalc "chl_extent = if(extent==1,chlorophyll,null())" """
        g.run(chlextent_result)
        generate_stats_and_save_to_db('chl_extent', Chlorophyl)
        
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
            generate_stats_and_save_to_db(raster_name, Chlorophyl, upw_name)
        
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
            generate_stats_and_save_to_db(raster_name, Upwelling, chl_name)
        
        