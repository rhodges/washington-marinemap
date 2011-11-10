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

class FolderForm(FeatureForm):
    name = forms.CharField(label='Folder Name')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    class Meta(FeatureForm.Meta):
        model = Folder

class SubstrateModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name
        
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

class MultiObjectiveScenarioForm(FeatureForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    support_file = ValidFileField(widget=AdminFileWidget,required=False,label="Support File")
        #could optionally add a param similar to the following:  help_text="(e.g. a pdf or text document that explains this scenario)"
    
    input_objectives = forms.ModelMultipleChoiceField(  queryset=Objective.objects.all().order_by('id'), 
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'objectives'}),
                                                        required=False, 
                                                        label="")
    
                                                       
    # Objective 1
    input_parameters_1 = forms.ModelMultipleChoiceField(queryset=Parameter.objects.filter(objectives=1),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_1'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=1),
                                                        label="")
    input_dist_shore_1 = forms.FloatField(min_value=0, max_value=40, initial=5,
                                        widget=SliderWidget(min=0,max=40,step=.5),
                                        label="Within distance of Shore (km)", required=False)
    input_dist_port_1 = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)", required=False)
    input_min_depth_1 = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_1 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_1 = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth_1','input_max_depth_1',
                                                            min=-1000,max=0,step=10),
                                    label="Depth Range (meters)", required=False)
    input_substrate_1 = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 2
    input_parameters_2 = forms.ModelMultipleChoiceField(queryset=Parameter.objects.filter(objectives=2),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_2'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=2),
                                                        label="")
    input_dist_shore_2 = forms.FloatField(min_value=0, max_value=40, initial=5,
                                        widget=SliderWidget(min=0,max=40,step=.5),
                                        label="Within distance of Shore (km)", required=False)
    input_dist_port_2 = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)", required=False)
    input_min_depth_2 = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_2 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_2 = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth_2','input_max_depth_2',
                                                            min=-1000,max=0,step=10),
                                    label="Depth Range (meters)", required=False)
    input_substrate_2 = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 3
    input_parameters_3 = forms.ModelMultipleChoiceField(queryset=Parameter.objects.filter(objectives=3),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_3'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=3),
                                                        label="")
    input_dist_shore_3 = forms.FloatField(min_value=0, max_value=40, initial=5,
                                        widget=SliderWidget(min=0,max=40,step=.5),
                                        label="Within distance of Shore (km)", required=False)
    input_dist_port_3 = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)", required=False)
    input_min_depth_3 = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_3 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_3 = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth_3','input_max_depth_3',
                                                            min=-1000,max=0,step=10),
                                    label="Depth Range (meters)", required=False)
    input_substrate_3 = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 4
    input_parameters_4 = forms.ModelMultipleChoiceField(queryset=Parameter.objects.filter(objectives=4),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_4'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=4),
                                                        label="")
    input_dist_shore_4 = forms.FloatField(min_value=0, max_value=40, initial=5,
                                        widget=SliderWidget(min=0,max=40,step=.5),
                                        label="Within distance of Shore (km)", required=False)
    input_dist_port_4 = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)", required=False)
    input_min_depth_4 = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_4 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_4 = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth_4','input_max_depth_4',
                                                            min=-1000,max=0,step=10),
                                    label="Depth Range (meters)", required=False)
    input_substrate_4 = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types", required=False) 
                                                        
    # Objective 5
    input_parameters_5 = forms.ModelMultipleChoiceField(queryset=Parameter.objects.filter(objectives=5),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_5'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=5),
                                                        label="")
    input_dist_shore_5 = forms.FloatField(min_value=0, max_value=40, initial=5,
                                        widget=SliderWidget(min=0,max=40,step=.5),
                                        label="Within distance of Shore (km)", required=False)
    input_dist_port_5 = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)", required=False)
    input_min_depth_5 = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_5 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_5 = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth_5','input_max_depth_5',
                                                            min=-1000,max=0,step=10),
                                    label="Depth Range (meters)", required=False)
    input_substrate_5 = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types", required=False)  
                                                        
    # Objective 6
    input_parameters_6 = forms.ModelMultipleChoiceField(queryset=Parameter.objects.filter(objectives=6),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_6'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=6),
                                                        label="")
    input_dist_shore_6 = forms.FloatField(min_value=0, max_value=40, initial=5,
                                        widget=SliderWidget(min=0,max=40,step=.5),
                                        label="Within distance of Shore (km)", required=False)
    input_dist_port_6 = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)", required=False)
    input_min_depth_6 = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_6 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    # Dummy field to set both of the above
    input_depth_6 = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth_6','input_max_depth_6',
                                                            min=-1000,max=0,step=10),
                                    label="Depth Range (meters)", required=False)
    input_substrate_6 = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types", required=False) 
    
    '''
    input_widgets = {}
    for i in range(6):
        i += 1
        input_widgets['input_dist_shore_%s'%i] = forms.FloatField(  min_value=0, max_value=40, initial=5,
                                                                    widget=SliderWidget(min=0,max=40,step=.5),
                                                                    label="Within distance of Shore (km)")
        input_widgets['input_dist_port_%s'%i] = forms.FloatField(   min_value=0, max_value=100, initial=10,
                                                                    widget=SliderWidget(min=0,max=100,step=1),
                                                                    label="Within distance of Port (km)")
        input_widgets['input_min_depth_%s'%i] = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}))
        input_widgets['input_max_depth_%s'%i] = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}))
        input_widgets['input_depth_%s'%i] = forms.FloatField(   min_value=-1000, max_value=0, initial=0,
                                                                widget=DualSliderWidget('input_min_depth','input_max_depth',
                                                                                        min=-1000,max=0,step=10),
                                                                label="Depth Range (meters)")
        input_widgest['input_substrate%s'%i] = SubstrateModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                        widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                        label="Include areas with the following Substrate Types") 
    '''
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
