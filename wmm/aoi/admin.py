from django.contrib import admin
from wmm.aoi.models import *

class AOIAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
    
admin.site.register(AOI, AOIAdmin)

class ReportCacheAdmin (admin.ModelAdmin):
    list_display = ()

admin.site.register(ReportCache, ReportCacheAdmin)

class ZonalCacheAdmin (admin.ModelAdmin):
    list_display = ()

admin.site.register(ZonalCache, ZonalCacheAdmin)


