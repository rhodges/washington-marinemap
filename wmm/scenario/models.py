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
    '''
    input_parameters_tidal_energy = models.ManyToManyField("TidalEnergyParameter")
    input_dist_shore_tidal_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_tidal_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_tidal_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_tidal_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_tidal_energy = models.ManyToManyField("Substrate", related_name="MOSTidalEnergySubstrate", null=True, blank=True)
    
    input_parameters_wind_energy = models.ManyToManyField("WindEnergyParameter")
    input_dist_shore_wind_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_wind_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_wind_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_wind_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_wind_energy = models.ManyToManyField("Substrate", related_name="MOSWindEnergySubstrate", null=True, blank=True)
    
    input_parameters_wave_energy = models.ManyToManyField("WaveEnergyParameter")
    input_dist_shore_wave_energy = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_wave_energy = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_wave_energy = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_wave_energy = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_wave_energy = models.ManyToManyField("Substrate", related_name="MOSWaveEnergySubstrate", null=True, blank=True)
    
    # Conservation Parameters
    
    input_parameters_offshore_conservation = models.ManyToManyField("OffshoreConservationParameter")
    input_dist_shore_offshore_conservation = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_offshore_conservation = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_offshore_conservation = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_offshore_conservation = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_offshore_conservation = models.ManyToManyField("Substrate", related_name="MOSOffshoreConservationSubstrate", null=True, blank=True)
    
    input_parameters_nearshore_conservation = models.ManyToManyField("NearshoreConservationParameter")
    input_dist_shore_nearshore_conservation = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_nearshore_conservation = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_nearshore_conservation = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_nearshore_conservation = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_nearshore_conservation = models.ManyToManyField("Substrate", related_name="MOSNearshoreConservationSubstrate", null=True, blank=True)
    
    input_parameters_water_column_conservation = models.ManyToManyField("WaterColumnConservationParameter")
    input_dist_shore_water_column_conservation = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_water_column_conservation = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_water_column_conservation = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_water_column_conservation = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_water_column_conservation = models.ManyToManyField("Substrate", related_name="MOSWaterColumnConservationSubstrate", null=True, blank=True)
    
    # Development Parameters
    
    input_parameters_shoreside_development = models.ManyToManyField("ShoresideDevelopmentParameter")
    input_dist_shore_shoreside_development = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_shoreside_development = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_shoreside_development = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_shoreside_development = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_shoreside_development = models.ManyToManyField("Substrate", related_name="MOSShoresideDevelopmentSubstrate", null=True, blank=True)
    
    # Fisheries Parameters
    
    input_parameters_shellfish_aquaculture = models.ManyToManyField("ShellfishAquacultureParameter")
    input_dist_shore_shellfish_aquaculture = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_shellfish_aquaculture = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_shellfish_aquaculture = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_shellfish_aquaculture = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_shellfish_aquaculture = models.ManyToManyField("Substrate", related_name="MOSShellfishAquacultureSubstrate", null=True, blank=True)
    
    input_parameters_offshore_fishing = models.ManyToManyField("OffshoreFishingParameter")
    input_dist_shore_offshore_fishing = models.FloatField(verbose_name='Distance from Shoreline', null=True, blank=True)
    input_dist_port_offshore_fishing = models.FloatField(verbose_name='Distance to Port', null=True, blank=True)
    input_min_depth_offshore_fishing = models.FloatField(verbose_name='Minimum Depth', null=True, blank=True)
    input_max_depth_offshore_fishing = models.FloatField(verbose_name='Maximum Depth', null=True, blank=True)
    input_substrate_offshore_fishing = models.ManyToManyField("Substrate", related_name="MOSOffshoreFishingSubstrate", null=True, blank=True)
    '''
    
    description = models.TextField(null=True, blank=True)
    support_file = models.FileField(upload_to='scenarios/files/', null=True, blank=True)
       
       
    def save(self, form=None, *args, **kwargs):
        if form is not None: 
            form_data = form.cleaned_data 
            user = form_data['user'] 
            name = form_data['name']
            self.name = name
            first_run = True
            rerun = False
            
            # if this is an edit request
            if self.pk is not None:
                #if no input_ fields have changed, then save without rerunning scenario analysis
                first_run = False
                #TODO: might move the following into a function rerun=inputs_have_changed()
                orig = MOS.objects.get(pk=self.pk)
                input_fields = [f for f in self._meta.fields if f.attname.startswith('input_')]
                for f in input_fields:
                    if getattr(orig, f.name) != getattr(self, f.name):
                        rerun = True
                        break
                if not rerun:
                    #IMPORTANT NOTE:  We can't compare the objectives until we save m2m
                    #first collect the original objectives, parameters, and substrate values, then save, then compare 
                    from itertools import chain
                    orig_objs = list(chain(self.input_objectives_energy.all(), self.input_objectives_conservation.all(), self.input_objectives_development.all(), self.input_objectives_fisheries.all()))
                    
                    orig_dict = {}
                    for obj in orig_objs:
                        suffix = obj.objective.short_name
                        #it appears that getattr returns a dynamic list (one that gets updated after call to super.save below)
                        #casting to list here makes the list static, preventing automatic changes after super.save
                        orig_dict['input_params_%s'%suffix] = list(getattr(self, 'input_parameters_%s'%suffix).all())
                        orig_dict['input_substrate_%s'%suffix] = list(getattr(self, 'input_substrate_%s'%suffix).all())
                    
                    #save so that m2m variables are updated
                    super(MOS, self).save(form=form)
                    
                    #get new objectives
                    new_objs = self.input_objectives.all()
                    
                    #now compare for differences
                            
                    #compare obj lists
                    if len(orig_objs) != len(new_objs):
                        rerun = True
                    else:
                        objs_differ = len([i==j for i, j in zip(orig_objs, new_objs) if i!=j]) > 0
                        if objs_differ:
                            rerun = True
                    if not rerun:
                        for obj in orig_objs:
                            suffix = obj.objective.short_name
                            orig_params = orig_dict['input_params_%s'%suffix]
                            new_params = getattr(self, 'input_parameters_%s'%suffix).all()
                            if len(orig_params) != len(new_params):
                                rerun = True
                                break
                            else:
                                for i in range(len(orig_params)):
                                    if orig_params[i] != new_params[i]:
                                        rerun = True
                                        break
                            if not rerun:
                                orig_substrate = orig_dict['input_substrate_%s'%suffix]
                                new_substrate = getattr(self, 'input_substrate_%s'%suffix).all()
                                if len(orig_substrate) != len(new_substrate):
                                    rerun = True
                                    break
                                else:
                                    for i in range(len(orig_substrate)):
                                        if orig_substrate[i] != new_substrate[i]:
                                            rerun = True
                                            break
            
            #NOTE:  This might need to be used to save self (maybe with form kwarg?) to save instance before scenarios are built
            super(MOS, self).save(form=form)
            
            if first_run or rerun: 
                #remove old scenarios from this multi-objective scenario object 
                #TODO:  consider optimizing this so that it only removes those scenarios that need to be re-generated
                old_scenarios = Scenario.objects.filter(mos=self.id)
                for old_scenario in old_scenarios:
                    self.scenarios.remove(old_scenario) #removes the relationship but not the scenario itself
                    old_scenario.delete()              #removes the actual scenario
                                
                #generate new scenarios
                '''
                energy_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_energy']]
                conservation_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_conservation']]
                development_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_development']]
                fisheries_objectives = [self.input_objectives.add(obj.objective) for obj in form_data['input_objectives_fisheries']]
                '''  
                input_objectives = [obj.objective for obj in form_data['input_objectives_energy']]
                input_objectives += [obj.objective for obj in form_data['input_objectives_conservation']]
                input_objectives += [obj.objective for obj in form_data['input_objectives_development']]
                input_objectives += [obj.objective for obj in form_data['input_objectives_fisheries']]
                                
                for obj in input_objectives:
                    #obj_id = obj.objective.id
                    obj_short_name = obj.short_name
                    scenario_name = name + '_%s' % obj_short_name
                    
                    params = form_data['input_parameters_%s'%obj_short_name]
                    
                    dist_shore = form_data['input_dist_shore_%s'%obj_short_name]
                    dist_port = form_data['input_dist_port_%s'%obj_short_name]
                    min_depth = form_data['input_min_depth_%s'%obj_short_name]
                    max_depth = form_data['input_max_depth_%s'%obj_short_name]
                    substrates = form_data['input_substrate_%s'%obj_short_name]
                    
                    scenario = Scenario(user=user, name=scenario_name, input_objective=obj, input_dist_shore=dist_shore,
                                        input_dist_port = dist_port, input_min_depth=min_depth, input_max_depth=max_depth)            
                    scenario.save(rerun=False)
                    
                    for param in params:
                        scenario.input_parameters.add(param.parameter)
                        for substrate in substrates:
                            scenario.input_substrate.add(substrate)
                    scenario.save()
                    self.scenarios.add(scenario)
                    
        super(MOS, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name
        
    def support_filename(self):
        return os.path.basename(self.support_file.name)
    '''      
    #@property
    #def input_objectives(self):
        #return list(chain(self.input_objectives_energy.all(), self.input_objectives_conservation.all(), self.input_objectives_development.all(), self.input_objectives_fisheries.all()))
          
    @property
    def input_objective_names(self):
        import pdb
        pdb.set_trace()
        names = []
        energy_names = [obj.objective.short_name for obj in self.input_objectives_energy.all()]
        conservation_names = [obj.objective.short_name for obj in self.input_objectives_conservation.all()]
        development_names = [obj.objective.short_name for obj in self.input_objectives_development.all()]
        fisheries_names = [obj.objective.short_name for obj in self.input_objectives_fisheries.all()]
        names = energy_names + conservation_names + development_names + fisheries_names
        return names
        #obj.objective.short_name
        #return getattr(self, 'input_objectives_%s' %self.input_objective.short_name)
    '''      
    @property
    def objective_ids(self):
        obj_ids = [scenario.input_objective.id for scenario in self.scenarios.all()]
        return obj_ids
          
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
        for scenario in self.scenarios.all():
            name = self.name + '_' + scenario.input_objective.name
            kml =   """
                    %s
                    <Placemark>
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
                        <MultiGeometry>
                        %s
                        </MultiGeometry>
                    </Placemark>
                    """ % ( self.scenario_style(scenario.color), escape(name), self.model_uid(),
                            escape(self.name), self.user, escape(self.description), self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
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
    
    geometry_final = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Final Scenario Geometry")
    
    def run(self):
        from lingcod.analysistools.grass import Grass

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
            substrate_formula = ' || '.join(['substrate==%s' % s.id for s in self.input_substrate.all()])
            substrate = 'if(%s)' %substrate_formula
        else:   
            substrate = 1
        
        if 6 in input_params:
            depth_class_formula = ' || '.join(['depth_class==%s' % dc.id for dc in self.input_depth_class.all()])
            depth_class = 'if(%s)' %depth_class_formula
        else:   
            depth_class = 1
        
        if 7 in input_params:
            geomorphology_formula = ' || '.join(['geomorphology==%s' % g.id for g in self.input_geomorphology.all()])
            geomorphology = 'if(%s)' %geomorphology_formula
        else:   
            geomorphology = 1
        
        mapcalc = """r.mapcalc "rresult = if((%s + %s + %s + %s)==4,1,null())" """ % (port_buffer, shoreline_buffer, substrate, depth)
        #mapcalc = """r.mapcalc "rresult = if((if(shoreline_rast_buffer==2) + if(port_buffer_rast) + if(bathy>%s && bathy<%s) + if(%s))==4,1,null())" """ % (self.input_min_depth, self.input_max_depth, substrate_formula) 
        g.run(mapcalc)
        self.output_mapcalc = mapcalc
        
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
        
    def save(self, rerun=True, *args, **kwargs):
        # only rerun the analysis if any of the input_ fields have changed
        # ie if name and description change no need to rerun the full analysis
        if self.pk is not None:
            rerun = False
            outputs = Scenario.output_fields()
            for output in outputs:
                if output.null:
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
                super(Scenario, self).save(rerun=False, *args, **kwargs)
                new_substrates = set(getattr(self, 'input_substrate').all())
                if orig_substrates != new_substrates:
                    rerun = True
        super(Scenario, self).save(rerun=rerun, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name
        
    def support_filename(self):
        return os.path.basename(self.support_file.name)
        
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
        
    @property
    def input_depth_class(self):
        return getattr(self, 'input_depth_class_%s' %self.input_objective.short_name)
        
    @property
    def input_geomorphology(self):
        return getattr(self, 'input_geomorphology_%s' %self.input_objective.short_name)
        
    #@property
    #def input_parameters(self):        
    #    return getattr(self, 'input_parameters_%s' %self.input_objective.short_name)

    @property
    def input_parameter_ids(self):
        #input_params = [p.parameter.id for p in self.input_parameters.all()]
        input_params = [p.id for p in self.input_parameters.all()]
        return input_params
        
    @property
    def input_substrate_names(self):
        input_substrate = [substrate.name for substrate in self.input_substrate.all()]
        return input_substrate
        
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
