from django.contrib import admin
from models import *

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
admin.site.register(Folder, FolderAdmin)

class AnalysisFolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'user', 'date_created', 'date_modified')
    list_filter = ['date_modified', 'date_created']
    search_fields = ('name', 'user__username', 'id')
    fields = ['name', 'description']
admin.site.register(AnalysisFolder, AnalysisFolderAdmin)
