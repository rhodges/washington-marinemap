from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.utils.html import escape
from picklefield import PickledObjectField
from lingcod.common.utils import asKml
from lingcod.features import register, alternate
from lingcod.features.models import Feature, PolygonFeature

# Create your models here.
    
@register
class SMPSite(PolygonFeature):
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
        return '778B1A55'             

    class Options:
        verbose_name = 'SMP Characterization Site'
        form = 'smp.forms.SMPSiteForm'
        form_template = 'form.html'
        show_template = 'show.html'
        icon_url = 'wmm/img/smp.png'

class ReportCache(models.Model):
    wkt_hash = models.CharField(max_length=255)
    context = PickledObjectField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    
    #ensure no duplicates (same geometry and type) 
    def save(self, *args, **kwargs):
        #remove any old entries
        old_entries = ReportCache.objects.filter(wkt_hash=self.wkt_hash)
        for entry in old_entries:
            ReportCache.delete(entry)
        #save the new entry
        super(ReportCache, self).save(*args, **kwargs)
 
class OverwaterStructure(models.Model):
    objectid = models.IntegerField()
    structure = models.CharField(max_length=15)
    boat = models.CharField(max_length=3)
    os_detail = models.CharField(max_length=50)
    cart_cd = models.CharField(max_length=50)
    navigability = models.CharField(max_length=50)
    county_nm = models.CharField(max_length=50)
    complexity = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Overwater Structures")
    objects = models.GeoManager()
    