from django.contrib import admin

from django.contrib.auth.models import Permission
admin.site.register(Permission)

from wmm.scenario.models import *

class ScenarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Scenario, ScenarioAdmin)


class FolderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Folder, FolderAdmin)

