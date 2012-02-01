from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Include all lingcod app urls. 
    (r'', include('lingcod.common.urls')),
    (r'^bookmark/', include('lingcod.bookmarks.urls')),
    (r'^folder/', include('folder.urls')),
    (r'^scenario/', include('scenario.urls')),
    (r'^smp/', include('smp.urls')),
)
