# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FederalWaters'
        db.create_table('wmm_manipulators_federalwaters', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('wmm_manipulators', ['FederalWaters'])

        # Adding model 'Estuaries'
        db.create_table('wmm_manipulators_estuaries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('wmm_manipulators', ['Estuaries'])

        # Adding model 'StateWaters'
        db.create_table('wmm_manipulators_statewaters', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=32610, null=True, blank=True)),
        ))
        db.send_create_signal('wmm_manipulators', ['StateWaters'])


    def backwards(self, orm):
        
        # Deleting model 'FederalWaters'
        db.delete_table('wmm_manipulators_federalwaters')

        # Deleting model 'Estuaries'
        db.delete_table('wmm_manipulators_estuaries')

        # Deleting model 'StateWaters'
        db.delete_table('wmm_manipulators_statewaters')


    models = {
        'wmm_manipulators.estuaries': {
            'Meta': {'object_name': 'Estuaries'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'wmm_manipulators.federalwaters': {
            'Meta': {'object_name': 'FederalWaters'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'wmm_manipulators.marine': {
            'Meta': {'object_name': 'Marine'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'wmm_manipulators.statewaters': {
            'Meta': {'object_name': 'StateWaters'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'wmm_manipulators.terrestrial': {
            'Meta': {'object_name': 'Terrestrial'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['wmm_manipulators']
