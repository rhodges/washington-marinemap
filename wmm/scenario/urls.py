from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'form/get-params', get_params), 
)
