# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field input_substrate_tidal_energy on 'MOS'
        db.delete_table('scenario_mos_input_substrate_tidal_energy')


    def backwards(self, orm):
        
        # Adding M2M table for field input_substrate_tidal_energy on 'MOS'
        db.create_table('scenario_mos_input_substrate_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('substrate', models.ForeignKey(orm['scenario.substrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_tidal_energy', ['mos_id', 'substrate_id'])


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
        'scenario.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'scenario.conservationobjective': {
            'Meta': {'object_name': 'ConservationObjective'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Objective']", 'null': 'True', 'blank': 'True'})
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
        'scenario.developmentobjective': {
            'Meta': {'object_name': 'DevelopmentObjective'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Objective']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.energyobjective': {
            'Meta': {'object_name': 'EnergyObjective'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Objective']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.fisheriesobjective': {
            'Meta': {'object_name': 'FisheriesObjective'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Objective']", 'null': 'True', 'blank': 'True'})
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
        'scenario.mos': {
            'Meta': {'object_name': 'MOS'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_mos_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_dist_port_nearshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_offshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_offshore_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_shellfish_aquaculture': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_shoreside_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_tidal_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_water_column_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_wave_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_port_wind_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_nearshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_offshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_offshore_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_shellfish_aquaculture': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_shoreside_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_tidal_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_water_column_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_wave_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore_wind_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_nearshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_offshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_offshore_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_shellfish_aquaculture': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_shoreside_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_tidal_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_water_column_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_wave_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth_wind_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_nearshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_offshore_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_offshore_fishing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_shellfish_aquaculture': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_shoreside_development': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_tidal_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_water_column_conservation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_wave_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth_wind_energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_objectives_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.ConservationObjective']", 'null': 'True', 'blank': 'True'}),
            'input_objectives_development': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.DevelopmentObjective']", 'null': 'True', 'blank': 'True'}),
            'input_objectives_energy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.EnergyObjective']", 'null': 'True', 'blank': 'True'}),
            'input_objectives_fisheries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.FisheriesObjective']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.NearshoreConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreFishingParameter']", 'symmetrical': 'False'}),
            'input_parameters_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishAquacultureParameter']", 'symmetrical': 'False'}),
            'input_parameters_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShoresideDevelopmentParameter']", 'symmetrical': 'False'}),
            'input_parameters_tidal_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalEnergyParameter']", 'symmetrical': 'False'}),
            'input_parameters_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaterColumnConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaveEnergyParameter']", 'symmetrical': 'False'}),
            'input_parameters_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindEnergyParameter']", 'symmetrical': 'False'}),
            'input_substrate_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSNearshoreConservationSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSOffshoreConservationSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSOffshoreFishingSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSShellfishAquacultureSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSShoresideDevelopmentSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSWaterColumnConservationSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSWaveEnergySubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MOSWindEnergySubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scenarios': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.Scenario']", 'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_mos_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'support_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_mos_related'", 'to': "orm['auth.User']"})
        },
        'scenario.nearshoreconservationparameter': {
            'Meta': {'object_name': 'NearshoreConservationParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.objective': {
            'Meta': {'object_name': 'Objective'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'778B1A55'", 'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'scenario.offshoreconservationparameter': {
            'Meta': {'object_name': 'OffshoreConservationParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.offshorefishingparameter': {
            'Meta': {'object_name': 'OffshoreFishingParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
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
            'input_dist_port': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_dist_shore': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_max_depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_min_depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'input_objective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Objective']"}),
            'input_parameters_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.NearshoreConservationParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.OffshoreConservationParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.OffshoreFishingParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.ShellfishAquacultureParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.ShoresideDevelopmentParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_tidal_energy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.TidalEnergyParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.WaterColumnConservationParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.WaveEnergyParameter']", 'null': 'True', 'blank': 'True'}),
            'input_parameters_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.WindEnergyParameter']", 'null': 'True', 'blank': 'True'}),
            'input_substrate_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'NearshoreConservationSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'OffshoreConservationSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'OffshoreFishingSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ShellfishAquacultureSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ShoresideDevelopmentSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_tidal_energy': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'TidalEnergySubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'WaterColumnConservationSubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'WaveEnergySubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'input_substrate_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'WindEnergySubstrate'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['scenario.Substrate']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'output_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'output_geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '32610', 'null': 'True', 'blank': 'True'}),
            'output_mapcalc': ('django.db.models.fields.CharField', [], {'max_length': '360', 'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_scenario_related'", 'to': "orm['auth.User']"})
        },
        'scenario.shellfishaquacultureparameter': {
            'Meta': {'object_name': 'ShellfishAquacultureParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.shoresidedevelopmentparameter': {
            'Meta': {'object_name': 'ShoresideDevelopmentParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.substrate': {
            'Meta': {'object_name': 'Substrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'scenario.tidalenergyparameter': {
            'Meta': {'object_name': 'TidalEnergyParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.tidalenergysubstrate': {
            'Meta': {'object_name': 'TidalEnergySubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
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
        'scenario.watercolumnconservationparameter': {
            'Meta': {'object_name': 'WaterColumnConservationParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.waveenergyparameter': {
            'Meta': {'object_name': 'WaveEnergyParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.windenergyparameter': {
            'Meta': {'object_name': 'WindEnergyParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['scenario']
