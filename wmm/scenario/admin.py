from django.contrib import admin

from django.contrib.auth.models import Permission
admin.site.register(Permission)

from wmm.scenario.models import *

class MOSAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'user', 'date_created', 'date_modified')
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

class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'id']
    fields = ['name', 'short_name']
admin.site.register(Parameter, ParameterAdmin)

class TidalEnergyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'ordering', 'id']
    fields = ['parameter', 'ordering']
    ordering = ['ordering']
admin.site.register(TidalEnergyParameter, TidalEnergyParameterAdmin)

class WaveEnergyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'ordering', 'id']
    fields = ['parameter', 'ordering']
    ordering = ['ordering']
admin.site.register(WaveEnergyParameter, WaveEnergyParameterAdmin)

class WindEnergyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'ordering', 'id']
    fields = ['parameter', 'ordering']
    ordering = ['ordering']
admin.site.register(WindEnergyParameter, WindEnergyParameterAdmin)

class OffshoreConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'ordering', 'id']
    fields = ['parameter', 'ordering']
    ordering = ['ordering']
admin.site.register(OffshoreConservationParameter, OffshoreConservationParameterAdmin)

class NearshoreConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'ordering', 'id']
    fields = ['parameter', 'ordering']
    ordering = ['ordering']
admin.site.register(NearshoreConservationParameter, NearshoreConservationParameterAdmin)

class PelagicConservationParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'ordering', 'id']
    fields = ['parameter', 'ordering']
    ordering = ['ordering']
admin.site.register(PelagicConservationParameter, PelagicConservationParameterAdmin)

class SubstrateAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name', 'color']
    fields = ['name', 'short_name', 'color']
admin.site.register(Substrate, SubstrateAdmin)

class WindPotentialAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'id', 'density', 'speed']
    fields = ['name', 'short_name', 'density', 'speed']
admin.site.register(WindPotential, WindPotentialAdmin)

class DepthClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name']
    fields = ['name', 'short_name']
admin.site.register(DepthClass, DepthClassAdmin)

class GeomorphologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name']
    fields = ['name', 'short_name']
admin.site.register(Geomorphology, GeomorphologyAdmin)

class TidalSubstrateAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name', 'color']
    fields = ['name', 'short_name', 'color']
admin.site.register(TidalSubstrate, TidalSubstrateAdmin)

class NearshoreSubstrateAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name', 'color']
    fields = ['name', 'short_name', 'color']
admin.site.register(NearshoreSubstrate, NearshoreSubstrateAdmin)

class NearshoreExposureAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name']
    fields = ['name', 'short_name']
admin.site.register(NearshoreExposure, NearshoreExposureAdmin)

class NearshoreEcosystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name']
    fields = ['name', 'short_name']
admin.site.register(NearshoreEcosystem, NearshoreEcosystemAdmin)

class UpwellingAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name']
    fields = ['name', 'short_name']
admin.site.register(Upwelling, UpwellingAdmin)

class ChlorophylAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'short_name']
    fields = ['name', 'short_name']
admin.site.register(Chlorophyl, ChlorophylAdmin)

class OffshoreConservationParameterAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']
    fields = ['name', 'area']
admin.site.register(OffshoreConservationParameterArea, OffshoreConservationParameterAreaAdmin)

class NearshoreConservationParameterAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']
    fields = ['name', 'area']
admin.site.register(NearshoreConservationParameterArea, NearshoreConservationParameterAreaAdmin)

class PelagicConservationParameterAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']
    fields = ['name', 'area']
admin.site.register(PelagicConservationParameterArea, PelagicConservationParameterAreaAdmin)

class TidalEnergyParameterAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']
    fields = ['name', 'area']
admin.site.register(TidalEnergyParameterArea, TidalEnergyParameterAreaAdmin)

class WindEnergyParameterAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']
    fields = ['name', 'area']
admin.site.register(WindEnergyParameterArea, WindEnergyParameterAreaAdmin)

class WaveEnergyParameterAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'area']
    fields = ['name', 'area']
admin.site.register(WaveEnergyParameterArea, WaveEnergyParameterAreaAdmin)

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
