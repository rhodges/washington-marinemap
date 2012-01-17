from lingcod.features.forms import FeatureForm, SpatialFeatureForm
from django import forms
from models import *


class SMPSiteForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = SMPSite
            