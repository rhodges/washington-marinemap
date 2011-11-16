from django.contrib import admin

from django.contrib.auth.models import Permission
admin.site.register(Permission)

from wmm.scenario.models import *

class MultiObjectiveScenarioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description', 'user', 'scenarios', 'support_file'] 
    #NOTE:  can't do 'input_parameters' because it manually specifies a 'through' model ('ScenarioParameters')
admin.site.register(MultiObjectiveScenario, MultiObjectiveScenarioAdmin)

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')
    fields = ['name', 'short_name', 'color']
admin.site.register(Objective, ObjectiveAdmin)

class ParameterAdmin(admin.ModelAdmin):
    fields = ['name', 'short_name']
admin.site.register(Parameter, ParameterAdmin)

class TidalParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter']
    fields = ['parameter']
admin.site.register(TidalParameter, TidalParameterAdmin)

class WindParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter']
    fields = ['parameter']
admin.site.register(WindParameter, WindParameterAdmin)

class ConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter']
    fields = ['parameter']
admin.site.register(ConservationParameter, ConservationParameterAdmin)

class DevelopmentParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter']
    fields = ['parameter']
admin.site.register(DevelopmentParameter, DevelopmentParameterAdmin)

class ShellfishParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter']
    fields = ['parameter']
admin.site.register(ShellfishParameter, ShellfishParameterAdmin)

class FishingParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter']
    fields = ['parameter']
admin.site.register(FishingParameter, FishingParameterAdmin)

class TidalSubstrateAdmin(admin.ModelAdmin):
    list_display = ['substrate']
    fields = ['substrate']
admin.site.register(TidalSubstrate, TidalSubstrateAdmin)

class WindSubstrateAdmin(admin.ModelAdmin):
    list_display = ['substrate']
    fields = ['substrate']
admin.site.register(WindSubstrate, WindSubstrateAdmin)

class ConservationSubstrateAdmin(admin.ModelAdmin):
    list_display = ['substrate']
    fields = ['substrate']
admin.site.register(ConservationSubstrate, ConservationSubstrateAdmin)

class DevelopmentSubstrateAdmin(admin.ModelAdmin):
    list_display = ['substrate']
    fields = ['substrate']
admin.site.register(DevelopmentSubstrate, DevelopmentSubstrateAdmin)

class ShellfishSubstrateAdmin(admin.ModelAdmin):
    list_display = ['substrate']
    fields = ['substrate']
admin.site.register(ShellfishSubstrate, ShellfishSubstrateAdmin)

class FishingSubstrateAdmin(admin.ModelAdmin):
    list_display = ['substrate']
    fields = ['substrate']
admin.site.register(FishingSubstrate, FishingSubstrateAdmin)

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

