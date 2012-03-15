from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.utils.html import escape
from picklefield import PickledObjectField
from madrona.common.utils import asKml
from madrona.features import register, alternate
from madrona.features.models import Feature, PolygonFeature
from general.utils import get_tradeoff_score, sq_meters_to_sq_miles

# Create your models here.
    
@register
class SMPSite(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    geometry_hash = models.BigIntegerField(null=True, blank=True)
    conservation_score = models.IntegerField(verbose_name='Conservation Score', null=True, blank=True)
    tidalenergy_score = models.IntegerField(verbose_name='Tidal Energy Score', null=True, blank=True)
    waveenergy_score = models.IntegerField(verbose_name='Wave Energy Score', null=True, blank=True)
    windenergy_score = models.IntegerField(verbose_name='Wind Energy Score', null=True, blank=True)
    
    @property
    def area_in_sq_miles(self):
        return sq_meters_to_sq_miles(self.geometry_final.area)
        
    @property
    def formatted_area(self):
        return int((self.area_in_sq_miles * 10) +.5) / 10.
        
    @property
    def kml(self):
        return """
        <Placemark id="%s">
            <visibility>1</visibility>
            <name>%s</name>
            <styleUrl>#%s-default</styleUrl>
            <ExtendedData>
                <Data name="name"><value>%s</value></Data>
                <Data name="area"><value>%s</value></Data>
                <Data name="conservation_score"><value>%s</value></Data>
                <Data name="tidal_score"><value>%s</value></Data>
                <Data name="wave_score"><value>%s</value></Data>
                <Data name="wind_score"><value>%s</value></Data>
                <Data name="user"><value>%s</value></Data>
                <Data name="desc"><value>%s</value></Data>
                <Data name="type"><value>%s</value></Data>
                <Data name="modified"><value>%s</value></Data>
            </ExtendedData>
            %s 
        </Placemark>
        """ % (self.uid, escape(self.name), self.model_uid(), 
               escape(self.name), self.formatted_area, self.conservation_score, self.tidalenergy_score, self.waveenergy_score, 
               self.windenergy_score, self.user, escape(self.description), self.Options.verbose_name, self.date_modified.replace(microsecond=0), 
               self.geom_kml)

    @property
    def kml_style(self):
        return """
        <Style id="%s-default">
            <BalloonStyle>
                <bgColor>ffeeeeee</bgColor>
                <text> <![CDATA[
                    <font color="#1A3752"><strong>$[name]</strong></font>
                    <p>Area: $[area] sq miles</p>
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
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#FDAE6B'))
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
        return '776BAEFD'             

    def run(self):
        #the following import needs to be here to prevent issues with / loss of imports due to circular imports between smp and general 
        from general.models import *
        #calculate objective scores
        avg_score = get_tradeoff_score(ConservationScoring, self.geometry_final)        
        self.conservation_score = int(round(avg_score * 10))
        avg_score = get_tradeoff_score(TidalEnergyScoring, self.geometry_final)        
        self.tidalenergy_score = int(round(avg_score * 10))
        avg_score = get_tradeoff_score(WaveEnergyScoring, self.geometry_final)        
        self.waveenergy_score = int(round(avg_score * 10))
        avg_score = get_tradeoff_score(WindEnergyScoring, self.geometry_final)        
        self.windenergy_score = int(round(avg_score * 10))
        
        self.geometry_hash = self.geometry_final.wkt.__hash__()
        
        return True        
        
    def save(self, *args, **kwargs):
        #save the new entry
        super(SMPSite, self).save(*args, **kwargs)
        #might also check for absent scores (ensure that scoring fields added later would still be updated)
        if self.geometry_final.wkt.__hash__() != self.geometry_hash or self.conservation_score is None or self.tidalenergy_score is None or self.waveenergy_score is None or self.windenergy_score is None:
            self.run()
            super(SMPSite, self).save(*args, **kwargs)

    class Options:
        manipulators = []
        optional_manipulators = [ 
                'wmm_manipulators.manipulators.ExcludeFederalWatersManipulator',
                'wmm_manipulators.manipulators.ExcludeStateWatersManipulator',
                'wmm_manipulators.manipulators.ExcludeEstuariesManipulator',
                'wmm_manipulators.manipulators.ExcludeTerrestrialManipulator']
        verbose_name = 'SMP Characterization Site'
        form = 'smp.forms.SMPSiteForm'
        form_template = 'smp/form.html'
        show_template = 'smp/show.html'
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
    
    