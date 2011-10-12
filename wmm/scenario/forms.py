from lingcod.features.forms import FeatureForm, SpatialFeatureForm
from lingcod.analysistools.widgets import SliderWidget, DualSliderWidget
from django import forms
from django.forms import ModelMultipleChoiceField
from django.forms.widgets import *
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import fromstr
from models import *

class FolderForm(FeatureForm):
    name = forms.CharField(label='Folder Name')
    class Meta(FeatureForm.Meta):
        model = Folder

class SubstrateModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name
            
class ScenarioForm(FeatureForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    input_dist_shore = forms.FloatField(min_value=0, max_value=40, initial=5,
            widget=SliderWidget(min=0,max=40,step=.5),
            label="Within distance of Shore (km)")
    input_dist_port = forms.FloatField(min_value=0, max_value=100, initial=10,
            widget=SliderWidget(min=0,max=100,step=1),
            label="Within distance of Port (km)")
    input_min_depth = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}))
    input_max_depth = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}))
    # Dummy field to set both of the above
    input_depth = forms.FloatField(min_value=-1000, max_value=0, initial=0,
            widget=DualSliderWidget('input_min_depth','input_max_depth',
                                    min=-1000,max=0,step=10),
            label="Depth Range (meters)")
    input_substrate = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), 
                                                        label="Include areas with the following substrates")    
        
    class Meta(FeatureForm.Meta):
        model = Scenario
        exclude = list(FeatureForm.Meta.exclude)
        for f in model.output_fields():
            exclude.append(f.attname)

class LoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = LOI

class PoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = POI

class AoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = AOI

class UserKmlForm(FeatureForm):
    class Meta(FeatureForm.Meta):
        model = UserKml

