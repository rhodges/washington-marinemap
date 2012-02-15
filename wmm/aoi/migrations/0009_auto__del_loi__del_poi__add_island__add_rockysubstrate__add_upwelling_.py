# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'LOI'
        db.delete_table('aoi_loi')

        # Removing M2M table for field sharing_groups on 'LOI'
        db.delete_table('aoi_loi_sharing_groups')

        # Deleting model 'POI'
        db.delete_table('aoi_poi')

        # Removing M2M table for field sharing_groups on 'POI'
        db.delete_table('aoi_poi_sharing_groups')

        # Adding model 'Island'
        db.create_table('aoi_island', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Island'])

        # Adding model 'RockySubstrate'
        db.create_table('aoi_rockysubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['RockySubstrate'])

        # Adding model 'Upwelling'
        db.create_table('aoi_upwelling', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Upwelling'])

        # Adding model 'EstuaryHabitat'
        db.create_table('aoi_estuaryhabitat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('habitat', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=29)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['EstuaryHabitat'])

        # Adding model 'Canyon'
        db.create_table('aoi_canyon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phys_hab', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('sgh_lith_1', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['Canyon'])

        # Adding model 'BenthicHabitat'
        db.create_table('aoi_benthichabitat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('depth', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('geomorph', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['BenthicHabitat'])


    def backwards(self, orm):
        
        # Adding model 'LOI'
        db.create_table('aoi_loi', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('manipulators', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='aoi_loi_related', to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='aoi_loi_related', null=True, to=orm['contenttypes.ContentType'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geometry_orig', self.gf('django.contrib.gis.db.models.fields.LineStringField')(srid=32610, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('geometry_final', self.gf('django.contrib.gis.db.models.fields.LineStringField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['LOI'])

        # Adding M2M table for field sharing_groups on 'LOI'
        db.create_table('aoi_loi_sharing_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('loi', models.ForeignKey(orm['aoi.loi'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('aoi_loi_sharing_groups', ['loi_id', 'group_id'])

        # Adding model 'POI'
        db.create_table('aoi_poi', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('manipulators', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='aoi_poi_related', to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='aoi_poi_related', null=True, to=orm['contenttypes.ContentType'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geometry_orig', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=32610, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('geometry_final', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('aoi', ['POI'])

        # Adding M2M table for field sharing_groups on 'POI'
        db.create_table('aoi_poi_sharing_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('poi', models.ForeignKey(orm['aoi.poi'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('aoi_poi_sharing_groups', ['poi_id', 'group_id'])

        # Deleting model 'Island'
        db.delete_table('aoi_island')

        # Deleting model 'RockySubstrate'
        db.delete_table('aoi_rockysubstrate')

        # Deleting model 'Upwelling'
        db.delete_table('aoi_upwelling')

        # Deleting model 'EstuaryHabitat'
        db.delete_table('aoi_estuaryhabitat')

        # Deleting model 'Canyon'
        db.delete_table('aoi_canyon')

        # Deleting model 'BenthicHabitat'
        db.delete_table('aoi_benthichabitat')


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
        'aoi.conservationscoring': {
            'Meta': {'object_name': 'ConservationScoring'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {})
        },
        'aoi.estuaryhabitat': {
            'Meta': {'object_name': 'EstuaryHabitat'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'habitat': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '29'})
        },
        'aoi.island': {
            'Meta': {'object_name': 'Island'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aoi.rockysubstrate': {
            'Meta': {'object_name': 'RockySubstrate'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
