from django.contrib import admin

from django.contrib.auth.models import Permission
admin.site.register(Permission)

from wmm.scenario.models import *

class MOSAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description', 'user', 'scenarios', 'support_file'] 
    #NOTE:  can't do 'input_parameters' because it manually specifies a 'through' model ('ScenarioParameters')
admin.site.register(MOS, MOSAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'pk')
    fields = ['name', 'short_name']
admin.site.register(Category, CategoryAdmin)

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'pk')
    fields = ['name', 'short_name', 'color']
admin.site.register(Objective, ObjectiveAdmin)

class EnergyObjectiveAdmin(admin.ModelAdmin):
    list_display = ['objective']
    fields = ['objective']
admin.site.register(EnergyObjective, EnergyObjectiveAdmin)

class ConservationObjectiveAdmin(admin.ModelAdmin):
    list_display = ['objective']
    fields = ['objective']
admin.site.register(ConservationObjective, ConservationObjectiveAdmin)

class FisheriesObjectiveAdmin(admin.ModelAdmin):
    list_display = ['objective']
    fields = ['objective']
admin.site.register(FisheriesObjective, FisheriesObjectiveAdmin)

class DevelopmentObjectiveAdmin(admin.ModelAdmin):
    list_display = ['objective']
    fields = ['objective']
admin.site.register(DevelopmentObjective, DevelopmentObjectiveAdmin)

class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'id']
    fields = ['name', 'short_name']
admin.site.register(Parameter, ParameterAdmin)

class TidalEnergyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(TidalEnergyParameter, TidalEnergyParameterAdmin)

class WaveEnergyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(WaveEnergyParameter, WaveEnergyParameterAdmin)

class WindEnergyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(WindEnergyParameter, WindEnergyParameterAdmin)

class OffshoreConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(OffshoreConservationParameter, OffshoreConservationParameterAdmin)

class NearshoreConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(NearshoreConservationParameter, NearshoreConservationParameterAdmin)

class WaterColumnConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(WaterColumnConservationParameter, WaterColumnConservationParameterAdmin)

class ShoresideDevelopmentParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(ShoresideDevelopmentParameter, ShoresideDevelopmentParameterAdmin)

class ShellfishAquacultureParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(ShellfishAquacultureParameter, ShellfishAquacultureParameterAdmin)

class OffshoreFishingParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id']
    fields = ['parameter']
admin.site.register(OffshoreFishingParameter, OffshoreFishingParameterAdmin)

class SubstrateAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'color']
    fields = ['name', 'color']
admin.site.register(Substrate, SubstrateAdmin)

class DepthClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    fields = ['name']
admin.site.register(DepthClass, DepthClassAdmin)

class GeomorphologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    fields = ['name']
admin.site.register(Geomorphology, GeomorphologyAdmin)

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

