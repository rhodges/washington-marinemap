from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'form/get-params', get_params), #called from the scenario creation wizard
    
    #feature reports
    url(r'conservation/(\d+)/(\w+)', conservation_analysis, name='conservation_analysis'), #user requested conservation analysis 
    url(r'wind/(\d+)/(\w+)', wind_analysis, name='wind_analysis'), #user requested wind energy analysis 
    
    #tradeoff analysis
    #url(r'tradeoff/(\d+)', tradeoff_analysis, name='tradeoff_analysis'), #user requested tradeoff analysis
    url(r'tradeoff/show-analysis', tradeoff_analysis, name='tradeoff_analysis'), #user requested tradeoff analysis
    url(r'tradeoff/show-table', tradeoff_table, name='tradeoff_table'), #user requested tradeoff analysis
)
