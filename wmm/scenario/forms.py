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

class UserKmlForm(FeatureForm):
    class Meta(FeatureForm.Meta):
        model = UserKml

class SubstrateModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.substrate.name
        #return obj.name
        
'''        
class ScenarioForm(FeatureForm):
    #description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    #file = forms.FileField(widget=forms.ClearableFileInput(attrs={'style': 'top:0px;margin-bottom:0px'), max_length=70, required=False) #using ClearableFileInput produces poorly formatted edit form
    #support_file = ValidFileField(widget=AdminFileWidget,required=False,label="Support File")
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
    input_dist_port = forms.FloatField( min_value=0, max_value=100, initial=10,
                                        widget=SliderWidget(min=0,max=100,step=1),
                                        label="Within distance of Port (km)")
    input_min_depth = forms.FloatField(initial=-500, widget=forms.TextInput(attrs={'class':'slidervalue'}))
    input_max_depth = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}))
    # Dummy field to set both of the above
    input_depth = forms.FloatField( min_value=-1000, max_value=0, initial=0,
                                    widget=DualSliderWidget('input_min_depth','input_max_depth', min=-1000,max=0,step=10),
                                    label="Depth Range (meters)")
    input_substrate = ModelMultipleChoiceField( queryset=Substrate.objects.all().order_by('id'), 
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
        
class MOSForm(FeatureForm):
    #scenarios = forms.ModelChoiceField( queryset=Scenario.objectis.filter(
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)
    support_file = ValidFileField(widget=AdminFileWidget,required=False,label="Support File")
    #could optionally add a param similar to the following:  help_text="(e.g. a pdf or text document that explains this scenario)"
    
    input_categories = forms.ModelMultipleChoiceField(  queryset=Category.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'categories'}),
                                                        required=False,
                                                        label="")
    input_objectives = forms.ModelMultipleChoiceField(  queryset=Objective.objects.all().order_by('id'), 
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'objectives'}),
                                                        required=False, 
                                                        label="")
               
               
    # CATEGORY:  RENEWABLE ENERGY
    
    input_objectives_energy = forms.ModelMultipleChoiceField(   queryset=EnergyObjective.objects.all().order_by('id'), 
                                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'energy_objectives'}),
                                                                required=False, 
                                                                label="")
        
    # Objective 1 - Tidal Energy
    # NOTE:  The input parameters must be ordered by id 
    
    input_parameters_tidal_energy = forms.ModelMultipleChoiceField( queryset=TidalEnergyParameter.objects.all().order_by('id'),
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_tidal_energy'}),
                                                                    required=False, 
                                                                    #initial = Parameter.objects.filter(objectives=1),
                                                                    label="")
    input_dist_shore_tidal_energy = forms.FloatField(   min_value=0, max_value=20, initial=2,
                                                        widget=SliderWidget(min=0,max=20,step=.25),
                                                        label="Within distance of Shore (miles)", required=False)
    input_dist_port_tidal_energy = forms.FloatField(    min_value=0, max_value=50, initial=5,
                                                        widget=SliderWidget(min=0,max=50,step=.5),
                                                        label="Within distance of Port (miles)", required=False)
    input_min_depth_tidal_energy = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_tidal_energy = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_tidal_energy = forms.FloatField(min_value=0, max_value=5000, initial=0,
                                                widget=DualSliderWidget('input_min_depth_tidal_energy','input_max_depth_tidal_energy',
                                                                        min=0,max=5000,step=10),
                                                label="Depth Range (feet)", required=False)
    input_substrate_tidal_energy = ModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            widget=forms.CheckboxSelectMultiple(attrs={'class':'tidal_energy_substrate_checkboxes'}),
                                                            label="Include areas with the following Substrate Types", required=False) 
    input_min_tidalmean_tidal_energy = forms.FloatField(initial=200, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_tidalmean_tidal_energy = forms.FloatField(initial=1200, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_tidalmean_tidal_energy = forms.FloatField(min_value=0, max_value=1750, initial=0,
                                                    widget=DualSliderWidget('input_min_tidalmean_tidal_energy','input_max_tidalmean_tidal_energy',
                                                                            min=0,max=1750,step=50),
                                                    label="Mean Tidal Energy (W/m2)", required=False)
    input_min_tidalmax_tidal_energy = forms.FloatField(initial=3000, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_tidalmax_tidal_energy = forms.FloatField(initial=13000, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_tidalmax_tidal_energy = forms.FloatField( min_value=0, max_value=15000, initial=0,
                                                    widget=DualSliderWidget('input_min_tidalmax_tidal_energy','input_max_tidalmax_tidal_energy',
                                                                            min=0,max=15000,step=500),
                                                    label="Max Tidal Energy (W/m2)", required=False)
    
    # Objective 7 - Wave Energy
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_wave_energy = forms.ModelMultipleChoiceField(  queryset=WaveEnergyParameter.objects.all().order_by('id'),
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_wave_energy'}),
                                                                    required=False, 
                                                                    #initial = Parameter.objects.filter(objectives=2),
                                                                    label="")
    input_dist_shore_wave_energy = forms.FloatField(min_value=0, max_value=20, initial=2,
                                                    widget=SliderWidget(min=0,max=20,step=.25),
                                                    label="Within distance of Shore (miles)", required=False)
    input_dist_port_wave_energy = forms.FloatField( min_value=0, max_value=50, initial=5,
                                                    widget=SliderWidget(min=0,max=50,step=.5),
                                                    label="Within distance of Port (miles)", required=False)
    input_min_depth_wave_energy = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_wave_energy = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_wave_energy = forms.FloatField( min_value=0, max_value=5000, initial=0,
                                                widget=DualSliderWidget('input_min_depth_wave_energy','input_max_depth_wave_energy',min=0,max=5000,step=10),
                                                label="Depth Range (feet)", required=False)
    input_substrate_wave_energy = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                widget=forms.CheckboxSelectMultiple(attrs={'class':'wave_energy_substrate_checkboxes'}),
                                                                label="Include areas with the following Substrate Types", required=False) 
    input_min_wavesummer_wave_energy = forms.FloatField(initial=15, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_wavesummer_wave_energy = forms.FloatField(initial=20, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_wavesummer_wave_energy = forms.FloatField(min_value=0, max_value=25, initial=0,
                                                    widget=DualSliderWidget('input_min_wavesummer_wave_energy','input_max_wavesummer_wave_energy',
                                                                            min=0,max=25,step=1),
                                                    label="Summer Wave Energy (kW/m of shoreline)", required=False)
    input_min_wavewinter_wave_energy = forms.FloatField(initial=45, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_wavewinter_wave_energy = forms.FloatField(initial=65, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_wavewinter_wave_energy = forms.FloatField(min_value=0, max_value=76, initial=0,
                                                    widget=DualSliderWidget('input_min_wavewinter_wave_energy','input_max_wavewinter_wave_energy',
                                                                            min=0,max=76,step=1),
                                                    label="Winter Wave Energy (kW/m of shoreline)", required=False)
    
    # Objective 2 - Wind Energy
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_wind_energy = forms.ModelMultipleChoiceField(  queryset=WindEnergyParameter.objects.all().order_by('id'),
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_wind_energy'}),
                                                                    required=False, 
                                                                    #initial = Parameter.objects.filter(objectives=2),
                                                                    label="")
    input_dist_shore_wind_energy = forms.FloatField(min_value=0, max_value=20, initial=2,
                                                    widget=SliderWidget(min=0,max=20,step=.25),
                                                    label="Within distance of Shore (miles)", required=False)
    input_dist_port_wind_energy = forms.FloatField( min_value=0, max_value=50, initial=5,
                                                    widget=SliderWidget(min=0,max=50,step=.5),
                                                    label="Within distance of Port (miles)", required=False)
    input_min_depth_wind_energy = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_wind_energy = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_wind_energy = forms.FloatField( min_value=0, max_value=5000, initial=0,
                                                widget=DualSliderWidget('input_min_depth_wind_energy','input_max_depth_wind_energy',min=0,max=5000,step=10),
                                                label="Depth Range (feet)", required=False)
    input_substrate_wind_energy = ModelMultipleChoiceField( queryset=Substrate.objects.all().order_by('id'), 
                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            widget=forms.CheckboxSelectMultiple(attrs={'class':'wind_energy_substrate_checkboxes'}),
                                                            required=False) 
    input_wind_potential_wind_energy = ModelMultipleChoiceField(queryset=WindPotential.objects.all().order_by('id'), 
                                                                #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                widget=forms.CheckboxSelectMultiple(attrs={'class':'wind_energy_wind_potential_checkboxes'}),
                                                                required=False) 
    
    
    # CATEGORY:  CONSERVATION 
    
    input_objectives_conservation = forms.ModelMultipleChoiceField( queryset=ConservationObjective.objects.all().order_by('id'), 
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'conservation_objectives'}),
                                                                    required=False, 
                                                                    label="")
                                     
    # Objective 3 - Offshore Conservation (Benthic)
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_offshore_conservation = forms.ModelMultipleChoiceField(queryset=OffshoreConservationParameter.objects.all().order_by('id'),
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_offshore_conservation'}),
                                                                            required=False, 
                                                                            #initial = Parameter.objects.filter(objectives=3),
                                                                            label="")
    input_substrate_offshore_conservation = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(attrs={'class':'offshore_conservation_substrate_checkboxes'}),
                                                                        label="Include the following Substrate Types", required=False) 
    input_depth_class_offshore_conservation = ModelMultipleChoiceField( queryset=DepthClass.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':4}), initial="1",
                                                                        widget=forms.CheckboxSelectMultiple(attrs={'class':'offshore_conservation_depth_class_checkboxes'}),
                                                                        label="Include the following Depth Classes", required=False)     
    input_geomorphology_offshore_conservation = ModelMultipleChoiceField(   queryset=Geomorphology.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':4}), initial="1",
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class':'offshore_conservation_geomorphology_checkboxes'}),
                                                                            label="Include the following Geomorphologies", required=False)     
    
    # Objective 8 - Nearshore Conservation
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_nearshore_conservation = forms.ModelMultipleChoiceField(   queryset=NearshoreConservationParameter.objects.all().order_by('id'),
                                                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_nearshore_conservation'}),
                                                                                required=False, 
                                                                                #initial = Parameter.objects.filter(objectives=3),
                                                                                label="")
    input_substrate_nearshore_conservation = ModelMultipleChoiceField(  queryset=NearshoreSubstrate.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(attrs={'class':'nearshore_conservation_substrate_checkboxes'}),
                                                                        required=False) 
    input_exposure_nearshore_conservation = ModelMultipleChoiceField(  queryset=NearshoreExposure.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(attrs={'class':'nearshore_conservation_exposure_checkboxes'}),
                                                                        required=False) 
    input_ecosystem_nearshore_conservation = ModelMultipleChoiceField(  queryset=NearshoreEcosystem.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(attrs={'class':'nearshore_conservation_ecosystem_checkboxes'}),
                                                                        required=False) 
    
    
    # Objective 9 - Water Column Conservation (Pelagic)
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_water_column_conservation = forms.ModelMultipleChoiceField(queryset=WaterColumnConservationParameter.objects.all().order_by('id'),
                                                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_water_column_conservation'}),
                                                                                required=False, 
                                                                                #initial = Parameter.objects.filter(objectives=3),
                                                                                label="")
    input_upwelling_water_column_conservation = ModelMultipleChoiceField(   queryset=Upwelling.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class':'water_column_conservation_upwelling_checkboxes'}),
                                                                            required=False) 
    input_chlorophyl_water_column_conservation = ModelMultipleChoiceField(  queryset=Chlorophyl.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class':'water_column_conservation_chlorophyl_checkboxes'}),
                                                                            required=False) 
                  
    
    def save(self, commit=True):
        inst = super(FeatureForm, self).save(commit=False)
        if self.data.get('clear_support_file'):
            inst.support_file = None
        if commit:
            inst.save()
        return inst
    
    class Meta(FeatureForm.Meta):
        model = MOS
        exclude = list(FeatureForm.Meta.exclude)
        exclude.append('scenarios')

