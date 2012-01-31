import time
import os
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from django.utils import simplejson
from lingcod.analysistools.models import Analysis
from lingcod.features import register, alternate
from lingcod.common.utils import asKml
from lingcod.features.models import Feature, PointFeature, LineFeature, PolygonFeature, FeatureCollection
from lingcod.layers.models import PrivateLayerList
from utils import miles_to_meters, feet_to_meters, intcomma


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
                           'smp.models.SMPSite',
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
    # Tidal
    input_parameters_tidal_energy = models.ManyToManyField("TidalEnergyParameter", null=True, blank=True)
    input_dist_shore_tidal_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_tidal_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_tidal_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_tidal_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_tidal_energy = models.ManyToManyField("Substrate", related_name="MOSTidalEnergySubstrate", null=True, blank=True)
    input_min_tidalmean_tidal_energy = models.FloatField(verbose_name='Minimum TidalMax', null=True, blank=True)
    input_max_tidalmean_tidal_energy = models.FloatField(verbose_name='Maximum TidalMax', null=True, blank=True)
    input_min_tidalmax_tidal_energy = models.FloatField(verbose_name='Minimum TidalMax', null=True, blank=True)
    input_max_tidalmax_tidal_energy = models.FloatField(verbose_name='Maximum TidalMax', null=True, blank=True)
    # Wind
    input_parameters_wind_energy = models.ManyToManyField("WindEnergyParameter")
    input_dist_shore_wind_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_wind_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_wind_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_wind_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_wind_energy = models.ManyToManyField("Substrate", related_name="MOSWindEnergySubstrate", null=True, blank=True)
    input_wind_potential_wind_energy = models.ManyToManyField("WindPotential", null=True, blank=True)
    # Wave
    input_parameters_wave_energy = models.ManyToManyField("WaveEnergyParameter")
    input_dist_shore_wave_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_wave_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_wave_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_wave_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_wave_energy = models.ManyToManyField("Substrate", related_name="MOSWaveEnergySubstrate", null=True, blank=True)
    input_min_wavesummer_wave_energy = models.FloatField(verbose_name='Minimum Wave-Summer', null=True, blank=True)
    input_max_wavesummer_wave_energy = models.FloatField(verbose_name='Maximum Wave-Summer', null=True, blank=True)
    input_min_wavewinter_wave_energy = models.FloatField(verbose_name='Minimum Wave-Winter', null=True, blank=True)
    input_max_wavewinter_wave_energy = models.FloatField(verbose_name='Maximum Wave-Winter', null=True, blank=True)
    
    # Conservation Parameters
    input_objectives_conservation = models.ManyToManyField("ConservationObjective", null=True, blank=True)
    # Offshore 
    input_parameters_offshore_conservation = models.ManyToManyField("OffshoreConservationParameter")
    input_substrate_offshore_conservation = models.ManyToManyField("Substrate", related_name="MOSOffshoreConservationSubstrate", null=True, blank=True)
    input_depth_class_offshore_conservation = models.ManyToManyField("DepthClass", related_name="MOSOffshoreConservationDepthClass", null=True, blank=True)    
    input_geomorphology_offshore_conservation = models.ManyToManyField("Geomorphology", related_name="MOSOffshoreConservationGeomorphology", null=True, blank=True)
    # Nearshore
    input_parameters_nearshore_conservation = models.ManyToManyField("NearshoreConservationParameter")
    input_substrate_nearshore_conservation = models.ManyToManyField("NearshoreSubstrate", null=True, blank=True)
    input_exposure_nearshore_conservation = models.ManyToManyField("NearshoreExposure", null=True, blank=True)
    input_ecosystem_nearshore_conservation = models.ManyToManyField("NearshoreEcosystem", null=True, blank=True)
    # Water Column
    input_parameters_water_column_conservation = models.ManyToManyField("WaterColumnConservationParameter")
    input_upwelling_water_column_conservation = models.ManyToManyField("Upwelling", null=True, blank=True)
    input_chlorophyl_water_column_conservation = models.ManyToManyField("Chlorophyl", null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)
    support_file = models.FileField(upload_to='scenarios/files/', null=True, blank=True)
    
    overlap_geom = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Scenario Area of Overlap")
       
    
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
            #accumulate energy_objectives
            [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_energy']]
            #accumulate conservation_objectives
            [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_conservation']]
            #development_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_development']]
            #fisheries_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_fisheries']]
            
            #run analysis on scenarios only when necessary
            for obj in self.input_objectives.all():
                rerun = None
                obj_short_name = obj.short_name
                #note:  this is not the name provided in the kml.  this name is purely for referential purposes
                scenario_name = self.name + '_%s' % obj_short_name
                
                params = form_data['input_parameters_%s'%obj_short_name]
                input_params = [param.parameter for param in params]
                
                #while these are already in the MOS fields, the following keeps the code re-usable for all objectives
                dist_shore = self.get_form_data(form_data, 'input_dist_shore_%s'%obj_short_name)
                dist_port = self.get_form_data(form_data, 'input_dist_port_%s'%obj_short_name)
                min_depth = self.get_form_data(form_data, 'input_min_depth_%s'%obj_short_name)
                max_depth = self.get_form_data(form_data, 'input_max_depth_%s'%obj_short_name)
                substrates = self.get_form_data(form_data, 'input_substrate_%s'%obj_short_name)
                exposures = self.get_form_data(form_data, 'input_exposure_%s'%obj_short_name)
                ecosystems = self.get_form_data(form_data, 'input_ecosystem_%s'%obj_short_name)
                wind_potentials = self.get_form_data(form_data, 'input_wind_potential_%s'%obj_short_name)
                min_tidalmean = self.get_form_data(form_data, 'input_min_tidalmean_%s'%obj_short_name)
                max_tidalmean = self.get_form_data(form_data, 'input_max_tidalmean_%s'%obj_short_name)
                min_tidalmax = self.get_form_data(form_data, 'input_min_tidalmax_%s'%obj_short_name)
                max_tidalmax = self.get_form_data(form_data, 'input_max_tidalmax_%s'%obj_short_name)
                min_wavesummer = self.get_form_data(form_data, 'input_min_wavesummer_%s'%obj_short_name)
                max_wavesummer = self.get_form_data(form_data, 'input_max_wavesummer_%s'%obj_short_name)
                min_wavewinter = self.get_form_data(form_data, 'input_min_wavewinter_%s'%obj_short_name)
                max_wavewinter = self.get_form_data(form_data, 'input_max_wavewinter_%s'%obj_short_name)
                depth_classes = self.get_form_data(form_data, 'input_depth_class_%s'%obj_short_name)
                geomorphologies = self.get_form_data(form_data, 'input_geomorphology_%s'%obj_short_name)
                upwellings = self.get_form_data(form_data, 'input_upwelling_%s'%obj_short_name)
                chlorophyls = self.get_form_data(form_data, 'input_chlorophyl_%s'%obj_short_name)
                
                scenarios = self.scenarios.filter(mos=self.id, input_objective=obj)
                if len(scenarios) > 1: #not expecting this case to ever happen -- might want to log this event if it does...
                    for scenario in scenarios:
                        self.scenarios.remove(scenario) 
                        scenario.delete()
                    scenarios = []
                if len(scenarios) == 1:
                    scenario = scenarios[0]  
                    scenario_dict = {'user': user, 'name': scenario_name, 'input_parameters': input_params, 'input_objective': obj, 'input_dist_shore': dist_shore, 'input_dist_port': dist_port, 'input_min_depth': min_depth, 'input_max_depth': max_depth, 'input_min_tidalmean': min_tidalmean, 'input_max_tidalmean': max_tidalmean, 'input_min_tidalmax': min_tidalmax, 'input_max_tidalmax': max_tidalmax, 'input_min_wavesummer': min_wavesummer, 'input_max_wavesummer': max_wavesummer, 'input_min_wavewinter': min_wavewinter, 'input_max_wavewinter': max_wavewinter}
                    if scenario.needs_rerun(scenario_dict):
                        rerun = True
                    scenario.__dict__.update(scenario_dict)
                else:
                    scenario = Scenario(user=user, name=scenario_name, input_objective=obj, input_dist_shore=dist_shore, input_dist_port = dist_port, input_min_depth=min_depth, input_max_depth=max_depth, input_min_tidalmean=min_tidalmean, input_max_tidalmean=max_tidalmean, input_min_tidalmax=min_tidalmax, input_max_tidalmax=max_tidalmax, input_min_wavesummer=min_wavesummer, input_max_wavesummer=max_wavesummer, input_min_wavewinter=min_wavewinter, input_max_wavewinter=max_wavewinter)            
                scenario.save(rerun=False)
                
                if set(scenario.input_parameters.all()) != set(input_params) or set(scenario.input_wind_potential.all()) != set(wind_potentials) or (set(scenario.input_substrate.all()) != set(substrates) and set(scenario.input_nearshore_substrate.all()) != set(substrates)) or set(scenario.input_nearshore_exposure.all()) != set(exposures) or set(scenario.input_nearshore_ecosystem.all()) != set(ecosystems) or set(scenario.input_depth_class.all()) != set(depth_classes) or set(scenario.input_geomorphology.all()) != set(geomorphologies):
                    rerun = True   
                scenario.input_parameters = input_params 
                if obj_short_name == 'nearshore_conservation':
                    scenario.input_nearshore_substrate = substrates
                else:
                    scenario.input_substrate = substrates                  
                scenario.input_nearshore_ecosystem = ecosystems                   
                scenario.input_nearshore_exposure = exposures                     
                scenario.input_depth_class = depth_classes                    
                scenario.input_wind_potential = wind_potentials                    
                scenario.input_geomorphology = geomorphologies             
                scenario.input_upwelling = upwellings             
                scenario.input_chlorophyl = chlorophyls
                
                scenario.save(rerun=rerun)
                self.scenarios.add(scenario)
        
        #remove any unwanted scenarios
        objs = self.input_objectives.all()
        scenarios = self.scenarios.exclude(input_objective__in=objs)
        scenarios.delete()
        
        #generate overlapping geometry
        scenario_geoms = [s.geometry_final for s in self.scenarios.all()]
        scenario_areas = [s.area for s in scenario_geoms]
        self.overlap_geom = None
        if len(scenario_geoms) > 1:
            overlap = scenario_geoms[0].buffer(0)
            for geom in scenario_geoms[1:]:
                overlap = overlap.intersection(geom).buffer(0)
            if not overlap.empty:
                self.overlap_geom = overlap
        
        #TODO:  why are we running analysis twice when creating scenarios initially? -- is this still happening...?
        super(MOS, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name
        
    def support_filename(self):
        return os.path.basename(self.support_file.name)
    
    def get_form_data(self, form_data, index):
        try:
            data = form_data[index]
        except:
            if 'dist_shore' in index or 'dist_port' in index or 'min_depth' in index or 'max_depth' in index or 'min_tidalmean' in index or 'max_tidalmean' in index or 'min_tidalmax' in index or 'max_tidalmax' in index or 'min_wavesummer' in index or 'max_wavesummer' in index or 'min_wavewinter' in index or 'max_wavewinter' in index:
                data = 0
            else:
                data = []
        return data            
    
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
            html += '<p><strong> Substrates:</strong>  '
            html += ", ".join(scenario.input_substrate_names)
            html += " </p>"
            #html += "<ul>"
            #for substrate in scenario.input_substrate_names:
            #    html += "<li>%s</li>" %substrate
            #html += "</ul></p>"
        if 6 in parameter_ids:
            html += "<p><strong> Depth Classes:</strong>  "
            html += ", ".join(scenario.input_depth_class_names)
            html += " </p>"
        if 7 in parameter_ids:
            html += "<p><strong> Geomorphologies:</strong>  "
            html += ", ".join(scenario.input_geomorphology_names)
            html += " </p>"
        if 8 in parameter_ids:
            html += "<p><strong> Exposures:</strong>  "
            html += ", ".join(scenario.input_exposure_names)
            html += " </p>"
        if 9 in parameter_ids:
            html += "<p><strong> Ecosystems:</strong>  "
            html += ", ".join(scenario.input_ecosystem_names)
            html += " </p>"
        if 10 in parameter_ids:
            html += "<p><strong> Upwelling:</strong>  "
            html += ", ".join(scenario.input_upwelling_names)
            html += " </p>"
        if 11 in parameter_ids:
            html += "<p><strong> Chlorophyl:</strong>  "
            html += ", ".join(scenario.input_chlorophyl_names)
            html += " </p>"
        if 12 in parameter_ids:
            html += "<p><strong> Wind Potential:</strong>  "
            html += ", ".join(scenario.input_wind_potential_names)
            html += " </p>"
        if 13 in parameter_ids:
            html += "<p><strong> Mean Tidal Energy:</strong> %s to %s W/m2</p>" % (intcomma(int(scenario.input_min_tidalmean)), intcomma(int(scenario.input_max_tidalmean)))
        if 14 in parameter_ids:
            html += "<p><strong> Max Tidal Energy:</strong> %s to %s W/m2</p>" % (intcomma(int(scenario.input_min_tidalmax)), intcomma(int(scenario.input_max_tidalmax)))
        if 15 in parameter_ids:
            html += "<p><strong> Summer Wave Energy:</strong> %s to %s kW/m of shoreline</p>" % (intcomma(int(scenario.input_min_wavesummer)), intcomma(int(scenario.input_max_wavesummer)))
        if 16 in parameter_ids:
            html += "<p><strong> Winter Wave Energy:</strong> %s to %s kW/m of shoreline</p>" % (intcomma(int(scenario.input_min_wavewinter)), intcomma(int(scenario.input_max_wavewinter)))
        return html 
        
    @property 
    def kml(self):        
        combined_kml = '<Folder id="%s"><name>%s</name><visibility>0</visibility><open>0</open>' %(self.uid, self.name)
        #mos_name = escape(self.name)
        #print 'mos_name = %s' %mos_name
        for scenario in self.scenarios.all():
            header = '<strong>Scenario:</strong> %s' %self.name
            obj_name = scenario.input_objective.name
            objective = '<strong>Objective:</strong> %s' %obj_name
            #name = scenario.mos_set.all()[0].name #why is this not working...?
            kml =   """
                    %s
                    <Placemark>
                        <visibility>1</visibility>
                        <name>%s</name>
                        <styleUrl>#%s-default</styleUrl>
                        <ExtendedData>
                            <Data name="header"><value>%s</value></Data>
                            <Data name="objective"><value>%s</value></Data>
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
                    """ % ( self.scenario_style(scenario.color), obj_name, self.model_uid(),
                            header, objective, self.user, escape(self.description_html), escape(self.parameter_html(scenario)),
                            self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
                            asKml(scenario.output_geom.transform( settings.GEOMETRY_CLIENT_SRID, clone=True)) )
            combined_kml += kml
        if self.overlap_geom is not None:
            combined_kml += self.overlap_kml
        combined_kml += "</Folder>"
        return combined_kml
        
    @property
    def overlap_kml(self):
        header = '<strong>Area of Overlap</strong>'
        color = '501478B4'
        obj_name = 'Area of Overlap'
        objective = ''
        description = ''
        #name = scenario.mos_set.all()[0].name #why is this not working...?
        kml =   """
                %s
                <Placemark>
                    <visibility>1</visibility>
                    <name>%s</name>
                    <styleUrl>#%s-default</styleUrl>
                    <ExtendedData>
                        <Data name="header"><value>%s</value></Data>
                        <Data name="objective"><value>%s</value></Data>
                        <Data name="user"><value>%s</value></Data>
                        <Data name="desc"><value>%s</value></Data>
                        <Data name="params"><value>%s</value></Data>
                        <Data name="modified"><value>%s</value></Data>
                    </ExtendedData>
                    <MultiGeometry>
                    %s
                    </MultiGeometry>
                </Placemark>
                """ % ( color, obj_name, self.model_uid(),
                        header, objective, self.user, escape(self.description_html), description,
                        self.date_modified.replace(microsecond=0), 
                        asKml(self.overlap_geom.transform( settings.GEOMETRY_CLIENT_SRID, clone=True)) )
        return kml

    def scenario_style(self, color='778B1A55'):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752">
                    <p>$[header]</p>
                    $[desc]
                    <p>$[objective]</p> 
                    <p>$[params]</p>
                    <p>
                    </font>                    
                    <font size=1>created by $[user] on $[modified]</font>
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
        verbose_name = 'Scenario'
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
    
    input_wind_potential = models.ManyToManyField("WindPotential", null=True, blank=True)  
    input_min_tidalmean = models.FloatField(verbose_name='Minimum TidalMax', null=True, blank=True)
    input_max_tidalmean = models.FloatField(verbose_name='Maximum TidalMax', null=True, blank=True)
    input_min_tidalmax = models.FloatField(verbose_name='Minimum TidalMax', null=True, blank=True)
    input_max_tidalmax = models.FloatField(verbose_name='Maximum TidalMax', null=True, blank=True)
    input_min_wavesummer = models.FloatField(verbose_name='Minimum Wave-Summer', null=True, blank=True)
    input_max_wavesummer = models.FloatField(verbose_name='Maximum Wave-Summer', null=True, blank=True)
    input_min_wavewinter = models.FloatField(verbose_name='Minimum Wave-Winter', null=True, blank=True)
    input_max_wavewinter = models.FloatField(verbose_name='Maximum Wave-Winter', null=True, blank=True)
    
    input_substrate = models.ManyToManyField("Substrate", null=True, blank=True)  
    input_depth_class = models.ManyToManyField("DepthClass", null=True, blank=True)    
    input_geomorphology = models.ManyToManyField("Geomorphology", null=True, blank=True)
    
    input_nearshore_substrate = models.ManyToManyField("NearshoreSubstrate", null=True, blank=True)
    input_nearshore_exposure = models.ManyToManyField("NearshoreExposure", null=True, blank=True)
    input_nearshore_ecosystem = models.ManyToManyField("NearshoreEcosystem", null=True, blank=True)
    
    input_upwelling = models.ManyToManyField("Upwelling", null=True, blank=True)
    input_chlorophyl = models.ManyToManyField("Chlorophyl", null=True, blank=True)
    
    # All output fields should be allowed to be Null/Blank
    output_geom = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Scenario Geometry")
    output_mapcalc = models.CharField(max_length=720, null=True, blank=True)
    output_area = models.FloatField(verbose_name="Total Area (sq km)", null=True, blank=True)
    
    #TODO will want to replace individual output stats field with a single field (as output stats will differ based on objective)
    #output_stats = models.TextField(null=True, blank=True) 
    #output_substrate_stats = models.TextField(max_length=360, null=True, blank=True)
    #output_depth_class_stats = models.TextField(max_length=360, null=True, blank=True)
    #output_geomorphology_stats = models.TextField(max_length=360, null=True, blank=True)
    
    #output_substrate_depth_class_stats = models.TextField(max_length=360, null=True, blank=True)
    #output_substrate_geomorphology_stats = models.TextField(max_length=360, null=True, blank=True)
    
    output_report = models.TextField(null=True, blank=True)
    
    #output_depth_class_substrate_stats = models.TextField(max_length=360, null=True, blank=True)
    #output_depth_class_geomorphology_stats = models.TextField(max_length=360, null=True, blank=True)
    #output_geomorphology_substrate_stats = models.TextField(max_length=360, null=True, blank=True)
    #output_geomorphology_depth_class_stats = models.TextField(max_length=360, null=True, blank=True)
    
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
        if self.input_objective.short_name == 'nearshore_conservation':
            g.run('g.region nsres=90 ewres=90')  #sets cell size
        else:
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
            if self.input_objective.short_name == 'nearshore_conservation':
                substrate_formula = ' || '.join(['nearshore_substrate==%s' % substrate.id for substrate in self.input_nearshore_substrate.all()])
            else:
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
        
        if 8 in input_params:
            exposure_formula = ' || '.join(['exposure==%s' % exposure.id for exposure in self.input_nearshore_exposure.all()])
            exposure = 'if(%s)' %exposure_formula
        else:   
            exposure = 1
        
        if 9 in input_params:
            ecosystem_formula = ' || '.join(['vegetation==%s' % ecosystem.id for ecosystem in self.input_nearshore_ecosystem.all()])
            ecosystem = 'if(%s)' %ecosystem_formula
        else:   
            ecosystem = 1
        
        if 10 in input_params:
            upwelling_formula = ' || '.join(['upwelling==%s' % upwelling.id for upwelling in self.input_upwelling.all()])
            upwelling = 'if(%s)' %upwelling_formula
        else:   
            upwelling = 1
        
        if 11 in input_params:
            chlorophyl_formula = ' || '.join(['chlorophyll==%s' % chlorophyl.id for chlorophyl in self.input_chlorophyl.all()])
            chlorophyl = 'if(%s)' %chlorophyl_formula
        else:   
            chlorophyl = 1
        
        if 12 in input_params:
            wind_formula = ' || '.join(['wind==%s' % wind.id for wind in self.input_wind_potential.all()])
            wind = 'if(%s)' %wind_formula
        else:   
            wind = 1
        
        if 13 in input_params:
            tidalmean = 'if(tidal_mean >= %s && tidal_mean <= %s)' % (self.input_min_tidalmean, self.input_max_tidalmean)
        else:
            tidalmean = 1
        
        if 14 in input_params:
            tidalmax = 'if(tidal_max >= %s && tidal_max <= %s)' % (self.input_min_tidalmax, self.input_max_tidalmax)
        else:
            tidalmax = 1
        
        if 15 in input_params:
            wavesummer = 'if(wave_summer >= %s && wave_summer <= %s)' % (self.input_min_wavesummer, self.input_max_wavesummer)
        else:
            wavesummer = 1
        
        if 16 in input_params:
            wavewinter = 'if(wave_winter >= %s && wave_winter <= %s)' % (self.input_min_wavewinter, self.input_max_wavewinter)
        else:
            wavewinter = 1
        
        mapcalc = """r.mapcalc "rresult = if((%s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s)==15,1,null())" """ % (port_buffer, shoreline_buffer, depth, substrate, depth_class, geomorphology, exposure, ecosystem, upwelling, chlorophyl, wind, tidalmean, tidalmax, wavesummer, wavewinter)
        #mapcalc = """r.mapcalc "rresult = if((if(shoreline_rast_buffer==2) + if(port_buffer_rast) + if(bathy>%s && bathy<%s) + if(%s))==4,1,null())" """ % (self.input_min_depth, self.input_max_depth, substrate_formula) 
        g.run(mapcalc)
        self.output_mapcalc = mapcalc
        
        if self.input_objective.short_name == 'offshore_conservation':
            self.output_report = offshore_conservation_report(g)
        elif self.input_objective.short_name == 'wind_energy':
            self.output_report = wind_energy_report(g)
        else:
            self.output_report = simplejson.dumps({})
        
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
        self.output_area = geom.area # sq m 
        
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
                    orig_nearshore_substrates = set(getattr(orig, 'input_nearshore_substrate').all())
                    orig_nearshore_exposures = set(getattr(orig, 'input_nearshore_exposure').all())
                    orig_nearshore_ecosystems = set(getattr(orig, 'input_nearshore_ecosystem').all())
                    orig_depth_classes = set(getattr(orig, 'input_depth_class').all())
                    orig_geomorphologies = set(getattr(orig, 'input_geomorphology').all())
                    orig_upwellings = set(getattr(orig, 'input_upwelling').all())
                    orig_chlorophyls = set(getattr(orig, 'input_chlorophyl').all())
                    super(Scenario, self).save(rerun=False, *args, **kwargs)
                    new_substrates = set(getattr(self, 'input_substrate').all())
                    new_nearshore_substrates = set(getattr(self, 'input_nearshore_substrate').all())
                    new_nearshore_exposures = set(getattr(self, 'input_nearshore_exposure').all())
                    new_nearshore_ecosystems = set(getattr(self, 'input_nearshore_ecosystem').all())
                    new_depth_classes = set(getattr(self, 'input_depth_class').all())
                    new_geomorphologies = set(getattr(self, 'input_geomorphology').all())
                    new_upwellings = set(getattr(self, 'input_upwelling').all())
                    new_chlorophyls = set(getattr(self, 'input_chlorophyl').all())
                    if orig_substrates != new_substrates or orig_nearshore_substrates != new_nearshore_substrates or orig_nearshore_exposures != new_nearshore_exposures or orig_nearshore_ecosystems != new_nearshore_ecosystems or orig_depth_classes != new_depth_classes or orig_geomorphologies != new_geomorphologies or orig_upwellings != new_upwellings or orig_chlorophyls != new_chlorophyls:
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
    
    def wind_energy_report(self, g):
        wind_report = {}
        
        # Scenario 
        
        #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
        substrate_result = """r.mapcalc "subresult = if(rresult==1,substrate,null())" """
        g.run(substrate_result)
        #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
        substrate_name_dict, substrate_dict = self.get_dict_from_stats(g, Substrate, 'subresult')
        wind_report['substrate'] = substrate_name_dict
                
        #wind stats -- collecting area (in meters) for each wind energy class represented in the resulting scenario
        wind_result = """r.mapcalc "windresult = if(rresult==1,wind,null())" """
        g.run(wind_result)
        #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
        wind_name_dict, wind_dict = self.get_dict_from_stats(g, WindPotential, 'windresult')
        wind_report['wind_potential'] = wind_name_dict
        
        # Substrate -- Drilling Down
        
        #substrate depth_class stats -- collecting area (in meters) of each depth class in each substrate 
        sub_ids = substrate_dict.keys()
        substrate_wind_dict = {}
        for sub_id in sub_ids:
            #generate substrate raster
            sub_raster = 'subresult_%s' %sub_id
            substrate_result = """r.mapcalc "%s = if(substrate==%s,subresult,null())" """ % (sub_raster, sub_id)
            g.run(substrate_result)
            #generate wind class results for current substrate
            sub_wind_raster = 'substrate_%s_windresult' %sub_id
            wind_result = """r.mapcalc "%s = if(%s==%s,wind,null())" """ %(sub_wind_raster, sub_raster, sub_id)
            g.run(wind_result)
            wind_name_dict, wind_dict = self.get_dict_from_stats(g, WindPotential, sub_wind_raster)
            #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
            substrate_wind_dict[Substrate.objects.get(id=sub_id).short_name] = wind_name_dict
        wind_report['substrate_wind_potential'] = substrate_wind_dict
        
        # Wind Potential -- Drilling Down
        
        #wind potential substrate stats -- collecting area (in meters) of each substrate in each wind class 
        wind_report['wind_potential_substrate']=self.transpose_nested_dict(substrate_wind_dict)

        return simplejson.dumps(wind_report)
    
    
    #TODO: much of the following can be factored out into helper methods...
    def offshore_conservation_report(g):
        offshore_report = {}
        
        # Scenario 
        
        #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
        substrate_result = """r.mapcalc "subresult = if(rresult==1,substrate,null())" """
        g.run(substrate_result)
        #generate dictionary from stats
        substrate_name_dict, substrate_dict = get_dict_from_stats(g, Substrate, 'subresult')
        offshore_report['substrate']=substrate_name_dict
        
        #depth class stats
        depth_class_result = """r.mapcalc "dcresult = if(rresult==1,depth_class,null())" """
        g.run(depth_class_result)
        #generate dictionary from stats
        depth_class_name_dict, depth_class_dict = get_dict_from_stats(g, DepthClass, 'dcresult')
        offshore_report['depth_class']=depth_class_name_dict
        
        #geomorphology stats
        geomorphology_result = """r.mapcalc "georesult = if(rresult==1,geomorphology,null())" """
        g.run(geomorphology_result)
        #generate dictionary from stats
        geomorphology_name_dict, geomorphology_dict = get_dict_from_stats(g, Geomorphology, 'georesult')
        offshore_report['geomorphology']=geomorphology_name_dict
        
        # Substrate -- Drilling Down
        
        #substrate depth_class stats -- collecting area (in meters) of each depth class in each substrate 
        sub_ids = substrate_dict.keys()
        substrate_dc_dict = {}
        for sub_id in sub_ids:
            #generate substrate raster
            sub_raster = 'subresult_%s' %sub_id
            substrate_result = """r.mapcalc "%s = if(substrate==%s,subresult,null())" """ % (sub_raster, sub_id)
            g.run(substrate_result)
            #generate depthclass results for current substrate
            sub_dc_raster = 'substrate_%s_dcresult' %sub_id
            dc_result = """r.mapcalc "%s = if(%s==%s,depth_class,null())" """ %(sub_dc_raster, sub_raster, sub_id)
            g.run(dc_result)
            #generate dictionary from stats
            dc_name_dict, dc_dict = get_dict_from_stats(g, DepthClass, sub_dc_raster)
            #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
            substrate_dc_dict[Substrate.objects.get(id=sub_id).short_name] = dc_name_dict
        offshore_report['substrate_depth_class']=substrate_dc_dict
        
        #substrate geomorphology stats -- collecting area (in meters) of each geomorphology in each substrate 
        substrate_geo_dict = {}
        for sub_id in sub_ids:
            #generate geomorphology results for current substrate
            sub_raster = 'subresult_%s' %sub_id
            sub_geo_raster = 'substrate_%s_georesult' %sub_id
            geo_result = """r.mapcalc "%s = if(%s==%s,geomorphology,null())" """ %(sub_geo_raster, sub_raster, sub_id)
            g.run(geo_result)
            #generate dictionary from stats
            geo_name_dict, geo_dict = get_dict_from_stats(g, Geomorphology, sub_geo_raster)
            #the following key uses Substrate.short_name to prevent html iregularities when assigning div names in report template
            substrate_geo_dict[Substrate.objects.get(id=sub_id).short_name] = geo_name_dict
        offshore_report['substrate_geomorphology']=substrate_geo_dict
        
        # Depth Class -- Drilling Down
        
        #depth class geomorphology stats -- collecting area (in meters) of each geomorphology in each depth class 
        depth_class_geo_dict = {}
        dc_ids = depth_class_dict.keys()
        for dc_id in dc_ids:
            #generate depthclass raster
            dc_raster = 'dcresult_%s' %dc_id
            depth_class_result = """r.mapcalc "%s = if(depth_class==%s,dcresult,null())" """ % (dc_raster, dc_id)
            g.run(depth_class_result)
            #generate geomorphology results for current depthclass
            dc_geo_raster = 'depth_class_%s_georesult' %dc_id
            dc_result = """r.mapcalc "%s = if(%s==%s,geomorphology,null())" """ %(dc_geo_raster, dc_raster, dc_id)
            g.run(dc_result)
            #generate dictionary from stats
            dc_name_dict, dc_dict = get_dict_from_stats(g, Geomorphology, dc_geo_raster)
            depth_class_geo_dict[DepthClass.objects.get(id=dc_id).short_name] = dc_name_dict
        offshore_report['depth_class_geomorphology']=depth_class_geo_dict
        
        #depth class substrate stats -- collecting area (in meters) of each substrate in each depth class 
        offshore_report['depth_class_substrate']=transpose_nested_dict(substrate_dc_dict)
        
        # Geomorphology -- Drilling Down
        
        #geomorphology substrate stats -- collecting area (in meters) of each substrate in each geomorphology
        offshore_report['geomorphology_substrate']=transpose_nested_dict(substrate_geo_dict)
        
        #geomorphology depth_class stats -- collecting area (in meters) of each depth_class in each geomorphology
        offshore_report['geomorphology_depth_class']=transpose_nested_dict(depth_class_geo_dict)
        
        return simplejson.dumps(offshore_report)

    def transpose_nested_dict(orig_dict):
        transposed_dict = {}
        for key, value in orig_dict.items():
            for inner_key, area in value.items():
                if inner_key not in transposed_dict.keys():
                    transposed_dict[inner_key] = {key: area}
                else:
                    transposed_dict[inner_key][key] = area
        return transposed_dict
    
    def get_dict_from_stats(g, model_class, input_rast):  
        #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
        stats = g.run('r.stats -an input=%s' %input_rast)  
        #stats is something like the following: '2 1360911.649924\n4 2940800464.852541\n'
        stats_list = stats.split()
        #stats_list becomes: ['2', '1360911.649924', '4', '2940800464.852541']
        clean_list = clean_stats_list(stats_list)
        int_list = [int(float(x)+.5) for x in clean_list]
        #int_list becomes: [2, 1360911, 4, 2940800464]
        stats_dict = dict(zip(int_list[::2], int_list[1::2])) 
        #stats_dict becoms: {2: 1360911, 4: 2940800464}
        name_dict = dict( map( lambda(key, value): (model_class.objects.get(id=key).short_name, value), stats_dict.items()))
        #name_dict finally becomes: {'Flat': 1360911, 'Slope': 2940800464}
        return name_dict, stats_dict
    
    def clean_stats_list(list):
        clean_list = []
        #note the following '-' search is taking care to remove possible range values in stats list
        for item in list:
            if '-' in item:
                clean_list.append( item[:item.find('-')] )
            else:
                clean_list.append(item)
        return clean_list
                
    
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
        if self.input_objective.short_name == 'nearshore_conservation':
            substrate_names = [substrate.name for substrate in self.input_nearshore_substrate.all()]
        else: 
            substrate_names = [substrate.name for substrate in self.input_substrate.all()]
        return substrate_names
    
    @property
    def input_exposure_names(self):
        exposure_names = [exposure.name for exposure in self.input_nearshore_exposure.all()]
        return exposure_names
    
    @property
    def input_ecosystem_names(self):
        ecosystem_names = [ecosystem.name for ecosystem in self.input_nearshore_ecosystem.all()]
        return ecosystem_names
    
    @property
    def input_depth_class_names(self):
        depth_class_names = [depth_class.name for depth_class in self.input_depth_class.all()]
        return depth_class_names
        
    @property
    def input_geomorphology_names(self):
        geomorphology_names = [geomorphology.name for geomorphology in self.input_geomorphology.all()]
        return geomorphology_names
    
    @property
    def input_upwelling_names(self):
        upwelling_names = [upwelling.name for upwelling in self.input_upwelling.all()]
        return upwelling_names
        
    @property
    def input_chlorophyl_names(self):
        chlorophyl_names = [chlorophyl.name for chlorophyl in self.input_chlorophyl.all()]
        return chlorophyl_names
                
    @property
    def input_wind_potential_names(self):
        wind_names = [wind.name for wind in self.input_wind_potential.all()]
        return wind_names
                       
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
    short_name = models.CharField(max_length=70, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' %self.name
        
class Objective(models.Model):
    name = models.CharField(max_length=70)
    short_name = models.CharField(max_length=70, null=True, blank=True)
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
    short_name = models.CharField(max_length=70, null=True, blank=True)
    
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
    short_name = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=8, default='778B1A55')

    def __unicode__(self):
        return u'%s' % self.name
        
class WindPotential(models.Model): 
    name = models.CharField(max_length=30)  
    short_name = models.CharField(max_length=30, null=True, blank=True)
    density = models.CharField(max_length=30)
    speed = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s (%s, %s)' %(self.name, self.density, self.speed)     
        
class DepthClass(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=30, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name        

class Geomorphology(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=30, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name        

class NearshoreSubstrate(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=8, default='778B1A55')
    
    def __unicode__(self):
        return u'%s' %self.name
        
class NearshoreExposure(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' %self.name
        
class NearshoreEcosystem(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' %self.name
        
class Upwelling(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' %self.name
        
class Chlorophyl(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' %self.name
        
class OffshoreConservationParameterArea(models.Model):
    name = models.CharField(max_length=70)
    area = models.FloatField(null=True,blank=True, verbose_name="area in meters")
    
    def __unicode__(self):
        return u'%s' %self.name
        
class WindEnergyParameterArea(models.Model):
    name = models.CharField(max_length=70)
    area = models.FloatField(null=True,blank=True, verbose_name="area in meters")
    
    def __unicode__(self):
        return u'%s' %self.name
        
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
        verbose_name = 'Area'
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
        verbose_name = 'Point'
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
        verbose_name = 'Line'
        form = 'scenario.forms.LoiForm'
        icon_url = 'wmm/img/loi.png'

@register
class UserKml(PrivateLayerList):
    class Options:
        verbose_name = 'Uploaded KML'
        form = 'scenario.forms.UserKmlForm'
        icon_url = 'media/common/images/kml_document_icon.png'
