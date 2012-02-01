from django.contrib.gis import admin
from wmm.wmm_manipulators.models import *


class TerrestrialAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'creation_date',)
    
admin.site.register(Terrestrial, TerrestrialAdmin)

class MarineAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'creation_date',)
    
admin.site.register(Marine, MarineAdmin)