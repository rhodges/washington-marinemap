# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FishingSubstrate.substrate'
        db.delete_column('scenario_fishingsubstrate', 'substrate')

        # Deleting field 'ConservationSubstrate.substrate'
        db.delete_column('scenario_conservationsubstrate', 'substrate')

        # Deleting field 'WindSubstrate.substrate'
        db.delete_column('scenario_windsubstrate', 'substrate')

        # Deleting field 'TidalSubstrate.substrate'
        db.delete_column('scenario_tidalsubstrate', 'substrate')

        # Deleting field 'ShellfishSubstrate.substrate'
        db.delete_column('scenario_shellfishsubstrate', 'substrate')

        # Deleting field 'DevelopmentSubstrate.substrate'
        db.delete_column('scenario_developmentsubstrate', 'substrate')


    def backwards(self, orm):
        
        # We cannot add back in field 'FishingSubstrate.substrate'
        raise RuntimeError(
            "Cannot reverse this migration. 'FishingSubstrate.substrate' and its values cannot be restored.")

        # We cannot add back in field 'ConservationSubstrate.substrate'
        raise RuntimeError(
            "Cannot reverse this migration. 'ConservationSubstrate.substrate' and its values cannot be restored.")

        # We cannot add back in field 'WindSubstrate.substrate'
        raise RuntimeError(
            "Cannot reverse this migration. 'WindSubstrate.substrate' and its values cannot be restored.")

        # We cannot add back in field 'TidalSubstrate.substrate'
        raise RuntimeError(
            "Cannot reverse this migration. 'TidalSubstrate.substrate' and its values cannot be restored.")

        # We cannot add back in field 'ShellfishSubstrate.substrate'
        raise RuntimeError(
            "Cannot reverse this migration. 'ShellfishSubstrate.substrate' and its values cannot be restored.")

        # We cannot add back in field 'DevelopmentSubstrate.substrate'
        raise RuntimeError(
            "Cannot reverse this migration. 'DevelopmentSubstrate.substrate' and its values cannot be restored.")


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
        'scenario.aoi': {
            'Meta': {'object_name': 'AOI'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_aoi_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_aoi_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_aoi_related'", 'to': "orm['auth.User']"})
        },
        'scenario.conservationparameter': {
            'Meta': {'object_name': 'ConservationParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.conservationsite': {
            'Meta': {'object_name': 'ConservationSite'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_conservationsite_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_conservationsite_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_conservationsite_related'", 'to': "orm['auth.User']"})
        },
        'scenario.conservationsubstrate': {
            'Meta': {'object_name': 'ConservationSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.developmentparameter': {
            'Meta': {'object_name': 'DevelopmentParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.developmentsubstrate': {
            'Meta': {'object_name': 'DevelopmentSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.fishingparameter': {
            'Meta': {'object_name': 'FishingParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.fishingsubstrate': {
            'Meta': {'object_name': 'FishingSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.folder': {
            'Meta': {'object_name': 'Folder'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_folder_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_folder_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_folder_related'", 'to': "orm['auth.User']"})
        },
        'scenario.loi': {
            'Meta': {'object_name': 'LOI'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_loi_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_loi_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_loi_related'", 'to': "orm['auth.User']"})
        },
        'scenario.multiobjectivescenario': {
            'Meta': {'object_name': 'MultiObjectiveScenario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_multiobjectivescenario_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_dist_port_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_shellfish': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_tidal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_wind': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_shellfish': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_tidal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_wind': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_shellfish': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_tidal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_wind': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_shellfish': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_tidal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_wind': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_objectives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.Objective']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.DevelopmentParameter']", 'symmetrical': 'False'}),
            'input_parameters_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.FishingParameter']", 'symmetrical': 'False'}),
            'input_parameters_shellfish': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishParameter']", 'symmetrical': 'False'}),
            'input_parameters_tidal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalParameter']", 'symmetrical': 'False'}),
            'input_parameters_wind': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindParameter']", 'symmetrical': 'False'}),
            'input_substrate_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.DevelopmentSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.FishingSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_shellfish': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_tidal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_wind': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindSubstrate']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scenarios': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.Scenario']", 'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_multiobjectivescenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'support_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_multiobjectivescenario_related'", 'to': "orm['auth.User']"})
        },
        'scenario.objective': {
            'Meta': {'object_name': 'Objective'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'778B1A55'", 'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'scenario.parameter': {
            'Meta': {'object_name': 'Parameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'scenario.poi': {
            'Meta': {'object_name': 'POI'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_poi_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_poi_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_poi_related'", 'to': "orm['auth.User']"})
        },
        'scenario.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_scenario_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_dist_port': ('django.db.models.fields.FloatField', [], {}),
            'input_dist_shore': ('django.db.models.fields.FloatField', [], {}),
            'input_max_depth': ('django.db.models.fields.FloatField', [], {}),
            'input_min_depth': ('django.db.models.fields.FloatField', [], {}),
            'input_objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Objective']"}),
            'input_parameters_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.DevelopmentParameter']", 'symmetrical': 'False'}),
            'input_parameters_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.FishingParameter']", 'symmetrical': 'False'}),
            'input_parameters_shellfish': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishParameter']", 'symmetrical': 'False'}),
            'input_parameters_tidal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalParameter']", 'symmetrical': 'False'}),
            'input_parameters_wind': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindParameter']", 'symmetrical': 'False'}),
            'input_substrate_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.DevelopmentSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.FishingSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_shellfish': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_tidal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_wind': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindSubstrate']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'output_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'output_geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'output_mapcalc': ('django.db.models.fields.CharField', [], {'max_length': '360', 'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_scenario_related'", 'to': "orm['auth.User']"})
        },
        'scenario.shellfishparameter': {
            'Meta': {'object_name': 'ShellfishParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.shellfishsubstrate': {
            'Meta': {'object_name': 'ShellfishSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.substrate': {
            'Meta': {'object_name': 'Substrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'scenario.tidalparameter': {
            'Meta': {'object_name': 'TidalParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.tidalsubstrate': {
            'Meta': {'object_name': 'TidalSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.userkml': {
            'Meta': {'object_name': 'UserKml'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_userkml_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kml_file': ('django.db.models.fields.files.FileField', [], {'max_length': '510'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_userkml_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_userkml_related'", 'to': "orm['auth.User']"})
        },
        'scenario.windenergysite': {
            'Meta': {'object_name': 'WindEnergySite'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_windenergysite_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_windenergysite_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_windenergysite_related'", 'to': "orm['auth.User']"})
        },
        'scenario.windparameter': {
            'Meta': {'object_name': 'WindParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.windsubstrate': {
            'Meta': {'object_name': 'WindSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scenario']
