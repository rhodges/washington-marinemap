from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from madrona.features import register, alternate
from madrona.common.utils import asKml
from madrona.features.models import PointFeature, LineFeature, PolygonFeature
from madrona.raster_stats.models import RasterDataset, zonal_stats
from picklefield import PickledObjectField

@register
class AOI(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    geometry_hash = models.BigIntegerField(null=True, blank=True)
    conservation_score = models.IntegerField(verbose_name='Conservation Score', null=True, blank=True)
    tidalenergy_score = models.IntegerField(verbose_name='Tidal Energy Score', null=True, blank=True)
    waveenergy_score = models.IntegerField(verbose_name='Wave Energy Score', null=True, blank=True)
    windenergy_score = models.IntegerField(verbose_name='Wind Energy Score', null=True, blank=True)
    
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

    def run(self):
        def get_tradeoff_score(model_class):
            scoring_objects = model_class.objects.filter(geometry__bboverlaps=self.geometry_final)
            total_area = 0.0
            total_score = 0.0
            
            for scoring_object in scoring_objects:
                scoring_geom = scoring_object.geometry
                overlap = scoring_geom.intersection(self.geometry_final)
                if overlap.area > 0:
                    total_area += overlap.area
                    total_score += scoring_object.score * overlap.area
            if total_area > 0:
                return total_score / total_area
            else:
                return 0
                
        #calculate objective scores
        avg_score = get_tradeoff_score(ConservationScoring)        
        self.conservation_score = int(round(avg_score * 10))
        avg_score = get_tradeoff_score(TidalEnergyScoring)        
        self.tidalenergy_score = int(round(avg_score * 10))
        avg_score = get_tradeoff_score(WaveEnergyScoring)        
        self.waveenergy_score = int(round(avg_score * 10))
        avg_score = get_tradeoff_score(WindEnergyScoring)        
        self.windenergy_score = int(round(avg_score * 10))
        
        self.geometry_hash = self.geometry_final.wkt.__hash__()
        
        return True        
        
    def save(self, *args, **kwargs):
        #save the new entry
        super(AOI, self).save(*args, **kwargs)
        #might also check for absent scores (ensure that scoring fields added later would still be updated)
        if self.geometry_final.wkt.__hash__() != self.geometry_hash:
            self.run()
            super(AOI, self).save(*args, **kwargs)

    class Options:
        manipulators = []
        optional_manipulators = [ 
                'wmm_manipulators.manipulators.ExcludeFederalWatersManipulator',
                'wmm_manipulators.manipulators.ExcludeStateWatersManipulator',
                'wmm_manipulators.manipulators.ExcludeEstuariesManipulator',
                'wmm_manipulators.manipulators.ExcludeTerrestrialManipulator']
        verbose_name = 'Area'
        form = 'aoi.forms.AoiForm'
        form_template = 'aoi/form.html'
        show_template = 'aoi/show.html'
        icon_url = 'wmm/img/aoi.png'

        
'''Scoring Models'''
       
class ConservationScoring(models.Model):
    score = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Conservation Scoring Grid")
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'Conservation Score: %s' %self.score              

class TidalEnergyScoring(models.Model):
    score = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Tidal Energy Scoring Grid")
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'Tidal Energy Score: %s' %self.score              

class WindEnergyScoring(models.Model):
    score = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Wind Energy Scoring Grid")
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'Wind Energy Score: %s' %self.score              

class WaveEnergyScoring(models.Model):
    score = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Wave Energy Scoring Grid")
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'Wave Energy Score: %s' %self.score              


'''Reporting Models'''     

'''Caching Model'''   
        
class ReportCache(models.Model):
    wkt_hash = models.BigIntegerField(null=True, blank=True) 
    title = models.CharField(max_length=35)
    report = PickledObjectField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    
    def save(self, *args, **kwargs):
        from report_caching import remove_report_cache
        remove_report_cache(self.wkt_hash, self.title)
        super(ReportCache, self).save(*args, **kwargs)
        
class ZonalCache(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    
                  
'''Energy Layers'''

class WindPower(models.Model):
    wpc = models.FloatField()
    potential = models.CharField(max_length=32)
    densitywm2 = models.CharField(max_length=16)
    speed_ms = models.CharField(max_length=16)
    speed_mph = models.CharField(max_length=16)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Wind Power")
    objects = models.GeoManager()
               
class TidalSubstrate(models.Model):
    gridcode = models.IntegerField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Tidal Substrate")
    objects = models.GeoManager()
    
class TidalSubstrateArea(models.Model):
    gridcode = models.IntegerField()
    area = models.FloatField()
    
    
'''Physical Layers'''
        
class BenthicHabitat(models.Model):
    depth = models.CharField(max_length=20)
    geomorph = models.CharField(max_length=20)
    substrate = models.CharField(max_length=20)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Benthic Habitat")
    objects = models.GeoManager()        
    
class BenthicDepthArea(models.Model):
    depth = models.CharField(max_length=12)
    area = models.FloatField()
    
class BenthicGeomorphArea(models.Model):
    geomorph = models.CharField(max_length=12)
    area = models.FloatField()
    
class BenthicSubstrateArea(models.Model):
    substrate = models.CharField(max_length=12)
    area = models.FloatField()
    
class Canyon(models.Model):
    phys_hab = models.CharField(max_length=40)
    sgh_lith_1 = models.CharField(max_length=15)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Canyon")
    objects = models.GeoManager()    
    
class RockySubstrate(models.Model):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Rocky Substrate")
    objects = models.GeoManager()  

class EstuaryHabitat(models.Model):
    habitat = models.CharField(max_length=12)
    substrate = models.CharField(max_length=29)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Estuary Habitat/Substrate")
    objects = models.GeoManager()    
    
class EstuaryHabitatArea(models.Model):
    habitat = models.CharField(max_length=12)
    area = models.FloatField()
    
class EstuarySubstrateArea(models.Model):
    substrate = models.CharField(max_length=29)
    area = models.FloatField()
    
class Island(models.Model):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Island")
    objects = models.GeoManager()    
    
class Upwelling(models.Model):
    type = models.CharField(max_length=8)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Upwelling")
    objects = models.GeoManager()    
    
class UpwellingArea(models.Model):
    type = models.CharField(max_length=8)
    area = models.FloatField()
    
'''Biological Layers'''

class Seabird(models.Model):
    species = models.CharField(max_length=40)
    count = models.IntegerField()
    geometry = models.PointField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Seabird Colonies")
    objects = models.GeoManager()
    
class SnowyPloverHabitat(models.Model):
    state = models.CharField(max_length=5)
    unit_name = models.CharField(max_length=50)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Snowy Plover Critical Habitats")
    objects = models.GeoManager()

class Haulout(models.Model):
    com_name = models.CharField(max_length=50)
    count = models.IntegerField()
    geometry = models.PointField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Seal and Sealion Haulout Sites")
    objects = models.GeoManager()

class OrcaHabitat(models.Model):
    tgt = models.CharField(max_length=20)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Killer Whale Critical Habitats")
    objects = models.GeoManager()

class Kelp(models.Model):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Kelp")
    objects = models.GeoManager()

class Chlorophyll(models.Model):
    type = models.CharField(max_length=8)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Chlorphyll")
    objects = models.GeoManager()

class ChlorophyllArea(models.Model):
    type = models.CharField(max_length=8)
    area = models.FloatField()
    
class Coral(models.Model):
    ordcode = models.CharField(max_length=11)
    sum_cpuekg = models.FloatField()
    coral_type = models.CharField(max_length=64)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Coral")
    objects = models.GeoManager()

class Sponge(models.Model):
    cpuekgkm = models.FloatField()
    common_nam = models.CharField(max_length=24, null=True, blank=True)
    target_nam = models.CharField(max_length=50)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Sponge")
    objects = models.GeoManager()

class OlympiaOyster(models.Model):
    estuary = models.CharField(max_length=30)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Olympia Oysters")
    objects = models.GeoManager()

