from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from lingcod.features.models import PolygonFeature, FeatureCollection
from lingcod.analysistools.models import Analysis
from lingcod.features import register, alternate

@register
class Scenario(Analysis):
    #Input Parameters
    input_dist_shore = models.FloatField(verbose_name='Distance from Shoreline')
    input_dist_port = models.FloatField(verbose_name='Distance to Port')
    input_min_depth = models.FloatField(verbose_name='Minimum Depth')
    input_max_depth = models.FloatField(verbose_name='Maximum Depth')
    
    #Descriptors (name field is inherited from Analysis)
    description = models.TextField(null=True, blank=True)
    
    # All output fields should be allowed to be Null/Blank
    output_geom = models.PolygonField(srid=settings.GEOMETRY_DB_SRID,
            null=True, blank=True, verbose_name="Scenario Geometry")
    
    def run(self):
#        from lingcod.analysistools.grass import Grass
#
#        coords = self.input_starting_point.transform(settings.GEOMETRY_DB_SRID, clone=True)
#        max_cost=100 * (self.input_temp_weight + self.input_language_weight + \
#                        self.input_precip_weight + self.input_biomass_weight)
#
#        g = Grass('world_moll', 
#                gisbase="/usr/local/grass-6.4.1RC2", 
#                gisdbase="/home/grass",
#                autoclean=True)
#        g.verbose = True
#        g.run('g.region rast=soilmoist')
#        rasts = g.list()['rast']
#
#        outdir = '/tmp'
#        outbase = 'bioregion_%s' % str(time.time()).split('.')[0]
#        output = os.path.join(outdir,outbase+'.json')
#        if os.path.exists(output):
#            raise Exception(output + " already exists")
#
#        g.run('r.mapcalc "weighted_combined_slope =  0.01 + ' +
#                            '(%s * temp_slope) + ' % self.input_temp_weight  + 
#                            '(%s * lang_slope) + ' % self.input_language_weight  +
#                            '(%s * precip_slope) + ' % self.input_precip_weight +
#                            '(%s * biomass_slope)' % self.input_biomass_weight +
#                            '"')
#        g.run('r.rescale input=weighted_combined_slope output=wcr_slope to=0,100')
#        g.run('r.cost -k input=wcr_slope output=cost coordinate=%s,%s max_cost=%s' % \
#                (coords[0],coords[1],max_cost) )
#        g.run('r.mapcalc "bioregion=if(cost >= 0)"')
#        g.run('r.to.vect -s input=bioregion output=bioregion_poly feature=area')
#        g.run('v.out.ogr -c input=bioregion_poly type=area format=GeoJSON dsn=%s' % output)
#
#        from django.contrib.gis.gdal import DataSource
#        ds = DataSource(output)
#        layer = ds[0]
#        geom = layer[0].geom.geos
#
#        # Take the single polygon with the largest geometry 
#        # Assume the rest are slivers, etc
#        largest_area = geom.area
#        for feat in layer[1:]:
#            if feat.geom.area > largest_area:
#                largest_area = feat.geom.area
#                geom = feat.geom.geos
#
#        geom.srid = settings.GEOMETRY_DB_SRID 
#        g2 = geom.buffer(20000)
#        geom = g2.buffer(-20000)
#        if geom and not settings.DEBUG:
#            os.remove(output)
#            del g
#        self.output_geom = geom
        return True
        
    def save(self, *args, **kwargs):
        rerun = False
        # only rerun the analysis if any of the input_ fields have changed
        # ie if name and description change no need to rerun the full analysis
        if self.pk is None:
            rerun = True
        else:
            orig = Scenario.objects.get(pk=self.pk)
            for f in Scenario.input_fields():
                # Is original value different from form value?
                if orig._get_FIELD_display(f) != getattr(self,f.name):
                    rerun = True
                    break
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


@register
class Folder(FeatureCollection):
        
    class Options:
        verbose_name = 'Folder'
        valid_children = ( 'scenario.models.Scenario', 'scenario.models.Folder')
        form = 'scenario.forms.FolderForm'
        show_template = 'folder/show.html'

    @classmethod
    def css(klass):
        return """ li.%(uid)s > .icon { 
        background: url('%(media)skmltree/dist/images/sprites/kml.png?1302821411') no-repeat -231px 0px ! important;
        } """ % { 'uid': klass.model_uid(), 'media': settings.MEDIA_URL }
    
