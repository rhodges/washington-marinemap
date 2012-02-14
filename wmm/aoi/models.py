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
        import pdb
        pdb.set_trace()
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

class ConservationScoring(models.Model):
    score = models.FloatField()
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Conservation Scoring Grid")
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'Conservation Score: %s' %self.score              


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
        form = 'aoi.forms.PoiForm'
        icon_url = 'wmm/img/poi.png'


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
        form = 'aoi.forms.LoiForm'
        icon_url = 'wmm/img/loi.png'
