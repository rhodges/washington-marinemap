from lingcod.manipulators.manipulators import BaseManipulator, ClipToStudyRegionManipulator, ClipToShapeManipulator, DifferenceFromShapeManipulator, manipulatorsDict
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from lingcod.common.utils import LargestPolyFromMulti
#from scenario.models import Scenario
from wmm.wmm_manipulators.models import *

very_small_area = .000000001
        
class ExcludeFederalWatersManipulator(DifferenceFromShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.diff_geom = FederalWaters.objects.current().geometry
            self.diff_geom.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeFederalWatersManipulator while obtaining exclude-from-federal-waters-manipulator geometry from database: " + e.message)    

    class Options:    
        name = 'ExcludeFederalWatersManipulator'
        display_name = 'Exclude Federal Waters'
        description = 'Removes any part of your shape that is within Federal Waters.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/exclude_federal.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[ExcludeFederalWatersManipulator.Options.name] = ExcludeFederalWatersManipulator        

class ExcludeStateWatersManipulator(DifferenceFromShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.diff_geom = StateWaters.objects.current().geometry
            self.diff_geom.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeStateWatersManipulator while obtaining exclude-from-federal-waters-manipulator geometry from database: " + e.message)    

    class Options:    
        name = 'ExcludeStateWatersManipulator'
        display_name = 'Exclude State Waters'
        description = 'Removes any part of your shape that is within State Waters.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/exclude_state.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[ExcludeStateWatersManipulator.Options.name] = ExcludeStateWatersManipulator  
  
class ExcludeTerrestrialManipulator(DifferenceFromShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.diff_geom = Terrestrial.objects.current().geometry
            self.diff_geom.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeTerrestrialManipulator while obtaining exclude-from-federal-waters-manipulator geometry from database: " + e.message)    

    class Options:    
        name = 'ExcludeTerrestrialManipulator'
        display_name = 'Exclude Land Areas'
        description = 'Removes any part of your shape that is terrestrial.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/exclude_terrestrial.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[ExcludeTerrestrialManipulator.Options.name] = ExcludeTerrestrialManipulator        

class ExcludeEstuariesManipulator(DifferenceFromShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.diff_geom = Estuaries.objects.current().geometry
            self.diff_geom.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeEstuariesManipulator while obtaining exclude-from-federal-waters-manipulator geometry from database: " + e.message)    

    class Options:    
        name = 'ExcludeEstuariesManipulator'
        display_name = 'Exclude Estuaries'
        description = 'Removes any part of your shape that is estuarine.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/exclude_estuaries.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[ExcludeEstuariesManipulator.Options.name] = ExcludeEstuariesManipulator        
   

'''     
class ExcludeStateWatersManipulator(BaseManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.inter_geom = TerrestrialAndEstuaries.objects.current().geometry
            self.inter_geom.transform(settings.GEOMETRY_CLIENT_SRID)
            self.diff_geom = EastOfTerritorialSeaLine.objects.current().geometry
            self.diff_geom.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeStateWatersManipulator while obtaining exclude-from-federal-waters-manipulator geometry from database: " + e.message)    

    def manipulate(self):
        #extract target_shape geometry
        target_shape = self.target_to_valid_geom(self.target_shape)
        
        #extract inter_geom geometry
        try:
            inter_geom = GEOSGeometry(self.inter_geom)
            inter_geom.set_srid(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeStateWatersManipulator while initializing geometry on self.inter_geom: " + e.message)
        
        if not inter_geom.valid:
            raise self.InternalException("ExcludeStateWatersManipulator: 'inter_geom' is not a valid geometry")
            
        #extract diff_geom geometry
        try:
            diff_geom = GEOSGeometry(self.diff_geom)
            diff_geom.set_srid(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeStateWatersManipulator while initializing geometry on self.diff_geom: " + e.message)
        
        if not diff_geom.valid:
            raise self.InternalException("ExcludeStateWatersManipulator: 'diff_geom' is not a valid geometry")
                
        #extract any part of the shape east of the shoreline
        try:
            clipped_shape = target_shape.intersection( inter_geom )
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeStateWatersManipulator while intersecting geometries: " + e.message)  
        
        #if there is no geometry left (intersection was empty)
        if clipped_shape.area <= self.zero:
            largest_land_poly = None
        else: #there was overlap
            largest_land_poly = LargestPolyFromMulti(clipped_shape)
        
        #extract any part of the shape in federal waters
        try:
            clipped_shape = target_shape.difference( diff_geom )
        except Exception, e:
            raise self.InternalException("Exception raised in ExcludeStateWatersManipulator while intersecting geometries: " + e.message)  
        
        #if there is no geometry left (difference was empty)
        if clipped_shape.area <= self.zero:
            largest_federal_waters_poly = None
        else: #there was overlap
            largest_federal_waters_poly = LargestPolyFromMulti(clipped_shape)
        
        if largest_land_poly is None and largest_federal_waters_poly is None:
            status_html = self.do_template("2")
            message = "difference resulted in empty geometry"
            raise self.HaltManipulations(message, status_html)
        elif largest_land_poly is None:
            largest_poly = largest_federal_waters_poly
        elif largest_federal_waters_poly is None:
            largest_poly = largest_land_poly        
        elif largest_land_poly.area > largest_federal_waters_poly.area:
            largest_poly = largest_land_poly
        else:
            largest_poly = largest_federal_waters_poly
        
         
        #if there is a remaining geometry
        #largest_poly = LargestPolyFromMulti(clipped_shape)
        status_html = self.do_template("0")
        return self.result(largest_poly, status_html)
        
    class Options:    
        name = 'ExcludeStateWatersManipulator'
        display_name = 'Exclude State Waters'
        description = 'Removes any part of your shape that is within state waters.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/exclude_state_waters.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[ExcludeStateWatersManipulator.Options.name] = ExcludeStateWatersManipulator        
'''        

'''               
class ClipToTerritorialSeaManipulator(ClipToStudyRegionManipulator):

    class Options:
        name = 'ClipToTerritorialSea'
        display_name = "Clip to Territorial Sea"
        #description = "Clip your shape to the study region"
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/territorialsea_clip.html', 
            '2':'wmm_manipulators/outside_territorialsea.html', 
        }
        
manipulatorsDict[ClipToTerritorialSeaManipulator.Options.name] = ClipToTerritorialSeaManipulator
 
   
class TerrestrialOnlyManipulator(ClipToShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.clip_against = Terrestrial.objects.current().geometry
            self.clip_against.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in TerrestrialOnlyManipulator while obtaining geometry from database: " + e.message)    

    class Options:    
        name = 'TerrestrialOnlyManipulator'
        display_name = 'Exclude Marine Areas'
        description = 'Removes any part of your shape that is not terrestrial.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/terrestrial_only.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[TerrestrialOnlyManipulator.Options.name] = TerrestrialOnlyManipulator        
   
class MarineOnlyManipulator(DifferenceFromShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        self.target_shape = target_shape
        try:
            self.diff_geom = Terrestrial.objects.current().geometry
            self.diff_geom.transform(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in MarineOnlyManipulator while obtaining geometry from database: " + e.message)    

    class Options:    
        name = 'MarineOnlyManipulator'
        display_name = 'Exclude Terrestrial Areas'
        description = 'Removes any part of your shape that is not marine.'
        supported_geom_fields = ['PolygonField']

        html_templates = {
            '0':'wmm_manipulators/marine_only.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[MarineOnlyManipulator.Options.name] = MarineOnlyManipulator        
'''
