from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from madrona.features.models import FeatureCollection
from madrona.features import register
from madrona.layers.models import PrivateLayerList
from scenario.models import MOS
from aoi.models import AOI
from smp.models import SMPSite


@register
class UserKml(PrivateLayerList):
    class Options:
        verbose_name = 'Uploaded KML'
        form = 'general.forms.UserKmlForm'
        icon_url = 'media/common/images/kml_document_icon.png'
        

@register
class Folder(FeatureCollection):
    description = models.TextField(null=True,blank=True)
    
    @property
    def aoi_set(self):
        aois = []
        features = self.feature_set()
        for feature in features:
            if feature.__class__ == AOI:
                aois.append(feature)
        return aois
    
    @property
    def smp_set(self):
        smps = []
        features = self.feature_set()
        for feature in features:
            if feature.__class__ == SMPSite:
                smps.append(feature)
        return smps
    
    @property
    def num_aois(self):
        count = 0
        for object in self.feature_set():
            if object.__class__ == AOI:
                count += 1
        return count 
    
    @property
    def num_scenarios(self):
        count = 0
        for object in self.feature_set():
            if object.__class__ == MOS:
                count += 1
        return count
    '''    
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
    '''    
    class Options:
        verbose_name = 'Folder'
        valid_children = ( 'scenario.models.MOS', 
                           'smp.models.SMPSite',
                           'aoi.models.AOI',
                           'general.models.UserKml', 
                           'general.models.Folder',
                           'madrona.bookmarks.models.Bookmark')
        form = 'general.forms.FolderForm'
        form_template = 'folder/form.html'
        show_template = 'folder/show.html'
        icon_url = 'wmm/img/folder.png'

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
