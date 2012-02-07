from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    #url(r'form/get-objs', get_objs), #called from the scenario creation wizard on edit
    url(r'form/list-params', list_params), #called from the scenario creation wizard
    
    #multi-objective scenario reports
    url(r'mos/view-report/(\d+)/(\d+)', scenario_report, name='scenario_report'), #user requested multi-objective scenario report
    url(r'mos/view-report/(\d+)', overlap_report, name='overlap_report'), #user requested multi-objective overlap report
    
)
