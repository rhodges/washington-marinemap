import time
import os
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from lingcod.analysistools.models import Analysis
from lingcod.features import register, alternate
from lingcod.common.utils import asKml
from lingcod.features.models import Feature, PointFeature, LineFeature, PolygonFeature, FeatureCollection
from lingcod.layers.models import PrivateLayerList
from utils import miles_to_meters, feet_to_meters
from django.utils import simplejson


@register
class Folder(FeatureCollection):
    description = models.TextField(null=True,blank=True)
    
    @property
    def num_scenarios(self):
        count = 0
        for object in self.feature_set():
            if object.__class__ == MOS:
                count += 1
        return count
        
    @property
    def num_conservation_sites(self):
        count = 0
        for object in self.feature_set():
            if object.__class__ == ConservationSite:
                count += 1
        return count
        
    @property
    def num_windenergy_sites(self):
        count = 0
        for object in self.feature_set():
            if object.__class__ == WindEnergySite:
                count += 1
        return count
        
    class Options:
        verbose_name = 'Folder'
        valid_children = ( 'scenario.models.MOS', 
                           'scenario.models.ConservationSite',
                           'scenario.models.WindEnergySite',
                           'scenario.models.AOI', 
                           'scenario.models.POI', 
                           'scenario.models.LOI', 
                           'scenario.models.UserKml', 
                           'lingcod.bookmarks.models.Bookmark', 
                           'scenario.models.Folder')
        form = 'scenario.forms.FolderForm'
        form_template = 'folder/form.html'
        show_template = 'folder/show.html'
        icon_url = 'wmm/img/folder.png'

