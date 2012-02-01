from lingcod.manipulators.manipulators import BaseManipulator, ClipToStudyRegionManipulator, ClipToShapeManipulator, DifferenceFromShapeManipulator, manipulatorsDict
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from lingcod.common.utils import LargestPolyFromMulti
#from scenario.models import Scenario
from wmm.wmm_manipulators.models import *

very_small_area = .000000001
   
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
 
