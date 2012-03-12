from madrona.features.forms import FeatureForm, SpatialFeatureForm
from django import forms
from models import *


class SMPSiteForm(SpatialFeatureForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    
    class Meta(SpatialFeatureForm.Meta):
        model = SMPSite
        exclude = list(SpatialFeatureForm.Meta.exclude)
        #not sure why I get a form error when I include the following within a single exclude.append...
        exclude.append('geometry_hash')
        exclude.append('conservation_score')
        exclude.append('tidalenergy_score')
        exclude.append('waveenergy_score')
        exclude.append('windenergy_score')
            