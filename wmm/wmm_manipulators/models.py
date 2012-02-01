from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from lingcod.manipulators.models import BaseManipulatorGeometry

    
class Terrestrial(BaseManipulatorGeometry):
    name = models.CharField(verbose_name="Terrestrial Geometry Name", max_length=255, blank=True)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Terrestrial-Only")

    def __unicode__(self):
        return "Terrestrial Layer, created: %s" % (self.creation_date)

class Marine(BaseManipulatorGeometry):
    name = models.CharField(verbose_name="Marine Geometry Name", max_length=255, blank=True)
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Marine-Only")

    def __unicode__(self):
        return "Marine Layer, created: %s" % (self.creation_date)

#Used the following for loading shapefiles into postgres and then copied the geometries over from the shell command line        
'''        
class Marine_Shp(models.Model):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True)

class Terrestrial_Shp(models.Model):
    geometry = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True)
'''
