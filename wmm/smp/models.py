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
    
class DriftCell(models.Model):
    objectid = models.IntegerField()
    ws_llid_nr = models.CharField(max_length=13, null=True, blank=True)
    ws_begin_a = models.FloatField()
    ws_end_ad = models.FloatField()
    dc_ds_path = models.CharField(max_length=64, null=True, blank=True)
    dcell_nr = models.CharField(max_length=20)
    cell_type = models.CharField(max_length=4)
    description = models.CharField(max_length=64)
    shape_leng = models.FloatField()
    geometry = models.MultiLineStringField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Drift Cells")
    objects = models.GeoManager()    
    
class LandUse(models.Model):
    landuse_cd = models.IntegerField()
    descr = models.CharField(max_length=72)
    source = models.CharField(max_length=24)
    area = models.FloatField()
    lu_code = models.FloatField()
    lu_class = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    objects = models.GeoManager()   
    
    class Meta:
        abstract = True 
    
class LandUseCultural(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Cultural Land Use")
    
class LandUseManufacturing(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Manufacturing Land Use")

class LandUseResidential(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Residential Land Use")

class LandUseServices(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Services Land Use")

class LandUseTrade(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Trade Land Use")

class LandUseTransportation(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Transportation Land Use")

class LandUseUndeveloped(LandUse):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Undeveloped Land Use")
    
class PublicAccess(models.Model):
    objectid = models.IntegerField()
    beach_name = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    class_desc = models.CharField(max_length=254, null=True, blank=True)
    beach_name_caps = models.CharField(max_length=254, null=True, blank=True)
    owner = models.CharField(max_length=254, null=True, blank=True)
    length = models.FloatField()
    rep_name = models.CharField(max_length=254, null=True, blank=True)
    geometry = models.PointField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Public Access Sites")
    objects = models.GeoManager()    
    
class HarvestSite(models.Model):
    acres = models.FloatField()
    company = models.CharField(max_length=64)
    geometry = models.PointField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Harvest Sites")
    objects = models.GeoManager()
    
class CommercialGrowingArea(models.Model):
    status = models.CharField(max_length=20)
    acres = models.FloatField()
    name = models.CharField(max_length=60)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Commercial Growing Areas")
    objects = models.GeoManager()

class OysterReserve(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    area_acres = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Oyster Reserves")
    objects = models.GeoManager()

class OysterTract(models.Model):
    app_no = models.CharField(max_length=10, null=True, blank=True)
    orig_id = models.IntegerField()
    area_acres = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Oyster Tracts")
    objects = models.GeoManager()    
    
    