from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from lingcod.features.models import FeatureCollection
from lingcod.features import register
from scenario.models import *

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
                           'smp.models.SMPSite',
                           'aoi.models.AOI', 
                           'aoi.models.POI', 
                           'aoi.models.LOI', 
                           'scenario.models.UserKml', 
                           'lingcod.bookmarks.models.Bookmark', 
                           'general.models.Folder')
        form = 'general.forms.FolderForm'
        form_template = 'folder/form.html'
        show_template = 'folder/show.html'
        icon_url = 'wmm/img/folder.png'