@register
class MOS(Feature):
    scenarios = models.ManyToManyField("Scenario", null=True, blank=True)
    input_objectives = models.ManyToManyField("Objective", null=True, blank=True)
        
    # Renewable Energy Parameters
    input_objectives_energy = models.ManyToManyField("EnergyObjective", null=True, blank=True)
    
    input_parameters_tidal_energy = models.ManyToManyField("TidalEnergyParameter", null=True, blank=True)
    input_dist_shore_tidal_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_tidal_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_tidal_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_tidal_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_tidal_energy = models.ManyToManyField("Substrate", related_name="MOSTidalEnergySubstrate", null=True, blank=True)
    input_depth_class_tidal_energy = models.ManyToManyField("DepthClass", related_name="MOSTidalEnergyDepthClass", null=True, blank=True)    
    input_geomorphology_tidal_energy = models.ManyToManyField("Geomorphology", related_name="MOSTidalEnergyGeomorphology", null=True, blank=True)
    
    input_parameters_wind_energy = models.ManyToManyField("WindEnergyParameter")
    input_dist_shore_wind_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_wind_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_wind_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_wind_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_wind_energy = models.ManyToManyField("Substrate", related_name="MOSWindEnergySubstrate", null=True, blank=True)
    input_depth_class_wind_energy = models.ManyToManyField("DepthClass", related_name="MOSWindEnergyDepthClass", null=True, blank=True)    
    input_geomorphology_wind_energy = models.ManyToManyField("Geomorphology", related_name="MOSWindEnergyGeomorphology", null=True, blank=True)
    
    input_parameters_wave_energy = models.ManyToManyField("WaveEnergyParameter")
    input_dist_shore_wave_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_wave_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_wave_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_wave_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_wave_energy = models.ManyToManyField("Substrate", related_name="MOSWaveEnergySubstrate", null=True, blank=True)
    input_depth_class_wave_energy = models.ManyToManyField("DepthClass", related_name="MOSWaveEnergyDepthClass", null=True, blank=True)    
    input_geomorphology_wave_energy = models.ManyToManyField("Geomorphology", related_name="MOSWaveEnergyGeomorphology", null=True, blank=True)
    
    # Conservation Parameters
    
    input_objectives_conservation = models.ManyToManyField("ConservationObjective", null=True, blank=True)
    
    input_parameters_offshore_conservation = models.ManyToManyField("OffshoreConservationParameter")
    input_dist_shore_offshore_conservation = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_offshore_conservation = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_offshore_conservation = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_offshore_conservation = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_offshore_conservation = models.ManyToManyField("Substrate", related_name="MOSOffshoreConservationSubstrate", null=True, blank=True)
    input_depth_class_offshore_conservation = models.ManyToManyField("DepthClass", related_name="MOSOffshoreConservationDepthClass", null=True, blank=True)    
    input_geomorphology_offshore_conservation = models.ManyToManyField("Geomorphology", related_name="MOSOffshoreConservationGeomorphology", null=True, blank=True)
    
    input_parameters_nearshore_conservation = models.ManyToManyField("NearshoreConservationParameter")
    input_dist_shore_nearshore_conservation = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_nearshore_conservation = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_nearshore_conservation = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_nearshore_conservation = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_nearshore_conservation = models.ManyToManyField("Substrate", related_name="MOSNearshoreConservationSubstrate", null=True, blank=True)
    input_depth_class_nearshore_conservation = models.ManyToManyField("DepthClass", related_name="MOSNearshoreConservationDepthClass", null=True, blank=True)    
    input_geomorphology_nearshore_conservation = models.ManyToManyField("Geomorphology", related_name="MOSNearshoreConservationGeomorphology", null=True, blank=True)
    
    input_parameters_water_column_conservation = models.ManyToManyField("WaterColumnConservationParameter")
    input_dist_shore_water_column_conservation = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_water_column_conservation = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_water_column_conservation = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_water_column_conservation = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_water_column_conservation = models.ManyToManyField("Substrate", related_name="MOSWaterColumnConservationSubstrate", null=True, blank=True)
    input_depth_class_water_column_conservation = models.ManyToManyField("DepthClass", related_name="MOSWaterColumnConservationDepthClass", null=True, blank=True)    
    input_geomorphology_water_column_conservation = models.ManyToManyField("Geomorphology", related_name="MOSWaterColumnConservationGeomorphology", null=True, blank=True)
    
    # Development Parameters
    
    input_objectives_development = models.ManyToManyField("DevelopmentObjective", null=True, blank=True)
    
    input_parameters_shoreside_development = models.ManyToManyField("ShoresideDevelopmentParameter")
    input_dist_shore_shoreside_development = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_shoreside_development = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_shoreside_development = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_shoreside_development = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_shoreside_development = models.ManyToManyField("Substrate", related_name="MOSShoresideDevelopmentSubstrate", null=True, blank=True)
    input_depth_class_shoreside_development = models.ManyToManyField("DepthClass", related_name="MOSShoresideDevelopmentDepthClass", null=True, blank=True)    
    input_geomorphology_shoreside_development = models.ManyToManyField("Geomorphology", related_name="MOSShoresideDevelopmentGeomorphology", null=True, blank=True)
    
    # Fisheries Parameters
    
    input_objectives_fisheries = models.ManyToManyField("FisheriesObjective", null=True, blank=True)
    
    input_parameters_shellfish_aquaculture = models.ManyToManyField("ShellfishAquacultureParameter")
    input_dist_shore_shellfish_aquaculture = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_shellfish_aquaculture = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_shellfish_aquaculture = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_shellfish_aquaculture = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_shellfish_aquaculture = models.ManyToManyField("Substrate", related_name="MOSShellfishAquacultureSubstrate", null=True, blank=True)
    input_depth_class_shellfish_aquaculture = models.ManyToManyField("DepthClass", related_name="MOSShellfishAquacultureDepthClass", null=True, blank=True)    
    input_geomorphology_shellfish_aquaculture = models.ManyToManyField("Geomorphology", related_name="MOSShellfishAquacultureGeomorphology", null=True, blank=True)
    
    input_parameters_offshore_fishing = models.ManyToManyField("OffshoreFishingParameter")
    input_dist_shore_offshore_fishing = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_offshore_fishing = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_offshore_fishing = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_offshore_fishing = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_offshore_fishing = models.ManyToManyField("Substrate", related_name="MOSOffshoreFishingSubstrate", null=True, blank=True)
    input_depth_class_offshore_fishing = models.ManyToManyField("DepthClass", related_name="MOSOffshoreFishingDepthClass", null=True, blank=True)    
    input_geomorphology_offshore_fishing = models.ManyToManyField("Geomorphology", related_name="MOSOffshoreFishingGeomorphology", null=True, blank=True)
        
    description = models.TextField(null=True, blank=True)
    support_file = models.FileField(upload_to='scenarios/files/', null=True, blank=True)
       
    
    def delete(self, *args, **kwargs):
        scenarios = Scenario.objects.filter(mos=self.id)
        scenarios.delete()
        super(MOS, self).delete(*args, **kwargs)
      
    def save(self, form=None, *args, **kwargs):
        if form is not None: 
            form_data = form.cleaned_data 
            user = form_data['user'] 
            self.name = form_data['name']
            #NOTE:  This might need to be used to save self (maybe with form kwarg?) to save instance before scenarios are built
            super(MOS, self).save(form=form)
            
            #accumulate input objectives into single field
            energy_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_energy']]
            conservation_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_conservation']]
            development_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_development']]
            fisheries_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_fisheries']]

            #run analysis on scenarios only when necessary
            for obj in self.input_objectives.all():
                rerun = None
                obj_short_name = obj.short_name
                #note:  this is not the name provided in the kml.  this name is purely for referential purposes
                scenario_name = self.name + '_%s' % obj_short_name
                
                params = form_data['input_parameters_%s'%obj_short_name]
                input_params = [param.parameter for param in params]
                
                #do we need to grab these from the form or are they already stored in the MOS fields?
                #probably stored in the fields already, but we do this to keep the code re-usable for all objectives
                dist_shore = form_data['input_dist_shore_%s'%obj_short_name]
                dist_port = form_data['input_dist_port_%s'%obj_short_name]
                min_depth = form_data['input_min_depth_%s'%obj_short_name]
                max_depth = form_data['input_max_depth_%s'%obj_short_name]
                substrates = form_data['input_substrate_%s'%obj_short_name]
                depth_classes = form_data['input_depth_class_%s'%obj_short_name]
                geomorphologies = form_data['input_geomorphology_%s'%obj_short_name]
                
                scenarios = self.scenarios.filter(mos=self.id, input_objective=obj)
                if len(scenarios) > 1: #not expecting this case to ever happen -- might want to log this event if it does...
                    for scenario in scenarios:
                        self.scenarios.remove(scenario) 
                        scenario.delete()
                    scenarios = []
                if len(scenarios) == 1:
                    scenario = scenarios[0]
                    scenario_dict = {'user': user, 'name': scenario_name, 'input_parameters': input_params, 'input_objective': obj, 'input_dist_shore': dist_shore, 'input_dist_port': dist_port, 'input_min_depth': min_depth, 'input_max_depth': max_depth}
                    if scenario.needs_rerun(scenario_dict):
                        rerun = True
                    scenario.__dict__.update(scenario_dict)
                else:
                    scenario = Scenario(user=user, name=scenario_name, input_objective=obj, input_dist_shore=dist_shore, input_dist_port = dist_port, input_min_depth=min_depth, input_max_depth=max_depth)            
                scenario.save(rerun=False)
                
                if set(scenario.input_parameters.all()) != set(input_params) or set(scenario.input_substrate.all()) != set(substrates) or set(scenario.input_depth_class.all()) != set(depth_classes) or set(scenario.input_geomorphology.all()) != set(geomorphologies):
                    rerun = True   
                scenario.input_parameters = input_params                    
                scenario.input_substrate = substrates                    
                scenario.input_depth_class = depth_classes                    
                scenario.input_geomorphology = geomorphologies
                
                scenario.save(rerun=rerun)
                self.scenarios.add(scenario)
        
        #remove any unwanted scenarios
        objs = self.input_objectives.all()
        scenarios = self.scenarios.exclude(input_objective__in=objs)
        scenarios.delete()
        
        #TODO:  why are we running analysis twice when creating scenarios initially???
        super(MOS, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name
        
    def support_filename(self):
        return os.path.basename(self.support_file.name)
    
    @property
    def objective_ids(self):
        obj_ids = [scenario.input_objective.id for scenario in self.scenarios.all()]
        return obj_ids
         
    #def mos_name(self, scenario):
    #    return scenario.mos_set.all()[0].name
       
    @property       
    def description_html(self):
        if self.description:
            return "<p><strong>Description:</strong> %s</p>" %self.description
        else:
            return ""
        
    def parameter_html(self, scenario):
        html = "" 
        parameter_ids = scenario.input_parameter_ids
        if 1 in parameter_ids:
            #the symbol had to be replaced with &#60; ('<' breaks the html, and &lt; was not working either for some reason...)
            html += "<p><strong> Distance to Shore</strong> &#60;= %s miles</p>" % scenario.input_dist_shore
        if 2 in parameter_ids:
            #the symbol had to be replaced with &#60; ('<' breaks the html, and &lt; was not working either for some reason...)
            html += "<p><strong> Distance to Port</strong> &#60;= %s miles</p>" % scenario.input_dist_port
        if 3 in parameter_ids:
            html += "<p><strong> Depth Range:</strong> %s to %s feet</p>" % (scenario.input_min_depth, scenario.input_max_depth)
        if 5 in parameter_ids:
            html += '<p><strong> Substrates:</strong> [ '
            html += ", ".join(scenario.input_substrate_names)
            html += " ]</p>"
            #html += "<ul>"
            #for substrate in scenario.input_substrate_names:
            #    html += "<li>%s</li>" %substrate
            #html += "</ul></p>"
        if 6 in parameter_ids:
            html += "<p><strong> Depth Classes:</strong> [ "
            html += ", ".join(scenario.input_depth_class_names)
            html += " ]</p>"
            #html += "<ul>"
            #for depth_class in scenario.input_depth_class_names:
            #    html += "<li>%s</li>" %depth_class
            #html += "</ul></p>"
        if 7 in parameter_ids:
            html += "<p><strong> Geomorphologies:</strong> [ "
            html += ", ".join(scenario.input_geomorphology_names)
            html += " ]</p>"
            #html += "<ul>"
            #for geomorphology in scenario.input_geomorphology_names:
            #    html += "<li>%s</li>" %geomorphology
            #html += "</ul></p>"
        return html 
         
    '''
    @property 
    def kml_working(self):
        return """
        <Placemark id="%s">
            <visibility>0</visibility>
            <name>%s (WORKING)</name>
        </Placemark>
        """ % (self.uid, escape(self.name))
    '''
    '''
    def get_scenarios_kml(self):
        scenarios_kml = ""
        scenarios = self.scenarios.all()
        for scenario in scenarios:
            scenario_kml = asKml(scenario.output_geom.transform( settings.GEOMETRY_CLIENT_SRID, clone=True))
            scenarios_kml += scenario_kml
        return scenarios_kml
    '''    
    @property 
    def kml(self):        
        combined_kml = '<Folder id="%s"><name>%s</name><visibility>0</visibility><open>0</open>' %(self.uid, self.name)
        #mos_name = escape(self.name)
        #print 'mos_name = %s' %mos_name
        for scenario in self.scenarios.all():
            obj = scenario.input_objective.name
            #name = scenario.mos_set.all()[0].name #why is this not working...?
            kml =   """
                    %s
                    <Placemark>
                        <visibility>1</visibility>
                        <name>%s</name>
                        <styleUrl>#%s-default</styleUrl>
                        <ExtendedData>
                            <Data name="mos_name"><value>%s</value></Data>
                            <Data name="obj"><value>%s</value></Data>
                            <Data name="user"><value>%s</value></Data>
                            <Data name="desc"><value>%s</value></Data>
                            <Data name="params"><value>%s</value></Data>
                            <Data name="type"><value>%s</value></Data>
                            <Data name="modified"><value>%s</value></Data>
                        </ExtendedData>
                        <MultiGeometry>
                        %s
                        </MultiGeometry>
                    </Placemark>
                    """ % ( self.scenario_style(scenario.color), obj, self.model_uid(),
                            self.name, obj, self.user, escape(self.description_html), escape(self.parameter_html(scenario)),
                            self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
                            asKml(scenario.output_geom.transform( settings.GEOMETRY_CLIENT_SRID, clone=True)) )
            combined_kml += kml
        combined_kml += "</Folder>"
        return combined_kml
    
    def scenario_style(self, color='778B1A55'):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752">
                    <p><strong>Multi-Objective Scenario:</strong> $[mos_name]</p>
                    $[desc]
                    <p><strong>Objective:</strong> $[obj]</p> 
                    <p>$[params]</p>
                    <p>
                    </font>                    
                    <font size=1>$[type] created by $[user] on $[modified]</font>
                ]]> </text>
            </BalloonStyle>
            <IconStyle>
                <color>ffffffff</color>
                <colorMode>normal</colorMode>
                <scale>0.9</scale> 
                <Icon> <href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href> </Icon>
            </IconStyle>
            <LabelStyle>
                <color>ffffffff</color>
                <scale>0.8</scale>
            </LabelStyle>
            <PolyStyle>
                <color>%s</color>
            </PolyStyle>
        </Style>
        """ % (self.model_uid(), color)
    
    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752"><strong>$[name]</strong></font><br />
                    <p>$[desc]</p>
                    <font size=1>$[type] created by $[user] on $[modified]</font>
                ]]> </text>
            </BalloonStyle>
            <IconStyle>
                <color>ffffffff</color>
                <colorMode>normal</colorMode>
                <scale>0.9</scale> 
                <Icon> <href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href> </Icon>
            </IconStyle>
            <LabelStyle>
                <color>ffffffff</color>
                <scale>0.8</scale>
            </LabelStyle>
            <PolyStyle>
                <color>778B1A55</color>
            </PolyStyle>
        </Style>
        """ % (self.model_uid())
        
    class Options:
        verbose_name = 'Multi-Objective Scenario'
        icon_url = 'wmm/img/multi.png'
        form = 'scenario.forms.MOSForm'
        form_template = 'multi_objective_scenario/form.html'
        show_template = 'multi_objective_scenario/show.html'

