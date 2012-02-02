from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from lingcod.features.models import FeatureCollection
from lingcod.features import register
from scenario.models import *


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
                           'smp.models.SMPSite',
                           'aoi.models.AOI',
                           'general.models.UserKml', 
                           'general.models.Folder',
                           'lingcod.bookmarks.models.Bookmark')
        form = 'general.forms.FolderForm'
        form_template = 'folder/form.html'
        show_template = 'folder/show.html'
        icon_url = 'wmm/img/folder.png'
