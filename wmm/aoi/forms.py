from madrona.features.forms import SpatialFeatureForm
from django import forms
from django.forms.widgets import *
from models import *

            
class AoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = AOI
        exclude = list(SpatialFeatureForm.Meta.exclude)
        #not sure why I get a form error when I include the following within a single exclude.append...
        exclude.append('geometry_hash')
        exclude.append('conservation_score')
        exclude.append('tidalenergy_score')
        exclude.append('waveenergy_score')
        exclude.append('windenergy_score')

