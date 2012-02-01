from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    #tradeoff analysis
    #url(r'tradeoff/(\d+)', tradeoff_analysis, name='tradeoff_analysis'), #user requested tradeoff analysis
    url(r'tradeoff/show-analysis', tradeoff_analysis, name='tradeoff_analysis'), #user requested tradeoff analysis
    url(r'tradeoff/show-table', tradeoff_table, name='tradeoff_table'), #user requested tradeoff analysis
)