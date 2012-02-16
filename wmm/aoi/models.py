from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from lingcod.features import register, alternate
from lingcod.common.utils import asKml
from lingcod.features.models import PointFeature, LineFeature, PolygonFeature
from lingcod.raster_stats.models import RasterDataset, zonal_stats

@register
class AOI(PolygonFeature):
    description = models.TextField(null=True,blank=True)
    geometry_hash = models.BigIntegerField(null=True, blank=True)
    conservation_score = models.IntegerField(verbose_name='Conservation Score', null=True, blank=True)
    
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
        #calculate objective scores
        #intersect with ConservationScoring (vector) or with benthic_scoring (raster/zonal_stats)
        self.geometry_hash = self.geometry_final.wkt.__hash__()
        
        #vector analysis
        scoring_objects = ConservationScoring.objects.filter(geometry__bboverlaps=self.geometry_final)
        total_area = 0.0
        total_score = 0.0
        
        for scoring_object in scoring_objects:
            scoring_geom = scoring_object.geometry
            overlap = scoring_geom.intersection(self.geometry_final)
            if overlap.area > 0:
                total_area += overlap.area
                total_score += scoring_object.score * overlap.area
        
        avg_score = total_score / total_area
        self.conservation_score = int(round(avg_score * 10))
        '''
        NOTE:  THIS RASTER FILE WILL NEED TO BE ADDED TO THE SERVER BEFORE ENABLING THE FOLLOWING
        import pdb
        pdb.set_trace()
        #raster analysis with starspan
        benthic_scoring = RasterDataset.objects.get(name='benthic_scoring')
        benthic_stats = zonal_stats(self.geometry_final, benthic_scoring)
        if benthic_stats.avg:
            raster_score = benthic_stats.avg * 10
        else:
            raster_score = None
        self.conservation_score = raster_score
        '''
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


'''Reporting Models'''        
        
'''Physical Layers'''
        
class BenthicHabitat(models.Model):
    depth = models.CharField(max_length=20)
    geomorph = models.CharField(max_length=20)
    substrate = models.CharField(max_length=20)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Benthic Habitat")
    objects = models.GeoManager()        
    
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
    
class Island(models.Model):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Island")
    objects = models.GeoManager()    
    
class Upwelling(models.Model):
    type = models.CharField(max_length=8)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Upwelling")
    objects = models.GeoManager()    
    
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