class Scenario(Analysis):
    #Input Parameters
    input_objective = models.ForeignKey("Objective")
    input_parameters = models.ManyToManyField("Parameter", null=True, blank=True) 
    
    input_dist_shore = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    
    input_substrate = models.ManyToManyField("Substrate", null=True, blank=True)    
    input_depth_class = models.ManyToManyField("DepthClass", null=True, blank=True)    
    input_geomorphology = models.ManyToManyField("Geomorphology", null=True, blank=True)
    
    # All output fields should be allowed to be Null/Blank
    output_geom = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Scenario Geometry")
    output_mapcalc = models.CharField(max_length=360, null=True, blank=True)
    output_area = models.FloatField(verbose_name="Total Area (sq km)", null=True, blank=True)
    
    output_substrate_stats = models.TextField(max_length=360, null=True, blank=True)
    output_depth_class_stats = models.TextField(max_length=360, null=True, blank=True)
    output_geomorphology_stats = models.TextField(max_length=360, null=True, blank=True)
    
    geometry_final = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Final Scenario Geometry")
    
    def run(self):
        from lingcod.analysistools.grass import Grass
        #print
        #print 'RUNNING GRASS ANALYSIS ON: %s' %self.name 
        #print
        #TODO: should change the following GRASS Location name to a settings var...
        #g = Grass('pacnw_utm10', 
        g = Grass('wa_marine_planner',
                gisbase=settings.GISBASE, #"/usr/local/grass-6.4.1RC2", 
                gisdbase=settings.GISDBASE,  #"/mnt/wmm/grass",
                autoclean=True)
        g.verbose = True
        
        g.run('g.region rast=bathy')  #sets extent 
        #g.run('g.region rast=geomorphology')
        g.run('g.region nsres=180 ewres=180')  #sets cell size
        rasts = g.list()['rast']

        outdir = settings.GRASS_TMP #'/tmp'
        outbase = 'wa_scenario_%s' % str(time.time()).split('.')[0]
        output = os.path.join(outdir,outbase+'.json')
        if os.path.exists(output):
            raise Exception(output + " already exists")
        
        input_params = self.input_parameter_ids
        result = 0
        
        #The following integers relate to the primary ids in the scenario_parameter table
        #TODO swap out numbers with parameter_names (I'm thinking the volatility that is introduced is worth the increase in readability)
        if 1 in input_params:
            g.run('r.buffer input=shoreline_rast output=shoreline_rast_buffer distances=%s' % miles_to_meters(self.input_dist_shore) )
            shoreline_buffer = 'if(shoreline_rast_buffer==2)'
        else:
            shoreline_buffer = 1
        
        if 2 in input_params:
            g.run('v.buffer input=ports output=port_buffer distance=%s' % miles_to_meters(self.input_dist_port) )
            g.run('v.to.rast input=port_buffer output=port_buffer_rast use=cat')
            port_buffer = 'if(port_buffer_rast)'
        else:
            port_buffer = 1
        
        if 3 in input_params:
            depth = 'if(bathy <= %s && bathy >= %s)' % (-feet_to_meters(self.input_min_depth), -feet_to_meters(self.input_max_depth))
        else:
            depth = 1
            
        if 5 in input_params:
            substrate_formula = ' || '.join(['substrate==%s' % substrate.id for substrate in self.input_substrate.all()])
            substrate = 'if(%s)' %substrate_formula
        else:   
            substrate = 1
        
        if 6 in input_params:
            depth_class_formula = ' || '.join(['depth_class==%s' % depth_class.id for depth_class in self.input_depth_class.all()])
            depth_class = 'if(%s)' %depth_class_formula
        else:   
            depth_class = 1
        
        if 7 in input_params:
            geomorphology_formula = ' || '.join(['geomorphology==%s' % geomorphology.id for geomorphology in self.input_geomorphology.all()])
            geomorphology = 'if(%s)' %geomorphology_formula
        else:   
            geomorphology = 1
        
        mapcalc = """r.mapcalc "rresult = if((%s + %s + %s + %s + %s + %s)==6,1,null())" """ % (port_buffer, shoreline_buffer, depth, substrate, depth_class, geomorphology)
        #mapcalc = """r.mapcalc "rresult = if((if(shoreline_rast_buffer==2) + if(port_buffer_rast) + if(bathy>%s && bathy<%s) + if(%s))==4,1,null())" """ % (self.input_min_depth, self.input_max_depth, substrate_formula) 
        g.run(mapcalc)
        self.output_mapcalc = mapcalc
        
        #substrate stats
        substrate_result = """r.mapcalc "subresult = if(rresult==1,substrate,null())" """
        g.run(substrate_result)
        #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
        substrate_stats = g.run('r.stats -an input=subresult')
        substrate_split = substrate_stats.split()
        #cast the area elements to integers (no need for the decimal value when dealing with meters)
        substrate_ints = [int(float(x)) for x in substrate_split]
        #note: we are now dealing with int areas rather than float strings 
        substrate_dict = dict(zip(substrate_ints[::2], substrate_ints[1::2])) 
        #use dumps to save and loads to extract
        self.output_substrate_stats = simplejson.dumps(substrate_dict)
        
        #depth class stats
        depth_class_result = """r.mapcalc "dcresult = if(rresult==1,depth_class,null())" """
        g.run(depth_class_result)
        depth_class_stats = g.run('r.stats -an input=dcresult')
        depth_class_split = depth_class_stats.split()
        #cast the area elements to integers (no need for the decimal value when dealing with meters)
        depth_class_ints = [int(float(x)) for x in depth_class_split]
        #generate dictionary result
        depth_class_dict = dict(zip(depth_class_ints[::2], depth_class_ints[1::2])) 
        #use dumps to save and loads to extract
        self.output_depth_class_stats = simplejson.dumps(depth_class_dict)
        
        #geomorphology stats
        geomorphology_result = """r.mapcalc "georesult = if(rresult==1,geomorphology,null())" """
        g.run(geomorphology_result)
        geomorphology_stats = g.run('r.stats -an input=georesult')
        geomorphology_split = geomorphology_stats.split()
        #cast the area elements to integers (no need for the decimal value when dealing with meters)
        geomorphology_ints = [int(float(x)) for x in geomorphology_split]
        #generate dictionary result
        geomorphology_dict = dict(zip(geomorphology_ints[::2], geomorphology_ints[1::2])) 
        #use dumps to save and loads to extract
        self.output_geomorphology_stats = simplejson.dumps(geomorphology_dict)
        
        g.run('r.to.vect input=rresult output=rresult_vect feature=area')

        g.run('v.out.ogr -c input=rresult_vect type=area format=GeoJSON dsn=%s' % output)

        from django.contrib.gis.gdal import DataSource
        from django.contrib.gis.geos import MultiPolygon
        try:
            ds = DataSource(output)
            layer = ds[0]
            geom = MultiPolygon([g.geos for g in layer.get_geoms()])
        except:
            # Grass had no geometries to give - empty output
            geom = MultiPolygon([])

        geom.srid = settings.GEOMETRY_DB_SRID
        self.output_geom = geom
        self.output_area = geom.area / 1000000.0 # sq m to sq km
        
        self.geometry_final = geom

        #cleanup
        os.remove(output)
        del g

        return True
        
    def save(self, rerun=None, *args, **kwargs):
        # only rerun the analysis if any of the input_ fields have changed
        # ie if name and description change no need to rerun the full analysis
        #if self.pk is None: #if new Scenario
        #    super(Scenario, self).save(rerun=True, *args, **kwargs)
        if rerun is None and self.pk is not None: #if editing a scenario and no value for rerun is given
            rerun = False
            outputs = Scenario.output_fields()
            for output in outputs:
                if getattr(self, output.name) is None:
                    rerun = True
                    break
            if not rerun:
                orig = Scenario.objects.get(pk=self.pk)
                for f in Scenario.input_fields():
                    # Is original value different from form value?
                    #if orig._get_FIELD_display(f) != getattr(self,f.name):
                    if getattr(orig, f.name) != getattr(self, f.name):
                        rerun = True
                        break                                                                                                                   
                if not rerun:
                    #the substrates need to be grabbed, then saved, then grabbed again because (regardless of whether we use orig or self) 
                    #both getattr calls return the same original list until the model has been saved 
                    #(I assume this means the form.save_m2m actually has to be called), after which calls to getattr 
                    #will return the same list (regardless of whether we use orig or self)
                    orig_substrates = set(getattr(orig, 'input_substrate').all())
                    orig_depth_classes = set(getattr(orig, 'input_depth_class').all())
                    orig_geomorphologies = set(getattr(orig, 'input_geomorphology').all())
                    super(Scenario, self).save(rerun=False, *args, **kwargs)
                    new_substrates = set(getattr(self, 'input_substrate').all())
                    new_depth_classes = set(getattr(self, 'input_depth_class').all())
                    new_geomorphologies = set(getattr(self, 'input_geomorphology').all())
                    if orig_substrates != new_substrates or orig_depth_classes != new_depth_classes or orig_geomorphologies != new_geomorphologies:
                        rerun = True                    
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)
        else: #editing a scenario and rerun is provided 
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name
        
    def support_filename(self):
        return os.path.basename(self.support_file.name)
        
    def needs_rerun(self, input_dict):
        rerun = False
        input_fields = Scenario.input_fields()
        for field in input_fields:
            try:
                if getattr(self, field.name) != input_dict[field.name]:
                    rerun = True
                    break
            except KeyError:
                print
                print 'KEYERROR in Scenario.needs_rerun'
                print '%s not found in needs_rerun.input_dict' %field.name
                print
                rerun = True
        return rerun
    
    @classmethod
    def mapnik_geomfield(self):
        return "output_geom"

    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#ffffff'))
        ps.fill_opacity = 0.5
        
        ls = mapnik.LineSymbolizer(mapnik.Color('#555555'),0.75)
        ls.stroke_opacity = 0.5
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        polygon_style.rules.append(r)
        return polygon_style   

    #@property
    #def input_substrate(self):
    #    return getattr(self, 'input_substrate_%s' %self.input_objective.short_name)
        
    #@property
    #def input_depth_class(self):
    #    return getattr(self, 'input_depth_class_%s' %self.input_objective.short_name)
        
    #@property
    #def input_geomorphology(self):
    #    return getattr(self, 'input_geomorphology_%s' %self.input_objective.short_name)
        
    #@property
    #def input_parameters(self):        
    #    return getattr(self, 'input_parameters_%s' %self.input_objective.short_name)

    @property
    def input_parameter_ids(self):
        #input_params = [p.parameter.id for p in self.input_parameters.all()]
        parameter_ids = [p.id for p in self.input_parameters.all()]
        return parameter_ids
        
    @property
    def input_parameter_names(self):
        parameter_names = [parameter.short_name for parameter in self.input_parameters.all()]
        return parameter_names
        
    @property
    def input_substrate_names(self):
        substrate_names = [substrate.name for substrate in self.input_substrate.all()]
        return substrate_names
    
    @property
    def input_depth_class_names(self):
        depth_class_names = [depth_class.name for depth_class in self.input_depth_class.all()]
        return depth_class_names
        
    @property
    def input_geomorphology_names(self):
        geomorphology_names = [geomorphology.name for geomorphology in self.input_geomorphology.all()]
        return geomorphology_names
        
    @property
    def get_id(self):
        return self.id
    
    @property
    def color(self):
        try:
            return Objective.objects.get(pk=self.input_objective.id).color
        except:
            return '778B1A55'
    
    @property
    def kml_param_output(self):
        return """
            <p>testing...</p>
        """
        
    @property 
    def kml_working(self):
        return """
        <Placemark id="%s">
            <visibility>0</visibility>
            <name>%s (WORKING)</name>
        </Placemark>
        """ % (self.uid, escape(self.name))

    @property 
    def kml_done(self):
        return """
        %s
        <Placemark id="%s">
            <visibility>1</visibility>
            <name>%s</name>
            <styleUrl>#%s-default</styleUrl>
            <ExtendedData>
                <Data name="name"><value>%s</value></Data>
                <Data name="user"><value>%s</value></Data>
                <Data name="desc"><value>%s</value></Data>
                <Data name="params"><value>%s</value></Data>
                <Data name="type"><value>%s</value></Data>
                <Data name="modified"><value>%s</value></Data>
            </ExtendedData>
            <MultiGeometry>
            %s
            </MultiGeometry>
        </Placemark>
        """ % (self.kml_style, self.uid, escape(self.name), self.model_uid(),
            escape(self.name), self.user, escape(self.description), self.kml_param_output, 
            self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
            asKml(self.output_geom.transform( settings.GEOMETRY_CLIENT_SRID, clone=True))
            )
        
    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752"><strong>$[name]</strong></font><br />
                    <p>$[desc]</p>
                    <font size=1>$[type] created by $[user] on $[modified]</font>
                ]]> </text>
            </BalloonStyle>
            <IconStyle>
                <color>ffffffff</color>
                <colorMode>normal</colorMode>
                <scale>0.9</scale> 
                <Icon> <href>http://maps.google.com/mapfiles/kml/paddle/wht-blank.png</href> </Icon>
            </IconStyle>
            <LabelStyle>
                <color>ffffffff</color>
                <scale>0.8</scale>
            </LabelStyle>
            <PolyStyle>
                <color>%s</color>
            </PolyStyle>
        </Style>
        """ % (self.model_uid(),self.color)
    
    class Options:
        verbose_name = 'Scenario'
        #ordering = ['id']
        form = 'scenario.forms.ScenarioForm'
        form_template = 'scenario/form.html'
        show_template = 'scenario/show.html'

class Category(models.Model):
    name = models.CharField(max_length=70)
    short_name = models.CharField(max_length=70)
    
    def __unicode__(self):
        return u'%s' %self.name
        
class Objective(models.Model):
    name = models.CharField(max_length=70)
    short_name = models.CharField(max_length=70)
    color = models.CharField(max_length=8, default='778B1A55')
    
    def __unicode__(self):
        return u'%s' % self.name   

class EnergyObjective(models.Model):
    objective = models.ForeignKey("Objective", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.objective.name

class ConservationObjective(models.Model):
    objective = models.ForeignKey("Objective", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.objective.name

class FisheriesObjective(models.Model):
    objective = models.ForeignKey("Objective", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.objective.name

class DevelopmentObjective(models.Model):
    objective = models.ForeignKey("Objective", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.objective.name

class Parameter(models.Model):
    name = models.CharField(max_length=70)
    short_name = models.CharField(max_length=70)
    
    def __unicode__(self):
        return u'%s' % self.name
        
class TidalEnergyParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class WindEnergyParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class WaveEnergyParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class OffshoreConservationParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class NearshoreConservationParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class WaterColumnConservationParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class ShoresideDevelopmentParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class ShellfishAquacultureParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class OffshoreFishingParameter(models.Model):
    parameter = models.ForeignKey("Parameter", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.parameter.name
        
class Substrate(models.Model):
    name = models.CharField(max_length=30)  

    def __unicode__(self):
        return u'%s' % self.name
        
class DepthClass(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % self.name        

class Geomorphology(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % self.name        

@register
class ConservationSite(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    
    @property
    def kml(self):
        return """
        <Placemark id="%s">
            <visibility>1</visibility>
            <name>%s</name>
            <styleUrl>#%s-default</styleUrl>
            <ExtendedData>
                <Data name="name"><value>%s</value></Data>
                <Data name="user"><value>%s</value></Data>
                <Data name="desc"><value>%s</value></Data>
                <Data name="type"><value>%s</value></Data>
                <Data name="modified"><value>%s</value></Data>
            </ExtendedData>
            %s 
        </Placemark>
        """ % (self.uid, escape(self.name), self.model_uid(), 
               escape(self.name), self.user, escape(self.description), self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
               self.geom_kml)

    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752"><strong>$[name]</strong></font><br />
                    <p>$[desc]</p>
                    <font size=1>$[type] created by $[user] on $[modified]</font>
                ]]> </text>
            </BalloonStyle>
            <PolyStyle>
                <color>%s</color>
            </PolyStyle>
            <LineStyle>
                <color>ffffffff</color>
            </LineStyle>
        </Style>
        """ % (self.model_uid(), self.color())

    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#DC640C'))
        ps.fill_opacity = 0.6
        ls = mapnik.LineSymbolizer(mapnik.Color('#ff0000'),0.2)
        ls.stroke_opacity = 1.0
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        
        polygon_style.rules.append(r)
        return polygon_style     

    @classmethod
    def color(self):
        try:
            return Objective.objects.get(id=3).color
        except:
            return '778B1A55'

    class Options:
        verbose_name = 'Conservation Site'
        form = 'scenario.forms.ConservationSiteForm'
        form_template = 'conservation/form.html'
        show_template = 'conservation/show.html'
        icon_url = 'wmm/img/conservation.png'

