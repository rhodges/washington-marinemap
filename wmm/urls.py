from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Include all madrona app urls. 
    (r'', include('madrona.common.urls')),
    (r'^bookmark/', include('madrona.bookmarks.urls')),
    (r'^general/', include('general.urls')),
    (r'^scenario/', include('scenario.urls')),
    (r'^smp/', include('smp.urls')),
    (r'^aoi/', include('aoi.urls'))
)
