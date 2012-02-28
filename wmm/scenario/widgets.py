from django import forms
from django.forms.widgets import *
from django.utils.safestring import mark_safe

class CheckboxSelectMultipleWithTooltip(forms.CheckboxSelectMultiple):
    def __init__(self, queryset=None, substrate=None, attrs=None):
        super(CheckboxSelectMultipleWithTooltip, self).__init__(attrs)
        self.queryset = queryset
        self.substrate = substrate

    def render(self, *args, **kwargs): 
        output = super(CheckboxSelectMultipleWithTooltip, self).render(*args,**kwargs) 
        for param in self.queryset:
            if param.parameter.short_name == 'substrate' and self.substrate is not None:
                output = output.replace(str(param), '%s <img src="/media/wmm/img/info.png" id="info_%s" class="info" />' %(str(param), self.substrate) )
            else:
                output = output.replace(str(param), '%s <img src="/media/wmm/img/info.png" id="info_%s" class="info" />' %(str(param), param.parameter.short_name) )
        #print output
        return mark_safe(output)
        #return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').replace(u'<li>', u'        
    