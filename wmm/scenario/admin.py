from django.contrib import admin

from django.contrib.auth.models import Permission
admin.site.register(Permission)

from wmm.scenario.models import *

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description', 'user', 'input_objectives', 'support_file'] 
    #NOTE:  can't do 'input_parameters' because it manually specifies a 'through' model ('ScenarioParameters')
admin.site.register(Scenario, ScenarioAdmin)

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')
    fields = ['name', 'color']
admin.site.register(Objective, ObjectiveAdmin)

class ParameterAdmin(admin.ModelAdmin):
    fields = ['name', 'objectives']
admin.site.register(Parameter, ParameterAdmin)

class ConservationSiteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
admin.site.register(ConservationSite, ConservationSiteAdmin)

class WindEnergySiteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
admin.site.register(WindEnergySite, WindEnergySiteAdmin)

class AOIAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
admin.site.register(AOI, AOIAdmin)

class FolderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
admin.site.register(Folder, FolderAdmin)

