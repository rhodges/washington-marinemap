from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    #url(r'form/get-objs', get_objs), #called from the scenario creation wizard on edit
    url(r'form/list-params', list_params), #called from the scenario creation wizard
    
    #feature reports
    url(r'smp/(\d+)/(\w+)', smp_analysis, name='smp_analysis'), #user requested smp analysis 
    url(r'conservation/(\d+)/(\w+)', conservation_analysis, name='conservation_analysis'), #user requested conservation analysis 
    url(r'wind/(\d+)/(\w+)', wind_analysis, name='wind_analysis'), #user requested wind energy analysis 
    
    #multi-objective scenario reports
    url(r'mos/view-report/(\d+)/(\d+)', scenario_report, name='scenario_report'), #user requested multi-objective scenario report
    
    #tradeoff analysis
    #url(r'tradeoff/(\d+)', tradeoff_analysis, name='tradeoff_analysis'), #user requested tradeoff analysis
    url(r'tradeoff/show-analysis', tradeoff_analysis, name='tradeoff_analysis'), #user requested tradeoff analysis
    url(r'tradeoff/show-table', tradeoff_table, name='tradeoff_table'), #user requested tradeoff analysis
)
