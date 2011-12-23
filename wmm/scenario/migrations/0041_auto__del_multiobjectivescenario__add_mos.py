# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario')

        # Removing M2M table for field input_parameters_shoreside_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_shoreside_eb56')

        # Removing M2M table for field input_objectives_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_objectives_development')

        # Removing M2M table for field input_objectives_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_objectives_energy')

        # Removing M2M table for field input_substrate_offshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_offshore_cocdc2')

        # Removing M2M table for field input_substrate_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_shellfish_a0000')

        # Removing M2M table for field sharing_groups on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_sharing_groups')

        # Removing M2M table for field input_parameters_offshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_offshore_cf012')

        # Removing M2M table for field input_objectives_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_objectives_conservation')

        # Removing M2M table for field input_substrate_tidal_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_tidal_energy')

        # Removing M2M table for field input_parameters_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_shellfish_4669')

        # Removing M2M table for field input_substrate_wave_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_wave_energy')

        # Removing M2M table for field scenarios on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_scenarios')

        # Removing M2M table for field input_parameters_wind_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_wind_energy')

        # Removing M2M table for field input_substrate_nearshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_nearshore_c5cf5')

        # Removing M2M table for field input_substrate_shoreside_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_shoreside_d2510')

        # Removing M2M table for field input_parameters_nearshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_nearshore_63d6')

        # Removing M2M table for field input_substrate_wind_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_wind_energy')

        # Removing M2M table for field input_parameters_wave_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_wave_energy')

        # Removing M2M table for field input_objectives_fisheries on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_objectives_fisheries')

        # Removing M2M table for field input_substrate_offshore_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_offshore_fi69e4')

        # Removing M2M table for field input_parameters_water_column_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_water_colufc6f')

        # Removing M2M table for field input_parameters_offshore_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_offshore_f4ee9')

        # Removing M2M table for field input_parameters_tidal_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_tidal_energy')

        # Removing M2M table for field input_substrate_water_column_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_water_columde71')

        # Adding model 'MOS'
        db.create_table('scenario_mos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scenario_mos_related', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='scenario_mos_related', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('input_dist_shore_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('support_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['MOS'])

        # Adding M2M table for field sharing_groups on 'MOS'
        db.create_table('scenario_mos_sharing_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('scenario_mos_sharing_groups', ['mos_id', 'group_id'])

        # Adding M2M table for field scenarios on 'MOS'
        db.create_table('scenario_mos_scenarios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False))
        ))
        db.create_unique('scenario_mos_scenarios', ['mos_id', 'scenario_id'])

        # Adding M2M table for field input_objectives_energy on 'MOS'
        db.create_table('scenario_mos_input_objectives_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('energyobjective', models.ForeignKey(orm['scenario.energyobjective'], null=False))
        ))
        db.create_unique('scenario_mos_input_objectives_energy', ['mos_id', 'energyobjective_id'])

        # Adding M2M table for field input_parameters_tidal_energy on 'MOS'
        db.create_table('scenario_mos_input_parameters_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('tidalenergyparameter', models.ForeignKey(orm['scenario.tidalenergyparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_tidal_energy', ['mos_id', 'tidalenergyparameter_id'])

        # Adding M2M table for field input_substrate_tidal_energy on 'MOS'
        db.create_table('scenario_mos_input_substrate_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('tidalenergysubstrate', models.ForeignKey(orm['scenario.tidalenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_tidal_energy', ['mos_id', 'tidalenergysubstrate_id'])

        # Adding M2M table for field input_parameters_wind_energy on 'MOS'
        db.create_table('scenario_mos_input_parameters_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('windenergyparameter', models.ForeignKey(orm['scenario.windenergyparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_wind_energy', ['mos_id', 'windenergyparameter_id'])

        # Adding M2M table for field input_substrate_wind_energy on 'MOS'
        db.create_table('scenario_mos_input_substrate_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('windenergysubstrate', models.ForeignKey(orm['scenario.windenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_wind_energy', ['mos_id', 'windenergysubstrate_id'])

        # Adding M2M table for field input_parameters_wave_energy on 'MOS'
        db.create_table('scenario_mos_input_parameters_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('waveenergyparameter', models.ForeignKey(orm['scenario.waveenergyparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_wave_energy', ['mos_id', 'waveenergyparameter_id'])

        # Adding M2M table for field input_substrate_wave_energy on 'MOS'
        db.create_table('scenario_mos_input_substrate_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('waveenergysubstrate', models.ForeignKey(orm['scenario.waveenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_wave_energy', ['mos_id', 'waveenergysubstrate_id'])

        # Adding M2M table for field input_objectives_conservation on 'MOS'
        db.create_table('scenario_mos_input_objectives_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('conservationobjective', models.ForeignKey(orm['scenario.conservationobjective'], null=False))
        ))
        db.create_unique('scenario_mos_input_objectives_conservation', ['mos_id', 'conservationobjective_id'])

        # Adding M2M table for field input_parameters_offshore_conservation on 'MOS'
        db.create_table('scenario_mos_input_parameters_offshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('offshoreconservationparameter', models.ForeignKey(orm['scenario.offshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_offshore_conservation', ['mos_id', 'offshoreconservationparameter_id'])

        # Adding M2M table for field input_substrate_offshore_conservation on 'MOS'
        db.create_table('scenario_mos_input_substrate_offshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('offshoreconservationsubstrate', models.ForeignKey(orm['scenario.offshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_offshore_conservation', ['mos_id', 'offshoreconservationsubstrate_id'])

        # Adding M2M table for field input_parameters_nearshore_conservation on 'MOS'
        db.create_table('scenario_mos_input_parameters_nearshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('nearshoreconservationparameter', models.ForeignKey(orm['scenario.nearshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_nearshore_conservation', ['mos_id', 'nearshoreconservationparameter_id'])

        # Adding M2M table for field input_substrate_nearshore_conservation on 'MOS'
        db.create_table('scenario_mos_input_substrate_nearshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('nearshoreconservationsubstrate', models.ForeignKey(orm['scenario.nearshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_nearshore_conservation', ['mos_id', 'nearshoreconservationsubstrate_id'])

        # Adding M2M table for field input_parameters_water_column_conservation on 'MOS'
        db.create_table('scenario_mos_input_parameters_water_column_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('watercolumnconservationparameter', models.ForeignKey(orm['scenario.watercolumnconservationparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_water_column_conservation', ['mos_id', 'watercolumnconservationparameter_id'])

        # Adding M2M table for field input_substrate_water_column_conservation on 'MOS'
        db.create_table('scenario_mos_input_substrate_water_column_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('watercolumnconservationsubstrate', models.ForeignKey(orm['scenario.watercolumnconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_water_column_conservation', ['mos_id', 'watercolumnconservationsubstrate_id'])

        # Adding M2M table for field input_objectives_development on 'MOS'
        db.create_table('scenario_mos_input_objectives_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('developmentobjective', models.ForeignKey(orm['scenario.developmentobjective'], null=False))
        ))
        db.create_unique('scenario_mos_input_objectives_development', ['mos_id', 'developmentobjective_id'])

        # Adding M2M table for field input_parameters_shoreside_development on 'MOS'
        db.create_table('scenario_mos_input_parameters_shoreside_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('shoresidedevelopmentparameter', models.ForeignKey(orm['scenario.shoresidedevelopmentparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_shoreside_development', ['mos_id', 'shoresidedevelopmentparameter_id'])

        # Adding M2M table for field input_substrate_shoreside_development on 'MOS'
        db.create_table('scenario_mos_input_substrate_shoreside_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('shoresidedevelopmentsubstrate', models.ForeignKey(orm['scenario.shoresidedevelopmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_shoreside_development', ['mos_id', 'shoresidedevelopmentsubstrate_id'])

        # Adding M2M table for field input_objectives_fisheries on 'MOS'
        db.create_table('scenario_mos_input_objectives_fisheries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('fisheriesobjective', models.ForeignKey(orm['scenario.fisheriesobjective'], null=False))
        ))
        db.create_unique('scenario_mos_input_objectives_fisheries', ['mos_id', 'fisheriesobjective_id'])

        # Adding M2M table for field input_parameters_shellfish_aquaculture on 'MOS'
        db.create_table('scenario_mos_input_parameters_shellfish_aquaculture', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('shellfishaquacultureparameter', models.ForeignKey(orm['scenario.shellfishaquacultureparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_shellfish_aquaculture', ['mos_id', 'shellfishaquacultureparameter_id'])

        # Adding M2M table for field input_substrate_shellfish_aquaculture on 'MOS'
        db.create_table('scenario_mos_input_substrate_shellfish_aquaculture', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('shellfishaquaculturesubstrate', models.ForeignKey(orm['scenario.shellfishaquaculturesubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_shellfish_aquaculture', ['mos_id', 'shellfishaquaculturesubstrate_id'])

        # Adding M2M table for field input_parameters_offshore_fishing on 'MOS'
        db.create_table('scenario_mos_input_parameters_offshore_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('offshorefishingparameter', models.ForeignKey(orm['scenario.offshorefishingparameter'], null=False))
        ))
        db.create_unique('scenario_mos_input_parameters_offshore_fishing', ['mos_id', 'offshorefishingparameter_id'])

        # Adding M2M table for field input_substrate_offshore_fishing on 'MOS'
        db.create_table('scenario_mos_input_substrate_offshore_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mos', models.ForeignKey(orm['scenario.mos'], null=False)),
            ('offshorefishingsubstrate', models.ForeignKey(orm['scenario.offshorefishingsubstrate'], null=False))
        ))
        db.create_unique('scenario_mos_input_substrate_offshore_fishing', ['mos_id', 'offshorefishingsubstrate_id'])


    def backwards(self, orm):
        
        # Adding model 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario', (
            ('input_dist_port_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('input_min_depth_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('support_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('input_dist_shore_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('input_dist_shore_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('input_min_depth_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scenario_multiobjectivescenario_related', null=True, to=orm['contenttypes.ContentType'], blank=True)),
            ('input_min_depth_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_max_depth_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('input_max_depth_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_port_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_dist_shore_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('input_dist_port_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('input_min_depth_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scenario_multiobjectivescenario_related', to=orm['auth.User'])),
        ))
        db.send_create_signal('scenario', ['MultiObjectiveScenario'])

        # Adding M2M table for field input_parameters_shoreside_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_shoreside_eb56', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shoresidedevelopmentparameter', models.ForeignKey(orm['scenario.shoresidedevelopmentparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_shoreside_eb56', ['multiobjectivescenario_id', 'shoresidedevelopmentparameter_id'])

        # Adding M2M table for field input_objectives_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_objectives_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('developmentobjective', models.ForeignKey(orm['scenario.developmentobjective'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_objectives_development', ['multiobjectivescenario_id', 'developmentobjective_id'])

        # Adding M2M table for field input_objectives_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_objectives_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('energyobjective', models.ForeignKey(orm['scenario.energyobjective'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_objectives_energy', ['multiobjectivescenario_id', 'energyobjective_id'])

        # Adding M2M table for field input_substrate_offshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_offshore_cocdc2', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshoreconservationsubstrate', models.ForeignKey(orm['scenario.offshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_offshore_cocdc2', ['multiobjectivescenario_id', 'offshoreconservationsubstrate_id'])

        # Adding M2M table for field input_substrate_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_shellfish_a0000', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shellfishaquaculturesubstrate', models.ForeignKey(orm['scenario.shellfishaquaculturesubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_shellfish_a0000', ['multiobjectivescenario_id', 'shellfishaquaculturesubstrate_id'])

        # Adding M2M table for field sharing_groups on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_sharing_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_sharing_groups', ['multiobjectivescenario_id', 'group_id'])

        # Adding M2M table for field input_parameters_offshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_offshore_cf012', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshoreconservationparameter', models.ForeignKey(orm['scenario.offshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_offshore_cf012', ['multiobjectivescenario_id', 'offshoreconservationparameter_id'])

        # Adding M2M table for field input_objectives_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_objectives_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('conservationobjective', models.ForeignKey(orm['scenario.conservationobjective'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_objectives_conservation', ['multiobjectivescenario_id', 'conservationobjective_id'])

        # Adding M2M table for field input_substrate_tidal_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalenergysubstrate', models.ForeignKey(orm['scenario.tidalenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_tidal_energy', ['multiobjectivescenario_id', 'tidalenergysubstrate_id'])

        # Adding M2M table for field input_parameters_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_shellfish_4669', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shellfishaquacultureparameter', models.ForeignKey(orm['scenario.shellfishaquacultureparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_shellfish_4669', ['multiobjectivescenario_id', 'shellfishaquacultureparameter_id'])

        # Adding M2M table for field input_substrate_wave_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('waveenergysubstrate', models.ForeignKey(orm['scenario.waveenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_wave_energy', ['multiobjectivescenario_id', 'waveenergysubstrate_id'])

        # Adding M2M table for field scenarios on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_scenarios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_scenarios', ['multiobjectivescenario_id', 'scenario_id'])

        # Adding M2M table for field input_parameters_wind_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('windenergyparameter', models.ForeignKey(orm['scenario.windenergyparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_wind_energy', ['multiobjectivescenario_id', 'windenergyparameter_id'])

        # Adding M2M table for field input_substrate_nearshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_nearshore_c5cf5', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('nearshoreconservationsubstrate', models.ForeignKey(orm['scenario.nearshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_nearshore_c5cf5', ['multiobjectivescenario_id', 'nearshoreconservationsubstrate_id'])

        # Adding M2M table for field input_substrate_shoreside_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_shoreside_d2510', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shoresidedevelopmentsubstrate', models.ForeignKey(orm['scenario.shoresidedevelopmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_shoreside_d2510', ['multiobjectivescenario_id', 'shoresidedevelopmentsubstrate_id'])

        # Adding M2M table for field input_parameters_nearshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_nearshore_63d6', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('nearshoreconservationparameter', models.ForeignKey(orm['scenario.nearshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_nearshore_63d6', ['multiobjectivescenario_id', 'nearshoreconservationparameter_id'])

        # Adding M2M table for field input_substrate_wind_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('windenergysubstrate', models.ForeignKey(orm['scenario.windenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_wind_energy', ['multiobjectivescenario_id', 'windenergysubstrate_id'])

        # Adding M2M table for field input_parameters_wave_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('waveenergyparameter', models.ForeignKey(orm['scenario.waveenergyparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_wave_energy', ['multiobjectivescenario_id', 'waveenergyparameter_id'])

        # Adding M2M table for field input_objectives_fisheries on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_objectives_fisheries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('fisheriesobjective', models.ForeignKey(orm['scenario.fisheriesobjective'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_objectives_fisheries', ['multiobjectivescenario_id', 'fisheriesobjective_id'])

        # Adding M2M table for field input_substrate_offshore_fishing on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_offshore_fi69e4', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshorefishingsubstrate', models.ForeignKey(orm['scenario.offshorefishingsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_offshore_fi69e4', ['multiobjectivescenario_id', 'offshorefishingsubstrate_id'])

        # Adding M2M table for field input_parameters_water_column_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_water_colufc6f', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('watercolumnconservationparameter', models.ForeignKey(orm['scenario.watercolumnconservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_water_colufc6f', ['multiobjectivescenario_id', 'watercolumnconservationparameter_id'])

        # Adding M2M table for field input_parameters_offshore_fishing on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_offshore_f4ee9', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshorefishingparameter', models.ForeignKey(orm['scenario.offshorefishingparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_offshore_f4ee9', ['multiobjectivescenario_id', 'offshorefishingparameter_id'])

        # Adding M2M table for field input_parameters_tidal_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalenergyparameter', models.ForeignKey(orm['scenario.tidalenergyparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_tidal_energy', ['multiobjectivescenario_id', 'tidalenergyparameter_id'])

        # Adding M2M table for field input_substrate_water_column_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_water_columde71', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('watercolumnconservationsubstrate', models.ForeignKey(orm['scenario.watercolumnconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_water_columde71', ['multiobjectivescenario_id', 'watercolumnconservationsubstrate_id'])

        # Deleting model 'MOS'
        db.delete_table('scenario_mos')

        # Removing M2M table for field sharing_groups on 'MOS'
        db.delete_table('scenario_mos_sharing_groups')

        # Removing M2M table for field scenarios on 'MOS'
        db.delete_table('scenario_mos_scenarios')

        # Removing M2M table for field input_objectives_energy on 'MOS'
        db.delete_table('scenario_mos_input_objectives_energy')

        # Removing M2M table for field input_parameters_tidal_energy on 'MOS'
        db.delete_table('scenario_mos_input_parameters_tidal_energy')

        # Removing M2M table for field input_substrate_tidal_energy on 'MOS'
        db.delete_table('scenario_mos_input_substrate_tidal_energy')

        # Removing M2M table for field input_parameters_wind_energy on 'MOS'
        db.delete_table('scenario_mos_input_parameters_wind_energy')

        # Removing M2M table for field input_substrate_wind_energy on 'MOS'
        db.delete_table('scenario_mos_input_substrate_wind_energy')

        # Removing M2M table for field input_parameters_wave_energy on 'MOS'
        db.delete_table('scenario_mos_input_parameters_wave_energy')

        # Removing M2M table for field input_substrate_wave_energy on 'MOS'
        db.delete_table('scenario_mos_input_substrate_wave_energy')

        # Removing M2M table for field input_objectives_conservation on 'MOS'
        db.delete_table('scenario_mos_input_objectives_conservation')

        # Removing M2M table for field input_parameters_offshore_conservation on 'MOS'
        db.delete_table('scenario_mos_input_parameters_offshore_conservation')

        # Removing M2M table for field input_substrate_offshore_conservation on 'MOS'
        db.delete_table('scenario_mos_input_substrate_offshore_conservation')

        # Removing M2M table for field input_parameters_nearshore_conservation on 'MOS'
        db.delete_table('scenario_mos_input_parameters_nearshore_conservation')

        # Removing M2M table for field input_substrate_nearshore_conservation on 'MOS'
        db.delete_table('scenario_mos_input_substrate_nearshore_conservation')

        # Removing M2M table for field input_parameters_water_column_conservation on 'MOS'
        db.delete_table('scenario_mos_input_parameters_water_column_conservation')

        # Removing M2M table for field input_substrate_water_column_conservation on 'MOS'
        db.delete_table('scenario_mos_input_substrate_water_column_conservation')

        # Removing M2M table for field input_objectives_development on 'MOS'
        db.delete_table('scenario_mos_input_objectives_development')

        # Removing M2M table for field input_parameters_shoreside_development on 'MOS'
        db.delete_table('scenario_mos_input_parameters_shoreside_development')

        # Removing M2M table for field input_substrate_shoreside_development on 'MOS'
        db.delete_table('scenario_mos_input_substrate_shoreside_development')

        # Removing M2M table for field input_objectives_fisheries on 'MOS'
        db.delete_table('scenario_mos_input_objectives_fisheries')

        # Removing M2M table for field input_parameters_shellfish_aquaculture on 'MOS'
        db.delete_table('scenario_mos_input_parameters_shellfish_aquaculture')

        # Removing M2M table for field input_substrate_shellfish_aquaculture on 'MOS'
        db.delete_table('scenario_mos_input_substrate_shellfish_aquaculture')

        # Removing M2M table for field input_parameters_offshore_fishing on 'MOS'
        db.delete_table('scenario_mos_input_parameters_offshore_fishing')

        # Removing M2M table for field input_substrate_offshore_fishing on 'MOS'
        db.delete_table('scenario_mos_input_substrate_offshore_fishing')


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
            'input_substrate_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.NearshoreConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreFishingSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishAquacultureSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShoresideDevelopmentSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_tidal_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalEnergySubstrate']", 'symmetrical': 'False'}),
            'input_substrate_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaterColumnConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaveEnergySubstrate']", 'symmetrical': 'False'}),
            'input_substrate_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindEnergySubstrate']", 'symmetrical': 'False'}),
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
        'scenario.nearshoreconservationsubstrate': {
            'Meta': {'object_name': 'NearshoreConservationSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
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
        'scenario.offshoreconservationsubstrate': {
            'Meta': {'object_name': 'OffshoreConservationSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.offshorefishingparameter': {
            'Meta': {'object_name': 'OffshoreFishingParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.offshorefishingsubstrate': {
            'Meta': {'object_name': 'OffshoreFishingSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
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
            'input_parameters_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.NearshoreConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreFishingParameter']", 'symmetrical': 'False'}),
            'input_parameters_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishAquacultureParameter']", 'symmetrical': 'False'}),
            'input_parameters_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShoresideDevelopmentParameter']", 'symmetrical': 'False'}),
            'input_parameters_tidal_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalEnergyParameter']", 'symmetrical': 'False'}),
            'input_parameters_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaterColumnConservationParameter']", 'symmetrical': 'False'}),
            'input_parameters_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaveEnergyParameter']", 'symmetrical': 'False'}),
            'input_parameters_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindEnergyParameter']", 'symmetrical': 'False'}),
            'input_substrate_nearshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.NearshoreConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_offshore_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_offshore_fishing': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.OffshoreFishingSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_shellfish_aquaculture': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShellfishAquacultureSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_shoreside_development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.ShoresideDevelopmentSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_tidal_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.TidalEnergySubstrate']", 'symmetrical': 'False'}),
            'input_substrate_water_column_conservation': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaterColumnConservationSubstrate']", 'symmetrical': 'False'}),
            'input_substrate_wave_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WaveEnergySubstrate']", 'symmetrical': 'False'}),
            'input_substrate_wind_energy': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scenario.WindEnergySubstrate']", 'symmetrical': 'False'}),
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
        'scenario.shellfishaquaculturesubstrate': {
            'Meta': {'object_name': 'ShellfishAquacultureSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.shoresidedevelopmentparameter': {
            'Meta': {'object_name': 'ShoresideDevelopmentParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.shoresidedevelopmentsubstrate': {
            'Meta': {'object_name': 'ShoresideDevelopmentSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
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
        'scenario.watercolumnconservationsubstrate': {
            'Meta': {'object_name': 'WaterColumnConservationSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.waveenergyparameter': {
            'Meta': {'object_name': 'WaveEnergyParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.waveenergysubstrate': {
            'Meta': {'object_name': 'WaveEnergySubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
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
        },
        'scenario.windenergysubstrate': {
            'Meta': {'object_name': 'WindEnergySubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Substrate']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scenario']