@register
class WindEnergySite(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    
    @property
    def kml(self):
        return """
        <Placemark id="%s">
            <visibility>1</visibility>
            <name>%s</name>
            <styleUrl>#%s-default</styleUrl>
            <ExtendedData>
                <Data name="name"><value>%s</value></Data>
                <Data name="user"><value>%s</value></Data>
                <Data name="desc"><value>%s</value></Data>
                <Data name="type"><value>%s</value></Data>
                <Data name="modified"><value>%s</value></Data>
            </ExtendedData>
            %s 
        </Placemark>
        """ % (self.uid, escape(self.name), self.model_uid(), 
               escape(self.name), self.user, escape(self.description), self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
               self.geom_kml)

    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752"><strong>$[name]</strong></font><br />
                    <p>$[desc]</p>
                    <font size=1>$[type] created by $[user] on $[modified]</font>
                ]]> </text>
            </BalloonStyle>
            <PolyStyle>
                <color>%s</color>
            </PolyStyle>
            <LineStyle>
                <color>ffffffff</color>
            </LineStyle>
        </Style>
        """ % (self.model_uid(), self.color())

    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#DC640C'))
        ps.fill_opacity = 0.6
        ls = mapnik.LineSymbolizer(mapnik.Color('#ff0000'),0.2)
        ls.stroke_opacity = 1.0
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        
        polygon_style.rules.append(r)
        return polygon_style        

    @classmethod
    def color(self):
        try:
            return Objective.objects.get(id=2).color
        except:
            return '778B1A55'             

    class Options:
        verbose_name = 'Wind Energy Site'
        form = 'scenario.forms.WindEnergySiteForm'
        form_template = 'wind/form.html'
        show_template = 'wind/show.html'
        icon_url = 'wmm/img/wind.png'


@register
class AOI(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    
    @property
    def kml(self):
        return """
        <Placemark id="%s">
            <visibility>1</visibility>
            <name>%s</name>
            <styleUrl>#%s-default</styleUrl>
            <ExtendedData>
                <Data name="name"><value>%s</value></Data>
                <Data name="user"><value>%s</value></Data>
                <Data name="desc"><value>%s</value></Data>
                <Data name="modified"><value>%s</value></Data>
            </ExtendedData>
            %s 
        </Placemark>
        """ % (self.uid, escape(self.name), self.model_uid(), 
               escape(self.name), self.user, escape(self.description), self.date_modified.replace(microsecond=0), 
               self.geom_kml)

    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752"><strong>$[name]</strong></font><br />
                    <p>$[desc]</p>
                    <font size=1>Created by $[user] on $[modified]</font>
                ]]> </text>
            </BalloonStyle>
            <PolyStyle>
                <color>%s</color>
            </PolyStyle>
            <LineStyle>
                <color>ffffffff</color>
            </LineStyle>
        </Style>
        """ % (self.model_uid(), self.color())        
    
    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#DC640C'))
        ps.fill_opacity = 0.6
        ls = mapnik.LineSymbolizer(mapnik.Color('#ff0000'),0.2)
        ls.stroke_opacity = 1.0
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        
        polygon_style.rules.append(r)
        return polygon_style       

    @classmethod
    def color(self):
        return '778B1A55'              

    class Options:
        verbose_name = 'Area of Interest'
        form = 'scenario.forms.AoiForm'
        form_template = 'aoi/form.html'
        show_template = 'aoi/show.html'
        icon_url = 'wmm/img/aoi.png'
                

@register
class POI(PointFeature):
    description = models.TextField(null=True,blank=True)
    
    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#DC640C'))
        ps.fill_opacity = 0.6
        ls = mapnik.LineSymbolizer(mapnik.Color('#ff0000'),0.2)
        ls.stroke_opacity = 1.0
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        
        polygon_style.rules.append(r)
        return polygon_style                

    class Options:
        verbose_name = 'Point of Interest'
        form = 'scenario.forms.PoiForm'
        icon_url = 'wmm/img/poi.png'

@register
class LOI(LineFeature):
    description = models.TextField(null=True,blank=True)
    
    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#DC640C'))
        ps.fill_opacity = 0.6
        ls = mapnik.LineSymbolizer(mapnik.Color('#ff0000'),0.2)
        ls.stroke_opacity = 1.0
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        
        polygon_style.rules.append(r)
        return polygon_style                

    class Options:
        verbose_name = 'Line of Interest'
        form = 'scenario.forms.LoiForm'
        icon_url = 'wmm/img/loi.png'

@register
class UserKml(PrivateLayerList):
    class Options:
        verbose_name = 'Uploaded KML'
        form = 'scenario.forms.UserKmlForm'
        icon_url = 'media/common/images/kml_document_icon.png'
