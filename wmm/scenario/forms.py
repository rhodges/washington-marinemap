from lingcod.features.forms import FeatureForm, SpatialFeatureForm
from lingcod.analysistools.widgets import SliderWidget, DualSliderWidget
from django import forms
from django.forms import ModelMultipleChoiceField
from django.forms.widgets import *
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import fromstr
from models import *
from os.path import splitext,split

class ConservationSiteForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = ConservationSite
            
class WindEnergySiteForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = WindEnergySite
            
class AoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = AOI

class LoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = LOI

class PoiForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = POI

class UserKmlForm(FeatureForm):
    class Meta(FeatureForm.Meta):
        model = UserKml

class FolderForm(FeatureForm):
    name = forms.CharField(label='Folder Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    class Meta(FeatureForm.Meta):
        model = Folder

class SubstrateModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.substrate.name
        
'''        
class ScenarioForm(FeatureForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    #file = forms.FileField(widget=forms.ClearableFileInput(attrs={'style': 'top:0px;margin-bottom:0px'), max_length=70, required=False) #using ClearableFileInput produces poorly formatted edit form
    support_file = ValidFileField(widget=AdminFileWidget,required=False,label="Support File")
        #could optionally add a param similar to the following:  help_text="(e.g. a pdf or text document that explains this scenario)"
    input_objective = forms.ModelChoiceField(   queryset=Objective.objects.all().order_by('id'), 
                                                widget=forms.RadioSelect(attrs={'class': 'objectives'}),
                                                required=False, 
                                                label="")
    input_parameters = forms.ModelMultipleChoiceField(  queryset=Parameter.objects.all(),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.all(),
                                                        label="")
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
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types") 
   
    def save(self, commit=True):
        inst = super(FeatureForm, self).save(commit=False)
        if self.data.get('clear_support_file'):
            inst.support_file = None
        if commit:
            inst.save()
        return inst
    
    class Meta(FeatureForm.Meta):
        model = Scenario
        exclude = list(FeatureForm.Meta.exclude)
        for f in model.output_fields():
            exclude.append(f.attname)
'''

class AdminFileWidget(forms.FileInput):
    """
    A FileField Widget that shows its current value if it has one.
    """
    def __init__(self, attrs={}):
        super(AdminFileWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = ['<p>']
        if value and hasattr(value, "name"):
            filename = split(value.name)[-1]
            output.append('Current File: <a href="%s" target="_blank">%s</a> : <input style="top:0px;margin-bottom:0px" type="checkbox" name="clear_%s" /> Remove </p>' % (value._get_url(), filename, name))
            output.append('<p> Change:') 
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        output.append("</p>")
        return mark_safe(u''.join(output))
 
# http://www.neverfriday.com/sweetfriday/2008/09/-a-long-time-ago.html
class FileValidationError(forms.ValidationError):
    def __init__(self):
        super(FileValidationError, self).__init__('Document types accepted: ' + ', '.join(ValidFileField.valid_file_extensions))
        
class ValidFileField(forms.FileField):
    """A validating document upload field"""
    valid_file_extensions = ['odt', 'pdf', 'doc', 'xls', 'txt', 'csv', 'kml', 'kmz', 'jpeg', 'jpg', 'png', 'gif', 'zip']

    def __init__(self, *args, **kwargs):
        super(ValidFileField, self).__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        f = super(ValidFileField, self).clean(data, initial)
        if f:
            ext = splitext(f.name)[1][1:].lower()
            if ext in ValidFileField.valid_file_extensions: 
                # check data['content-type'] ?
                return f
            raise FileValidationError()
        
class MultiObjectiveScenarioForm(FeatureForm):
    #scenarios = forms.ModelChoiceField( queryset=Scenario.objectis.filter(
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    support_file = ValidFileField(widget=AdminFileWidget,required=False,label="Support File")
        #could optionally add a param similar to the following:  help_text="(e.g. a pdf or text document that explains this scenario)"
    
    input_objectives = forms.ModelMultipleChoiceField(  queryset=Objective.objects.all().order_by('id'), 
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'objectives'}),
                                                        required=False, 
                                                        label="")
    
    # Objective 1 - Tidal Energy
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_tidal = forms.ModelMultipleChoiceField(queryset=TidalParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_tidal'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=1),
                                                        label="")
    input_dist_shore_tidal = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                            widget=SliderWidget(min=0,max=40,step=.5),
                                            label="Within distance of Shore (km)", required=False)
    input_dist_port_tidal = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                            widget=SliderWidget(min=0,max=100,step=1),
                                            label="Within distance of Port (km)", required=False)
    input_min_depth_tidal = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_tidal = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_tidal = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                        widget=DualSliderWidget('input_min_depth_tidal','input_max_depth_tidal',
                                                                min=-1000,max=0,step=10),
                                        label="Depth Range (meters)", required=False)
    input_substrate_tidal = SubstrateModelMultipleChoiceField(  queryset=TidalSubstrate.objects.all().order_by('id'), 
                                                            widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 2 - Wind Energy
    input_parameters_wind = forms.ModelMultipleChoiceField(queryset=WindParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_wind'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=2),
                                                        label="")
    input_dist_shore_wind = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                            widget=SliderWidget(min=0,max=40,step=.5),
                                            label="Within distance of Shore (km)", required=False)
    input_dist_port_wind = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                            widget=SliderWidget(min=0,max=100,step=1),
                                            label="Within distance of Port (km)", required=False)
    input_min_depth_wind = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_wind = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_wind = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                        widget=DualSliderWidget('input_min_depth_wind','input_max_depth_wind',
                                                                min=-1000,max=0,step=10),
                                        label="Depth Range (meters)", required=False)
    input_substrate_wind = SubstrateModelMultipleChoiceField(  queryset=WindSubstrate.objects.all().order_by('id'), 
                                                            widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 3 - Marine Conservation
    input_parameters_conservation = forms.ModelMultipleChoiceField(queryset=ConservationParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_conservation'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=3),
                                                        label="")
    input_dist_shore_conservation = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                            widget=SliderWidget(min=0,max=40,step=.5),
                                            label="Within distance of Shore (km)", required=False)
    input_dist_port_conservation = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                            widget=SliderWidget(min=0,max=100,step=1),
                                            label="Within distance of Port (km)", required=False)
    input_min_depth_conservation = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_conservation = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_conservation = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                        widget=DualSliderWidget('input_min_depth_conservation','input_max_depth_conservation',
                                                                min=-1000,max=0,step=10),
                                        label="Depth Range (meters)", required=False)
    input_substrate_conservation = SubstrateModelMultipleChoiceField(  queryset=ConservationSubstrate.objects.all().order_by('id'), 
                                                            widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 4 - Shoreside Development
    input_parameters_development = forms.ModelMultipleChoiceField(queryset=DevelopmentParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_development'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=4),
                                                        label="")
    input_dist_shore_development = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                            widget=SliderWidget(min=0,max=40,step=.5),
                                            label="Within distance of Shore (km)", required=False)
    input_dist_port_4 = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                            widget=SliderWidget(min=0,max=100,step=1),
                                            label="Within distance of Port (km)", required=False)
    input_min_depth_development = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_development = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_development = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                        widget=DualSliderWidget('input_min_depth_development','input_max_depth_development',
                                                                min=-1000,max=0,step=10),
                                        label="Depth Range (meters)", required=False)
    input_substrate_development = SubstrateModelMultipleChoiceField(  queryset=DevelopmentSubstrate.objects.all().order_by('id'), 
                                                            widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 5 - Shellfish Aquaculture
    input_parameters_shellfish = forms.ModelMultipleChoiceField(queryset=ShellfishParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_shellfish'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=5),
                                                        label="")
    input_dist_shore_shellfish = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                            widget=SliderWidget(min=0,max=40,step=.5),
                                            label="Within distance of Shore (km)", required=False)
    input_dist_port_shellfish = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                            widget=SliderWidget(min=0,max=100,step=1),
                                            label="Within distance of Port (km)", required=False)
    input_min_depth_shellfish = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_shellfish = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_shellfish = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                        widget=DualSliderWidget('input_min_depth_shellfish','input_max_depth_shellfish',
                                                                min=-1000,max=0,step=10),
                                        label="Depth Range (meters)", required=False)
    input_substrate_shellfish = SubstrateModelMultipleChoiceField(  queryset=ShellfishSubstrate.objects.all().order_by('id'), 
                                                            widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            label="Include areas with the following Substrate Types", required=False)  
                                                        
    # Objective 6 - Offshore Fishing
    input_parameters_fishing = forms.ModelMultipleChoiceField(queryset=FishingParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_fishing'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=6),
                                                        label="")
    input_dist_shore_fishing = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                            widget=SliderWidget(min=0,max=40,step=.5),
                                            label="Within distance of Shore (km)", required=False)
    input_dist_port_fishing = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                            widget=SliderWidget(min=0,max=100,step=1),
                                            label="Within distance of Port (km)", required=False)
    input_min_depth_fishing = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_fishing = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_fishing = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                        widget=DualSliderWidget('input_min_depth_fishing','input_max_depth_fishing',
                                                                min=-1000,max=0,step=10),
                                        label="Depth Range (meters)", required=False)
    input_substrate_fishing = SubstrateModelMultipleChoiceField(  queryset=FishingSubstrate.objects.all().order_by('id'), 
                                                            widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            label="Include areas with the following Substrate Types", required=False) 
    
    def save(self, commit=True):
        inst = super(FeatureForm, self).save(commit=False)
        if self.data.get('clear_support_file'):
            inst.support_file = None
        if commit:
            inst.save()
        return inst
    
    class Meta(FeatureForm.Meta):
        model = MultiObjectiveScenario
        exclude = list(FeatureForm.Meta.exclude)
        exclude.append('scenarios')

