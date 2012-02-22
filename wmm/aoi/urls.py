from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    #feature reports
    url(r'report/(\d+)/(\w+)', aoi_analysis, name='aoi_analysis'), #user requested aoi analysis 
    #admin request cache events
    url(r'admin_clear_cache/(\w+)/', admin_clear_aoi_report_cache),
)
