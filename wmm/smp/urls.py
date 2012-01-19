from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    #feature reports
    url(r'report/(\d+)/(\w+)', smp_analysis, name='smp_analysis'), #user requested smp analysis 
)
