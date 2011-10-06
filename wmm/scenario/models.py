import time
import os
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from lingcod.analysistools.models import Analysis
from lingcod.features import register, alternate
from lingcod.common.utils import asKml
from lingcod.features.models import PointFeature, LineFeature, PolygonFeature, FeatureCollection
from lingcod.layers.models import PrivateLayerList

@register
class Scenario(Analysis):
    #Input Parameters
    input_dist_shore = models.FloatField(verbose_name='Distance from Shoreline')
    input_dist_port = models.FloatField(verbose_name='Distance to Port')
    input_min_depth = models.FloatField(verbose_name='Minimum Depth')
    input_max_depth = models.FloatField(verbose_name='Maximum Depth')
    
    input_substrate = models.ManyToManyField("Substrate")
    
    #Descriptors (name field is inherited from Analysis)
    description = models.TextField(null=True, blank=True)
    
    # All output fields should be allowed to be Null/Blank
    output_geom = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID,
            null=True, blank=True, verbose_name="Scenario Geometry")
    output_mapcalc = models.CharField(max_length=360, null=True, blank=True)
    output_area = models.FloatField(null=True, blank=True, verbose_name="Total Area (sq km)")
    
    def run(self):
        from lingcod.analysistools.grass import Grass

        g = Grass('pacnw_utm10', 
                gisbase=settings.GISBASE, #"/usr/local/grass-6.4.1RC2", 
                gisdbase=settings.GISDBASE,  #"/mnt/wmm/grass",
                autoclean=True)
        g.verbose = True
        
        g.run('g.region rast=bathy')
        g.run('g.region nsres=180 ewres=180')
        rasts = g.list()['rast']

        outdir = settings.GRASS_TMP #'/tmp'
        outbase = 'wa_scenario_%s' % str(time.time()).split('.')[0]
        output = os.path.join(outdir,outbase+'.json')
        if os.path.exists(output):
            raise Exception(output + " already exists")

        g.run('v.buffer input=ports output=port_buffer distance=%s' % (self.input_dist_port * 1000,) )
        g.run('v.to.rast input=port_buffer output=port_buffer_rast use=cat')

        g.run('r.buffer input=shoreline_rast output=shoreline_rast_buffer distances=%s' % (self.input_dist_shore * 1000,) )

        substrate_formula = ' || '.join(['substrate==%s' % s.id for s in self.input_substrate.all()])
        
        mapcalc = """r.mapcalc "rresult = if((if(shoreline_rast_buffer==2) + if(port_buffer_rast) + if(bathy>%s && bathy<%s) + if(%s))==4,1,null())" """ % (self.input_min_depth, self.input_max_depth, substrate_formula) 
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

        #cleanup
        os.remove(output)
        del g

        return True
        
    def save(self, rerun=True, *args, **kwargs):
        # only rerun the analysis if any of the input_ fields have changed
        # ie if name and description change no need to rerun the full analysis
        if self.pk is not None:
            rerun = False
            orig = Scenario.objects.get(pk=self.pk)
            for f in Scenario.input_fields():
                # Is original value different from form value?
                #if orig._get_FIELD_display(f) != getattr(self,f.name):
                if getattr(orig, f.name) != getattr(self, f.name):
                    rerun = True
                    break
            if not rerun:
                #the substrates need to be grabbed, then saved, then grabbed again because both getattr calls 
                #(regardless of whether we use orig or self) return the same original list until the model has been saved 
                #(I assume this means the form.save_m2m actually has to be called), after which calls to getattr 
                #will return the same list (regardless of whether we use orig or self)
                orig_substrates = set(getattr(orig, 'input_substrate').all())
                super(Scenario, self).save(rerun=False, *args, **kwargs)
                new_substrates = set(getattr(self, 'input_substrate').all())
                if orig_substrates != new_substrates:
                    rerun = True
        super(Scenario, self).save(rerun=rerun, *args, **kwargs)

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
            <MultiGeometry>
            %s
            </MultiGeometry>
        </Placemark>
        """ % (self.kml_style, self.uid, escape(self.name), self.model_uid(),
            asKml(self.output_geom.transform( settings.GEOMETRY_CLIENT_SRID, clone=True))
            )
    
    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
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
        """ % (self.model_uid(),)
    
    class Options:
        verbose_name = 'Scenario'
        #icon_url = 'bmm/img/regions.png'
        form = 'scenario.forms.ScenarioForm'
        form_template = 'scenario/form.html'
        show_template = 'scenario/show.html'


class Substrate(models.Model):
    name = models.CharField(max_length=30)  

    def __unicode__(self):
        return u'%s' % self.name
    
        
@register
class Folder(FeatureCollection):
        
    class Options:
        verbose_name = 'Folder'
        valid_children = ( 'scenario.models.Scenario', 
	                   'scenario.models.AOI', 
	                   'scenario.models.POI', 
	                   'scenario.models.LOI', 
	                   'scenario.models.UserKml', 
	                   'lingcod.bookmarks.models.Bookmark', 
                           'scenario.models.Folder')
        form = 'scenario.forms.FolderForm'
        show_template = 'folder/show.html'

    @classmethod
    def css(klass):
        return """ li.%(uid)s > .icon { 
        background: url('%(media)skmltree/dist/images/sprites/kml.png?1302821411') no-repeat -231px 0px ! important;
        } """ % { 'uid': klass.model_uid(), 'media': settings.MEDIA_URL }


@register
class AOI(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    class Options:
        verbose_name = 'Area of Interest'
        form = 'scenario.forms.AoiForm'
        manipulators = []

@register
class POI(PointFeature):
    description = models.TextField(null=True,blank=True)
    class Options:
        verbose_name = 'Point of Interest'
        form = 'scenario.forms.PoiForm'

@register
class LOI(LineFeature):
    description = models.TextField(null=True,blank=True)
    class Options:
        verbose_name = 'Line of Interest'
        form = 'scenario.forms.LoiForm'

@register
class UserKml(PrivateLayerList):
    class Options:
        verbose_name = 'Uploaded KML'
        form = 'scenario.forms.UserKmlForm'
