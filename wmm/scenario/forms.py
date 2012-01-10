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
            
class SMPSiteForm(SpatialFeatureForm):
    class Meta(SpatialFeatureForm.Meta):
        model = SMPSite
            
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
    # Dummy field to set both of the above
    input_depth_tidal_energy = forms.FloatField(min_value=0, max_value=5000, initial=0,
                                                widget=DualSliderWidget('input_min_depth_tidal_energy','input_max_depth_tidal_energy',min=0,max=5000,step=10),
                                                label="Depth Range (feet)", required=False)
    input_substrate_tidal_energy = ModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'substrate_tidal_energy'}),
                                                            label="Include areas with the following Substrate Types", required=False) 
                                                       
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
                                                                widget=forms.CheckboxSelectMultiple(),
                                                                label="Include areas with the following Substrate Types", required=False) 
                                                                                                          
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
    input_substrate_wind_energy = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                widget=forms.CheckboxSelectMultiple(),
                                                                label="Include areas with the following Substrate Types", required=False) 
               
    
    
    # CATEGORY:  CONSERVATION 
    input_objectives_conservation = forms.ModelMultipleChoiceField( queryset=ConservationObjective.objects.all().order_by('id'), 
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'conservation_objectives'}),
                                                                    required=False, 
                                                                    label="")
                                     
    # Objective 3 - Offshore Conservation
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_offshore_conservation = forms.ModelMultipleChoiceField(queryset=OffshoreConservationParameter.objects.all().order_by('id'),
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_offshore_conservation'}),
                                                                            required=False, 
                                                                            #initial = Parameter.objects.filter(objectives=3),
                                                                            label="")
    input_dist_shore_offshore_conservation = forms.FloatField(  min_value=0, max_value=20, initial=2,
                                                                widget=SliderWidget(min=0,max=20,step=.25),
                                                                label="Within distance of Shore (miles)", required=False)
    input_dist_port_offshore_conservation = forms.FloatField(   min_value=0, max_value=50, initial=5,
                                                                widget=SliderWidget(min=0,max=50,step=.5),
                                                                label="Within distance of Port (miles)", required=False)
    input_min_depth_offshore_conservation = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_offshore_conservation = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_offshore_conservation = forms.FloatField(   min_value=0, max_value=5000, initial=0,
                                                            widget=DualSliderWidget('input_min_depth_offshore_conservation','input_max_depth_offshore_conservation',min=0,max=5000,step=10),
                                                            label="Depth Range (feet)", required=False)
    input_substrate_offshore_conservation = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(),
                                                                        label="Include areas with the following Substrate Types", required=False) 
    input_depth_class_offshore_conservation = ModelMultipleChoiceField( queryset=DepthClass.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':4}), initial="1",
                                                                        widget=forms.CheckboxSelectMultiple(),
                                                                        label="Include areas with the following Depth Classes", required=False)     
    input_geomorphology_offshore_conservation = ModelMultipleChoiceField(   queryset=Geomorphology.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':4}), initial="1",
                                                                            widget=forms.CheckboxSelectMultiple(),
                                                                            label="Include areas with the following Geomorphologies", required=False)     
    
    # Objective 8 - Nearshore Conservation
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_nearshore_conservation = forms.ModelMultipleChoiceField(   queryset=NearshoreConservationParameter.objects.all().order_by('id'),
                                                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_nearshore_conservation'}),
                                                                                required=False, 
                                                                                #initial = Parameter.objects.filter(objectives=3),
                                                                                label="")
    input_dist_shore_nearshore_conservation = forms.FloatField( min_value=0, max_value=20, initial=2,
                                                                widget=SliderWidget(min=0,max=20,step=.25),
                                                                label="Within distance of Shore (miles)", required=False)
    input_dist_port_nearshore_conservation = forms.FloatField(  min_value=0, max_value=50, initial=5,
                                                                widget=SliderWidget(min=0,max=50,step=.5),
                                                                label="Within distance of Port (miles)", required=False)
    input_min_depth_nearshore_conservation = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_nearshore_conservation = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_nearshore_conservation = forms.FloatField(  min_value=0, max_value=5000, initial=0,
                                                            widget=DualSliderWidget('input_min_depth_nearshore_conservation','input_max_depth_nearshore_conservation',min=0,max=5000,step=10),
                                                            label="Depth Range (feet)", required=False)
    input_substrate_nearshore_conservation = ModelMultipleChoiceField(  queryset=NearshoreSubstrate.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(),
                                                                        label="Include areas with the following Substrate Types", required=False) 
                                                                                 
    # Objective 9 - Water Column Conservation
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_water_column_conservation = forms.ModelMultipleChoiceField(queryset=WaterColumnConservationParameter.objects.all().order_by('id'),
                                                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_water_column_conservation'}),
                                                                                required=False, 
                                                                                #initial = Parameter.objects.filter(objectives=3),
                                                                                label="")
    input_dist_shore_water_column_conservation = forms.FloatField(  min_value=0, max_value=20, initial=2,
                                                                    widget=SliderWidget(min=0,max=20,step=.25),
                                                                    label="Within distance of Shore (miles)", required=False)
    input_dist_port_water_column_conservation = forms.FloatField(   min_value=0, max_value=50, initial=5,
                                                                    widget=SliderWidget(min=0,max=50,step=.5),
                                                                    label="Within distance of Port (miles)", required=False)
    input_min_depth_water_column_conservation = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_water_column_conservation = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_water_column_conservation = forms.FloatField(   min_value=0, max_value=5000, initial=0,
                                                                widget=DualSliderWidget('input_min_depth_water_column_conservation','input_max_depth_water_column_conservation',min=0,max=5000,step=10),
                                                                label="Depth Range (feet)", required=False)
    input_substrate_water_column_conservation = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                            widget=forms.CheckboxSelectMultiple(),
                                                                            label="Include areas with the following Substrate Types", required=False) 
    input_upwelling_water_column_conservation = ModelMultipleChoiceField(   queryset=Upwelling.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                            widget=forms.CheckboxSelectMultiple(),
                                                                            label="Include areas with the following Upwelling Classes", required=False) 
    input_chlorophyl_water_column_conservation = ModelMultipleChoiceField(  queryset=Chlorophyl.objects.all().order_by('id'), 
                                                                            #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                            widget=forms.CheckboxSelectMultiple(),
                                                                            label="Include areas with the following Chlorophyl Classes", required=False) 
                  
        
    # CATEGORY:  DEVELOPMENT 
    input_objectives_development = forms.ModelMultipleChoiceField(  queryset=DevelopmentObjective.objects.all().order_by('id'), 
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'development_objectives'}),
                                                                    required=False, 
                                                                    label="")
                                                                     
    # Objective 4 - Shoreside Development
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_shoreside_development = forms.ModelMultipleChoiceField(queryset=ShoresideDevelopmentParameter.objects.all().order_by('id'),
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_shoreside_development'}),
                                                                            required=False, 
                                                                            #initial = Parameter.objects.filter(objectives=4),
                                                                            label="")
    input_dist_shore_shoreside_development = forms.FloatField(  min_value=0, max_value=20, initial=2,
                                                                widget=SliderWidget(min=0,max=20,step=.25),
                                                                label="Within distance of Shore (miles)", required=False)
    input_dist_port_shoreside_development = forms.FloatField(   min_value=0, max_value=50, initial=5,
                                                                widget=SliderWidget(min=0,max=50,step=.5),
                                                                label="Within distance of Port (miles)", required=False)
    input_min_depth_shoreside_development = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_shoreside_development = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_shoreside_development = forms.FloatField(   min_value=0, max_value=5000, initial=0,
                                                            widget=DualSliderWidget('input_min_depth_shoreside_development','input_max_depth_shoreside_development',min=0,max=5000,step=10),
                                                            label="Depth Range (feet)", required=False)
    input_substrate_shoreside_development = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(),
                                                                        label="Include areas with the following Substrate Types", required=False) 
                
                
    # CATEGORY:  FISHERIES 
    input_objectives_fisheries = forms.ModelMultipleChoiceField(    queryset=FisheriesObjective.objects.all().order_by('id'), 
                                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'fisheries_objectives'}),
                                                                    required=False, 
                                                                    label="")
                                                       
    # Objective 5 - Shellfish Aquaculture
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_shellfish_aquaculture = forms.ModelMultipleChoiceField(queryset=ShellfishAquacultureParameter.objects.all().order_by('id'),
                                                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_shellfish_aquaculture'}),
                                                                            required=False, 
                                                                            #initial = Parameter.objects.filter(objectives=5),
                                                                            label="")
    input_dist_shore_shellfish_aquaculture = forms.FloatField(  min_value=0, max_value=20, initial=2,
                                                                widget=SliderWidget(min=0,max=20,step=.25),
                                                                label="Within distance of Shore (miles)", required=False)
    input_dist_port_shellfish_aquaculture = forms.FloatField(   min_value=0, max_value=50, initial=5,
                                                                widget=SliderWidget(min=0,max=50,step=.5),
                                                                label="Within distance of Port (miles)", required=False)
    input_min_depth_shellfish_aquaculture = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_shellfish_aquaculture = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_shellfish_aquaculture = forms.FloatField(   min_value=0, max_value=5000, initial=0,
                                                            widget=DualSliderWidget('input_min_depth_shellfish_aquaculture','input_max_depth_shellfish_aquaculture',min=0,max=5000,step=10),
                                                            label="Depth Range (feet)", required=False)
    input_substrate_shellfish_aquaculture = ModelMultipleChoiceField(   queryset=Substrate.objects.all().order_by('id'), 
                                                                        #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                        widget=forms.CheckboxSelectMultiple(),
                                                                        label="Include areas with the following Substrate Types", required=False)  
                                                        
    # Objective 6 - Offshore Fishing
    # NOTE:  The input parameters must be ordered by id 
    input_parameters_offshore_fishing = forms.ModelMultipleChoiceField(queryset=OffshoreFishingParameter.objects.all().order_by('id'),
                                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'parameters_offshore_fishing'}),
                                                        required=False, 
                                                        #initial = Parameter.objects.filter(objectives=6),
                                                        label="")
    input_dist_shore_offshore_fishing = forms.FloatField(min_value=0, max_value=20, initial=2,
                                                widget=SliderWidget(min=0,max=20,step=.25),
                                                label="Within distance of Shore (miles)", required=False)
    input_dist_port_offshore_fishing = forms.FloatField( min_value=0, max_value=50, initial=5,
                                                widget=SliderWidget(min=0,max=50,step=.5),
                                                label="Within distance of Port (miles)", required=False)
    input_min_depth_offshore_fishing = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_max_depth_offshore_fishing = forms.FloatField(initial=500, widget=forms.TextInput(attrs={'class':'slidervalue'}), required=False)
    input_depth_offshore_fishing = forms.FloatField( min_value=0, max_value=5000, initial=0,
                                            widget=DualSliderWidget('input_min_depth_offshore_fishing','input_max_depth_offshore_fishing',min=0,max=5000,step=10),
                                            label="Depth Range (feet)", required=False)
    input_substrate_offshore_fishing = ModelMultipleChoiceField(queryset=Substrate.objects.all().order_by('id'), 
                                                                #widget=forms.SelectMultiple(attrs={'size':6}), initial="3",
                                                                widget=forms.CheckboxSelectMultiple(),
                                                                label="Include areas with the following Substrate Types", required=False) 
    
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

