# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OverwaterStructure'
        db.create_table('smp_overwaterstructure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')()),
            ('structure', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('boat', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('os_detail', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cart_cd', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('navigability', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('county_nm', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('complexity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('smp', ['OverwaterStructure'])


    def backwards(self, orm):
        
        # Deleting model 'OverwaterStructure'
        db.delete_table('smp_overwaterstructure')


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
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'rep_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
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
