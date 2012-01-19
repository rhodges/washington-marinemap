from django.contrib import admin

from wmm.smp.models import *

class SMPSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description', 'user'] 
admin.site.register(SMPSite, SMPSiteAdmin)
