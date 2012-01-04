from lingcod.manipulators.manipulators import BaseManipulator, ClipToShapeManipulator, manipulatorsDict
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from lingcod.common.utils import LargestPolyFromMulti
from scenario.models import Scenario

very_small_area = .0000000000001
   
class ClipToScenarioManipulator(ClipToShapeManipulator):

    def __init__(self, target_shape, **kwargs):
        self.zero = very_small_area
        
        #get the user drawn shape
        self.target_shape = target_shape
        
        #get the scenario geometry
        try:
            #scenario_geom = Scenario.objects.all()[3].geometry_final
            try: 
                scenario_geom = Scenario.objects.get(id=28).geometry_final
            except:
                try:
                    scenario_geom = Scenario.objects.get(id=74).geometry_final
                except:
                    scenario_geom = Scenario.objects.all()[0].geometry_final
            #committing the above with id=28 for demo on thursday
            scenario_geom.transform(settings.GEOMETRY_CLIENT_SRID)
            #clean the scenario
            self.clip_against = scenario_geom.buffer(0)
            if not self.clip_against.valid:
                raise self.InternalException("ClipToScenarioManipulator: scenario is not a valid geometry")
        except Exception, e:
            raise self.InternalException("Exception raised in ClipToScenarioManipulator while obtaining scenario geometry from database: " + e.message)    
    """        
    def manipulate(self):
        #extract target_shape geometry
        target_shape = self.target_to_valid_geom(self.target_shape)
        
        #extract scenario geometry
        try:
            scenario = GEOSGeometry(self.scenario)
            scenario.set_srid(settings.GEOMETRY_CLIENT_SRID)
        except Exception, e:
            raise self.InternalException("Exception raised in ClipToScenarioManipulator while initializing geometry on self.scenario: " + e.message)
        
        #clean scenario geometry
        scenario = scenario.buffer(0)
        if not inter_geom.valid:
            raise self.InternalException("ClipToScenarioManipulator: 'inter_geom' is not a valid geometry")
        
        #intersect scenario with target_shape
        
        
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
    """
    
    class Options:    
        name = 'ClipToScenarioManipulator'
        display_name = 'Clip to Scenario'
        description = 'Removes any part of your shape that is outside the chosen Scenario.'
        supported_geom_fields = ['MultiPolygonField', 'PolygonField']

        html_templates = {
            '0':'wmm_manipulators/clip_to_scenario.html',
            '2':'wmm_manipulators/empty_result.html',
        }

manipulatorsDict[ClipToScenarioManipulator.Options.name] = ClipToScenarioManipulator