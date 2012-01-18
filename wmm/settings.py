# Django settings for omm project.
from lingcod.common.default_settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = "Washington Marine Planner"

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'washington',
        'USER': 'postgres',
     }
}

#TODO change db srid to 26910
GEOMETRY_DB_SRID = 32610 

TIME_ZONE = 'America/Vancouver'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

#SECRET_KEY = 'keep_the_one_autogenerated_by_django-admin'

ROOT_URLCONF = 'wmm.urls'

TEMPLATE_DIRS = ( os.path.realpath(os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')), )

INSTALLED_APPS += ( 'lingcod.analysistools', 
                    'scenario',
                    'smp',
                    'wmm_manipulators',
                    'lingcod.raster_stats')


COMPRESS_JS['application']['source_filenames'] += (
    'wmm/js/excanvas.js',
    'wmm/js/jquery.jqplot.js',
    'wmm/js/jqplot.bubbleRenderer.js',
    'wmm/js/jqplot.canvasTextRenderer.js',
    'wmm/js/jqplot.canvasAxisLabelRenderer.js',
    'wmm/js/jqplot.highlighter.js',
    'wmm/js/jqplot.enhancedLegendRenderer.js',
    'wmm/js/jqplot.barRenderer.js',
    'wmm/js/jqplot.categoryAxisRenderer.js',
    'wmm/js/jqplot.pointLabels.js'
)                    
                    
COMPRESS_CSS['application']['source_filenames'] += (
    'wmm/css/analysis_reports.css',
    'wmm/css/jquery.jqplot.css',
)
  
#was hoping one of the following would speed up the rendering process (it's timing out too often as it is), but not seeing any improvement
#KML_SIMPLIFY_TOLERANCE = 180 # meters (default is 20)
#KML_SIMPLIFY_TOLERANCE_DEGREES = 0.002 # (default is 0.0002)
     
# Make this unique, and don't share it with anybody.
SECRET_KEY = '3j9~fjio+adjf93iwashingtonjda()#Jfk3ljf-ea9#$@#90dsfj9@0aj3()*fj3iow2f'

LOG_FILE =  os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'bmm.log'))

PRIVATE_KML_ROOT = '/usr/local/privatekml'
BOOKMARK_FEATURE = True

#GRASS variables
GISBASE = "/usr/local/grass-6.4.1RC2"
GISDBASE = "/mnt/wmm/grass"
GRASS_TMP = "/tmp"
GRASS_PATH = "/usr/local/grass-6.4.1RC2/bin:/usr/local/grass-6.4.1RC2/scripts:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
GRASS_VERSION = "6.4.1"
GRASS_LIB_PATH = "/usr/local/grass-6.4.1RC2/lib"

from settings_local import *
