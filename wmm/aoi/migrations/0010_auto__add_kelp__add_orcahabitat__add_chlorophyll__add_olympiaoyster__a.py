# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Kelp'
        db.create_table('aoi_kelp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Kelp'])

        # Adding model 'OrcaHabitat'
        db.create_table('aoi_orcahabitat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tgt', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['OrcaHabitat'])

        # Adding model 'Chlorophyll'
        db.create_table('aoi_chlorophyll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Chlorophyll'])

        # Adding model 'OlympiaOyster'
        db.create_table('aoi_olympiaoyster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estuary', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['OlympiaOyster'])

        # Adding model 'SnowyPloverHabitat'
        db.create_table('aoi_snowyploverhabitat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['SnowyPloverHabitat'])

        # Adding model 'Haulout'
        db.create_table('aoi_haulout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('com_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Haulout'])

        # Adding model 'Seabird'
        db.create_table('aoi_seabird', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('species', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Seabird'])

        # Adding model 'Coral'
        db.create_table('aoi_coral', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordcode', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('sum_cpuekg', self.gf('django.db.models.fields.FloatField')()),
            ('coral_type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Coral'])

        # Adding model 'Sponge'
        db.create_table('aoi_sponge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cpuekgkm', self.gf('django.db.models.fields.FloatField')()),
            ('common_nam', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('target_nam', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Sponge'])


    def backwards(self, orm):
        
        # Deleting model 'Kelp'
        db.delete_table('aoi_kelp')

        # Deleting model 'OrcaHabitat'
        db.delete_table('aoi_orcahabitat')

        # Deleting model 'Chlorophyll'
        db.delete_table('aoi_chlorophyll')

        # Deleting model 'OlympiaOyster'
        db.delete_table('aoi_olympiaoyster')

        # Deleting model 'SnowyPloverHabitat'
        db.delete_table('aoi_snowyploverhabitat')

        # Deleting model 'Haulout'
        db.delete_table('aoi_haulout')

        # Deleting model 'Seabird'
        db.delete_table('aoi_seabird')

        # Deleting model 'Coral'
        db.delete_table('aoi_coral')

        # Deleting model 'Sponge'
        db.delete_table('aoi_sponge')


    models = {
        'aoi.aoi': {
            'Meta': {'object_name': 'AOI'},
            'conservation_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'aoi_aoi_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_hash': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'aoi_aoi_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aoi_aoi_related'", 'to': "orm['auth.User']"})
        },
        'aoi.benthichabitat': {
            'Meta': {'object_name': 'BenthicHabitat'},
            'depth': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geomorph': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'aoi.canyon': {
            'Meta': {'object_name': 'Canyon'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phys_hab': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sgh_lith_1': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'aoi.chlorophyll': {
            'Meta': {'object_name': 'Chlorophyll'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'aoi.conservationscoring': {
            'Meta': {'object_name': 'ConservationScoring'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {})
        },
        'aoi.coral': {
            'Meta': {'object_name': 'Coral'},
            'coral_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordcode': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'sum_cpuekg': ('django.db.models.fields.FloatField', [], {})
        },
        'aoi.estuaryhabitat': {
            'Meta': {'object_name': 'EstuaryHabitat'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'habitat': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '29'})
        },
        'aoi.haulout': {
            'Meta': {'object_name': 'Haulout'},
            'com_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aoi.island': {
            'Meta': {'object_name': 'Island'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aoi.kelp': {
            'Meta': {'object_name': 'Kelp'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aoi.olympiaoyster': {
            'Meta': {'object_name': 'OlympiaOyster'},
            'estuary': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aoi.orcahabitat': {
            'Meta': {'object_name': 'OrcaHabitat'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tgt': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'aoi.rockysubstrate': {
            'Meta': {'object_name': 'RockySubstrate'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aoi.seabird': {
            'Meta': {'object_name': 'Seabird'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'aoi.snowyploverhabitat': {
            'Meta': {'object_name': 'SnowyPloverHabitat'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aoi.sponge': {
            'Meta': {'object_name': 'Sponge'},
            'common_nam': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'cpuekgkm': ('django.db.models.fields.FloatField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'target_nam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aoi.upwelling': {
            'Meta': {'object_name': 'Upwelling'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
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
        }
    }

    complete_apps = ['aoi']
