# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LandUseTransportation'
        db.create_table('smp_landusetransportation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseTransportation'])

        # Adding model 'PublicAccess'
        db.create_table('smp_publicaccess', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')()),
            ('beach_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('class_desc', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('beach_name_caps', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('rep_name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['PublicAccess'])

        # Adding model 'LandUseTrade'
        db.create_table('smp_landusetrade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseTrade'])

        # Adding model 'LandUseManufacturing'
        db.create_table('smp_landusemanufacturing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseManufacturing'])

        # Adding model 'LandUseUndeveloped'
        db.create_table('smp_landuseundeveloped', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseUndeveloped'])

        # Adding model 'LandUseResidential'
        db.create_table('smp_landuseresidential', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseResidential'])

        # Adding model 'LandUseCultural'
        db.create_table('smp_landusecultural', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseCultural'])

        # Adding model 'LandUseServices'
        db.create_table('smp_landuseservices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('landuse_cd', self.gf('django.db.models.fields.IntegerField')()),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=72)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('lu_code', self.gf('django.db.models.fields.FloatField')()),
            ('lu_class', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['LandUseServices'])


    def backwards(self, orm):
        
        # Deleting model 'LandUseTransportation'
        db.delete_table('smp_landusetransportation')

        # Deleting model 'PublicAccess'
        db.delete_table('smp_publicaccess')

        # Deleting model 'LandUseTrade'
        db.delete_table('smp_landusetrade')

        # Deleting model 'LandUseManufacturing'
        db.delete_table('smp_landusemanufacturing')

        # Deleting model 'LandUseUndeveloped'
        db.delete_table('smp_landuseundeveloped')

        # Deleting model 'LandUseResidential'
        db.delete_table('smp_landuseresidential')

        # Deleting model 'LandUseCultural'
        db.delete_table('smp_landusecultural')

        # Deleting model 'LandUseServices'
        db.delete_table('smp_landuseservices')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'smp.landusecultural': {
            'Meta': {'object_name': 'LandUseCultural'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.landusemanufacturing': {
            'Meta': {'object_name': 'LandUseManufacturing'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.landuseresidential': {
            'Meta': {'object_name': 'LandUseResidential'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.landuseservices': {
            'Meta': {'object_name': 'LandUseServices'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.landusetrade': {
            'Meta': {'object_name': 'LandUseTrade'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.landusetransportation': {
            'Meta': {'object_name': 'LandUseTransportation'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.landuseundeveloped': {
            'Meta': {'object_name': 'LandUseUndeveloped'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '72'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landuse_cd': ('django.db.models.fields.IntegerField', [], {}),
            'lu_class': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'lu_code': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'smp.overwaterstructure': {
            'Meta': {'object_name': 'OverwaterStructure'},
            'boat': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'cart_cd': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'county_nm': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'navigability': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {}),
            'os_detail': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'smp.publicaccess': {
            'Meta': {'object_name': 'PublicAccess'},
            'beach_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'beach_name_caps': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'class_desc': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'objectid': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'rep_name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'smp.reportcache': {
            'Meta': {'object_name': 'ReportCache'},
            'context': ('picklefield.fields.PickledObjectField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wkt_hash': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'smp.smpsite': {
            'Meta': {'object_name': 'SMPSite'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'smp_smpsite_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'smp_smpsite_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'smp_smpsite_related'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['smp']
