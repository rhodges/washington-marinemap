from django import forms
from django.forms.widgets import *
from django.utils.safestring import mark_safe
from madrona.analysistools.widgets import SliderWidget, DualSliderWidget
from os.path import splitext,split

class AdminFileWidget(forms.FileInput):
    """
    A FileField Widget that shows its current value if it has one.
    """
    def __init__(self, attrs={}):
        super(AdminFileWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "name"):
            filename = split(value.name)[-1]
            output.append('Current File: <a href="%s" target="_blank">%s</a> : <input style="top:0px;margin-bottom:0px" type="checkbox" name="clear_%s" /> Remove </p>' % (value._get_url(), filename, name))
            output.append('<p> Change:') 
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        #output.append("</p>")
        return mark_safe(u''.join(output))
  
class CheckboxSelectMultipleWithObjTooltip(forms.CheckboxSelectMultiple):
    def __init__(self, queryset=None, attrs=None):
        super(CheckboxSelectMultipleWithObjTooltip, self).__init__(attrs)
        self.queryset = queryset
        self.attrs = attrs

    def render(self, *args, **kwargs): 
        output = super(CheckboxSelectMultipleWithObjTooltip, self).render(*args,**kwargs) 
        for obj in self.queryset: 
            output = output.replace(str(obj), '%s <img src="/media/wmm/img/info.png" id="info_%s" class="info" />' %(str(obj), obj.objective.short_name) )
        #print output
        return mark_safe(output)     
    
class CheckboxSelectMultipleWithTooltip(forms.CheckboxSelectMultiple):
    def __init__(self, queryset=None, substrate=None, attrs=None):
        super(CheckboxSelectMultipleWithTooltip, self).__init__(attrs)
        self.queryset = queryset
        self.substrate = substrate
        self.attrs = attrs

    def render(self, *args, **kwargs): 
        output = super(CheckboxSelectMultipleWithTooltip, self).render(*args,**kwargs) 
        for param in self.queryset: 
            tidal_substrate = False
            try:
                if param.parameter.short_name == 'substrate' and self.substrate is None and 'tidal' in self.attrs['class']:
                    tidal_substrate = True
            except:
                pass
            if param.parameter.short_name == 'substrate' and self.substrate is not None:
                output = output.replace(str(param), '%s <img src="/media/wmm/img/info.png" id="info_%s" class="info" />' %(str(param), self.substrate) )
            elif tidal_substrate:
                output = output.replace(str(param), '%s <img src="/media/wmm/img/info.png" id="info_tidal_substrate" class="info" />' %(str(param)) )
            else:
                output = output.replace(str(param), '%s <img src="/media/wmm/img/info.png" id="info_%s" class="info" />' %(str(param), param.parameter.short_name) )
        #print output
        return mark_safe(output)     
    
class SliderWidgetWithTooltip(SliderWidget):
    def __init__(self, min, max, step, id):
        super(SliderWidgetWithTooltip, self).__init__(min, max, step)
        self.id = id

    def render(self, *args, **kwargs): 
        output = super(SliderWidgetWithTooltip, self).render(*args,**kwargs) 
        output = output.replace('\n', '<img src="/media/wmm/img/info.png" id="%s" class="info" />\n' %self.id, 1)
        return mark_safe(output)      
    
class DualSliderWidgetWithTooltip(DualSliderWidget):
    def __init__(self, param1, param2, min, max, step, id):
        super(DualSliderWidgetWithTooltip, self).__init__(param1, param2, min, max, step)
        self.id = id

    def render(self, *args, **kwargs): 
        output = super(DualSliderWidgetWithTooltip, self).render(*args,**kwargs) 
        output = output.replace('\n', '<img src="/media/wmm/img/info.png" id="%s" class="info" />\n' %self.id, 1)
        return mark_safe(output)      
    