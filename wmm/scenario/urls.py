from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'form/get-params', get_params), #called from the scenario creation wizard
    url(r'conservation/(\d+)/(\w+)', conservation_analysis, name='conservation_analysis'), #user requested conservation analysis 
    url(r'wind/(\d+)/(\w+)', wind_analysis, name='wind_analysis'), #user requested wind energy analysis 
)
