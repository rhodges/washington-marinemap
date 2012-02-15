from lingcod.features.forms import SpatialFeatureForm
from django import forms
from django.forms.widgets import *
from models import *

            
class AoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = AOI
        exclude = list(SpatialFeatureForm.Meta.exclude)
        exclude.append('geometry_hash')
        exclude.append('conservation_score')

class LoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = LOI

class PoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = POI

