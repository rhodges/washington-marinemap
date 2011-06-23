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
    input_dist_shore = forms.FloatField(min_value=1, max_value=200, initial=10,
            widget=SliderWidget(min=1,max=200,step=1),
            label="Within distance of Shore (km)")
    input_dist_port = forms.FloatField(min_value=1, max_value=200, initial=10,
            widget=SliderWidget(min=1,max=200,step=1),
            label="Within distance of Port (km)")
    input_min_depth = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}))
    input_max_depth = forms.FloatField(initial=10, widget=forms.TextInput(attrs={'class':'slidervalue'}))
    # Dummy field to set both of the above
    input_depth = forms.FloatField(min_value=-2000, max_value=0, initial=0,
            widget=DualSliderWidget('input_min_depth','input_max_depth',
                                    min=-2000,max=0,step=1),
            label="Depth Range (meters)")
        
    class Meta(FeatureForm.Meta):
        model = Scenario
        exclude = list(FeatureForm.Meta.exclude)
        for f in model.output_fields():
            exclude.append(f.attname)
