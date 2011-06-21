from lingcod.features.forms import FeatureForm, SpatialFeatureForm
from lingcod.analysistools.widgets import SliderWidget, DualSliderWidget
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import fromstr
from models import *

class FolderForm(FeatureForm):
    name = forms.CharField(label='Folder Name')
    class Meta(FeatureForm.Meta):
        model = Folder

class ScenarioForm(FeatureForm):
    input_dist_shore = forms.FloatField(min_value=0, max_value=1.0, initial=0.5,
            widget=SliderWidget(min=0,max=1,step=0.01),
            label="Distance From Shore")
    input_dist_port = forms.FloatField(min_value=0, max_value=1.0, initial=0.5,
            widget=SliderWidget(min=0,max=1,step=0.01),
            label="Distance From Port")
    input_min_depth = forms.FloatField(initial=0)
    input_max_depth = forms.FloatField(initial=1)
    # Dummy field to set both of the above
    input_depth = forms.FloatField(min_value=0, max_value=1.0, initial=0.5,
            widget=DualSliderWidget('input_min_depth','input_max_depth',
                                    min=0,max=1,step=0.01),
            label="Depth Range")
        
    class Meta(FeatureForm.Meta):
        model = Scenario
        exclude = list(FeatureForm.Meta.exclude)
        for f in model.output_fields():
            exclude.append(f.attname)
