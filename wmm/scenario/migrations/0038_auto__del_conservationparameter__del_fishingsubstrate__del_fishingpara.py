# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ConservationParameter'
        db.delete_table('scenario_conservationparameter')

        # Deleting model 'FishingSubstrate'
        db.delete_table('scenario_fishingsubstrate')

        # Deleting model 'FishingParameter'
        db.delete_table('scenario_fishingparameter')

        # Deleting model 'ConservationSubstrate'
        db.delete_table('scenario_conservationsubstrate')

        # Deleting model 'ShellfishParameter'
        db.delete_table('scenario_shellfishparameter')

        # Deleting model 'TidalParameter'
        db.delete_table('scenario_tidalparameter')

        # Deleting model 'WindParameter'
        db.delete_table('scenario_windparameter')

        # Deleting model 'WindSubstrate'
        db.delete_table('scenario_windsubstrate')

        # Deleting model 'TidalSubstrate'
        db.delete_table('scenario_tidalsubstrate')

        # Deleting model 'DevelopmentParameter'
        db.delete_table('scenario_developmentparameter')

        # Deleting model 'ShellfishSubstrate'
        db.delete_table('scenario_shellfishsubstrate')

        # Deleting model 'DevelopmentSubstrate'
        db.delete_table('scenario_developmentsubstrate')

        # Adding model 'ShoresideDevelopmentParameter'
        db.create_table('scenario_shoresidedevelopmentparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['ShoresideDevelopmentParameter'])

        # Adding model 'ShoresideDevelopmentSubstrate'
        db.create_table('scenario_shoresidedevelopmentsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['ShoresideDevelopmentSubstrate'])

        # Adding model 'NearshoreConservationSubstrate'
        db.create_table('scenario_nearshoreconservationsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['NearshoreConservationSubstrate'])

        # Adding model 'OffshoreConservationSubstrate'
        db.create_table('scenario_offshoreconservationsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['OffshoreConservationSubstrate'])

        # Adding model 'OffshoreFishingSubstrate'
        db.create_table('scenario_offshorefishingsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['OffshoreFishingSubstrate'])

        # Adding model 'WaterColumnConservationSubstrate'
        db.create_table('scenario_watercolumnconservationsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['WaterColumnConservationSubstrate'])

        # Adding model 'TidalEnergySubstrate'
        db.create_table('scenario_tidalenergysubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['TidalEnergySubstrate'])

        # Adding model 'WaterColumnConservationParameter'
        db.create_table('scenario_watercolumnconservationparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['WaterColumnConservationParameter'])

        # Adding model 'ShellfishAquacultureParameter'
        db.create_table('scenario_shellfishaquacultureparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['ShellfishAquacultureParameter'])

        # Adding model 'ShellfishAquacultureSubstrate'
        db.create_table('scenario_shellfishaquaculturesubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['ShellfishAquacultureSubstrate'])

        # Adding model 'OffshoreConservationParameter'
        db.create_table('scenario_offshoreconservationparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['OffshoreConservationParameter'])

        # Adding model 'NearshoreConservationParameter'
        db.create_table('scenario_nearshoreconservationparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['NearshoreConservationParameter'])

        # Adding model 'WindEnergyParameter'
        db.create_table('scenario_windenergyparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['WindEnergyParameter'])

        # Adding model 'TidalEnergyParameter'
        db.create_table('scenario_tidalenergyparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['TidalEnergyParameter'])

        # Adding model 'OffshoreFishingParameter'
        db.create_table('scenario_offshorefishingparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['OffshoreFishingParameter'])

        # Adding model 'WindEnergySubstrate'
        db.create_table('scenario_windenergysubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['WindEnergySubstrate'])

        # Adding model 'WaveEnergyParameter'
        db.create_table('scenario_waveenergyparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['WaveEnergyParameter'])

        # Adding model 'WaveEnergySubstrate'
        db.create_table('scenario_waveenergysubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['WaveEnergySubstrate'])

        # Removing M2M table for field input_substrate_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_conservation')

        # Removing M2M table for field input_parameters_development on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_development')

        # Removing M2M table for field input_parameters_wind on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_wind')

        # Removing M2M table for field input_substrate_development on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_development')

        # Removing M2M table for field input_parameters_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_conservation')

        # Removing M2M table for field input_parameters_shellfish on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_shellfish')

        # Removing M2M table for field input_substrate_wind on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_wind')

        # Removing M2M table for field input_substrate_shellfish on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_shellfish')

        # Removing M2M table for field input_substrate_fishing on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_fishing')

        # Removing M2M table for field input_parameters_fishing on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_fishing')

        # Removing M2M table for field input_parameters_tidal on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_tidal')

        # Removing M2M table for field input_substrate_tidal on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_tidal')

        # Adding M2M table for field input_parameters_tidal_energy on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('tidalenergyparameter', models.ForeignKey(orm['scenario.tidalenergyparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_tidal_energy', ['scenario_id', 'tidalenergyparameter_id'])

        # Adding M2M table for field input_parameters_wind_energy on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('windenergyparameter', models.ForeignKey(orm['scenario.windenergyparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_wind_energy', ['scenario_id', 'windenergyparameter_id'])

        # Adding M2M table for field input_parameters_wave_energy on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('waveenergyparameter', models.ForeignKey(orm['scenario.waveenergyparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_wave_energy', ['scenario_id', 'waveenergyparameter_id'])

        # Adding M2M table for field input_parameters_offshore_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_offshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('offshoreconservationparameter', models.ForeignKey(orm['scenario.offshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_offshore_conservation', ['scenario_id', 'offshoreconservationparameter_id'])

        # Adding M2M table for field input_parameters_nearshore_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_nearshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('nearshoreconservationparameter', models.ForeignKey(orm['scenario.nearshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_nearshore_conservation', ['scenario_id', 'nearshoreconservationparameter_id'])

        # Adding M2M table for field input_parameters_water_column_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_water_column_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('watercolumnconservationparameter', models.ForeignKey(orm['scenario.watercolumnconservationparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_water_column_conservation', ['scenario_id', 'watercolumnconservationparameter_id'])

        # Adding M2M table for field input_parameters_shoreside_development on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_shoreside_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('shoresidedevelopmentparameter', models.ForeignKey(orm['scenario.shoresidedevelopmentparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_shoreside_development', ['scenario_id', 'shoresidedevelopmentparameter_id'])

        # Adding M2M table for field input_parameters_shellfish_aquaculture on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_shellfish_aquaculture', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('shellfishaquacultureparameter', models.ForeignKey(orm['scenario.shellfishaquacultureparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_shellfish_aquaculture', ['scenario_id', 'shellfishaquacultureparameter_id'])

        # Adding M2M table for field input_parameters_offshore_fishing on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_offshore_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('offshorefishingparameter', models.ForeignKey(orm['scenario.offshorefishingparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_offshore_fishing', ['scenario_id', 'offshorefishingparameter_id'])

        # Adding M2M table for field input_substrate_tidal_energy on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('tidalenergysubstrate', models.ForeignKey(orm['scenario.tidalenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_tidal_energy', ['scenario_id', 'tidalenergysubstrate_id'])

        # Adding M2M table for field input_substrate_wave_energy on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('waveenergysubstrate', models.ForeignKey(orm['scenario.waveenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_wave_energy', ['scenario_id', 'waveenergysubstrate_id'])

        # Adding M2M table for field input_substrate_wind_energy on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('windenergysubstrate', models.ForeignKey(orm['scenario.windenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_wind_energy', ['scenario_id', 'windenergysubstrate_id'])

        # Adding M2M table for field input_substrate_offshore_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_offshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('offshoreconservationsubstrate', models.ForeignKey(orm['scenario.offshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_offshore_conservation', ['scenario_id', 'offshoreconservationsubstrate_id'])

        # Adding M2M table for field input_substrate_nearshore_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_nearshore_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('nearshoreconservationsubstrate', models.ForeignKey(orm['scenario.nearshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_nearshore_conservation', ['scenario_id', 'nearshoreconservationsubstrate_id'])

        # Adding M2M table for field input_substrate_water_column_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_water_column_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('watercolumnconservationsubstrate', models.ForeignKey(orm['scenario.watercolumnconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_water_column_conservation', ['scenario_id', 'watercolumnconservationsubstrate_id'])

        # Adding M2M table for field input_substrate_shoreside_development on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_shoreside_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('shoresidedevelopmentsubstrate', models.ForeignKey(orm['scenario.shoresidedevelopmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_shoreside_development', ['scenario_id', 'shoresidedevelopmentsubstrate_id'])

        # Adding M2M table for field input_substrate_shellfish_aquaculture on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_shellfish_aquaculture', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('shellfishaquaculturesubstrate', models.ForeignKey(orm['scenario.shellfishaquaculturesubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_shellfish_aquaculture', ['scenario_id', 'shellfishaquaculturesubstrate_id'])

        # Adding M2M table for field input_substrate_offshore_fishing on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_offshore_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('offshorefishingsubstrate', models.ForeignKey(orm['scenario.offshorefishingsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_offshore_fishing', ['scenario_id', 'offshorefishingsubstrate_id'])

        # Deleting field 'MultiObjectiveScenario.input_dist_port_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_development')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_fishing')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_fishing')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_development')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_development')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_tidal')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_development')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_fishing')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_tidal')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_wind')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_tidal')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_wind')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_wind')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_wind')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_conservation')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_tidal')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_fishing')

        # Adding field 'MultiObjectiveScenario.input_dist_shore_tidal_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_tidal_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_tidal_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_tidal_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_tidal_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_wind_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_wind_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_wind_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_wind_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_wind_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_wave_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_wave_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_wave_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_wave_energy'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_wave_energy', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_offshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_offshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_offshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_offshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_offshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_nearshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_nearshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_nearshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_nearshore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_nearshore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_water_column_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_water_column_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_water_column_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_water_column_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_water_column_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_shoreside_development'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_shoreside_development'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_shoreside_development'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_shoreside_development'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_shoreside_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_shellfish_aquaculture'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_shellfish_aquaculture'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_shellfish_aquaculture'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_shellfish_aquaculture'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_shellfish_aquaculture', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_offshore_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_offshore_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_offshore_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_offshore_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_offshore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Removing M2M table for field input_substrate_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_conservation')

        # Removing M2M table for field input_parameters_wind on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_wind')

        # Removing M2M table for field input_parameters_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_conservation')

        # Removing M2M table for field input_parameters_shellfish on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_shellfish')

        # Removing M2M table for field input_substrate_shellfish on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_shellfish')

        # Removing M2M table for field input_substrate_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_fishing')

        # Removing M2M table for field input_substrate_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_development')

        # Removing M2M table for field input_parameters_tidal on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_tidal')

        # Removing M2M table for field input_substrate_tidal on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_tidal')

        # Removing M2M table for field input_parameters_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_development')

        # Removing M2M table for field input_substrate_wind on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_wind')

        # Removing M2M table for field input_parameters_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_fishing')

        # Adding M2M table for field input_parameters_tidal_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalenergyparameter', models.ForeignKey(orm['scenario.tidalenergyparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_tidal_energy', ['multiobjectivescenario_id', 'tidalenergyparameter_id'])

        # Adding M2M table for field input_substrate_tidal_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_tidal_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalenergysubstrate', models.ForeignKey(orm['scenario.tidalenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_tidal_energy', ['multiobjectivescenario_id', 'tidalenergysubstrate_id'])

        # Adding M2M table for field input_parameters_wind_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_wind_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('windenergyparameter', models.ForeignKey(orm['scenario.windenergyparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_wind_energy', ['multiobjectivescenario_id', 'windenergyparameter_id'])

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

        # Adding M2M table for field input_substrate_wave_energy on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_wave_energy', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('waveenergysubstrate', models.ForeignKey(orm['scenario.waveenergysubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_wave_energy', ['multiobjectivescenario_id', 'waveenergysubstrate_id'])

        # Adding M2M table for field input_parameters_offshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_offshore_cf012', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshoreconservationparameter', models.ForeignKey(orm['scenario.offshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_offshore_cf012', ['multiobjectivescenario_id', 'offshoreconservationparameter_id'])

        # Adding M2M table for field input_substrate_offshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_offshore_cocdc2', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshoreconservationsubstrate', models.ForeignKey(orm['scenario.offshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_offshore_cocdc2', ['multiobjectivescenario_id', 'offshoreconservationsubstrate_id'])

        # Adding M2M table for field input_parameters_nearshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_nearshore_63d6', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('nearshoreconservationparameter', models.ForeignKey(orm['scenario.nearshoreconservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_nearshore_63d6', ['multiobjectivescenario_id', 'nearshoreconservationparameter_id'])

        # Adding M2M table for field input_substrate_nearshore_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_nearshore_c5cf5', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('nearshoreconservationsubstrate', models.ForeignKey(orm['scenario.nearshoreconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_nearshore_c5cf5', ['multiobjectivescenario_id', 'nearshoreconservationsubstrate_id'])

        # Adding M2M table for field input_parameters_water_column_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_water_colufc6f', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('watercolumnconservationparameter', models.ForeignKey(orm['scenario.watercolumnconservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_water_colufc6f', ['multiobjectivescenario_id', 'watercolumnconservationparameter_id'])

        # Adding M2M table for field input_substrate_water_column_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_water_columde71', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('watercolumnconservationsubstrate', models.ForeignKey(orm['scenario.watercolumnconservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_water_columde71', ['multiobjectivescenario_id', 'watercolumnconservationsubstrate_id'])

        # Adding M2M table for field input_parameters_shoreside_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_shoreside_eb56', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shoresidedevelopmentparameter', models.ForeignKey(orm['scenario.shoresidedevelopmentparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_shoreside_eb56', ['multiobjectivescenario_id', 'shoresidedevelopmentparameter_id'])

        # Adding M2M table for field input_substrate_shoreside_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_shoreside_d2510', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shoresidedevelopmentsubstrate', models.ForeignKey(orm['scenario.shoresidedevelopmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_shoreside_d2510', ['multiobjectivescenario_id', 'shoresidedevelopmentsubstrate_id'])

        # Adding M2M table for field input_parameters_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_shellfish_4669', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shellfishaquacultureparameter', models.ForeignKey(orm['scenario.shellfishaquacultureparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_shellfish_4669', ['multiobjectivescenario_id', 'shellfishaquacultureparameter_id'])

        # Adding M2M table for field input_substrate_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_shellfish_a0000', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shellfishaquaculturesubstrate', models.ForeignKey(orm['scenario.shellfishaquaculturesubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_shellfish_a0000', ['multiobjectivescenario_id', 'shellfishaquaculturesubstrate_id'])

        # Adding M2M table for field input_parameters_offshore_fishing on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_offshore_f4ee9', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshorefishingparameter', models.ForeignKey(orm['scenario.offshorefishingparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_offshore_f4ee9', ['multiobjectivescenario_id', 'offshorefishingparameter_id'])

        # Adding M2M table for field input_substrate_offshore_fishing on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_offshore_fi69e4', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('offshorefishingsubstrate', models.ForeignKey(orm['scenario.offshorefishingsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_offshore_fi69e4', ['multiobjectivescenario_id', 'offshorefishingsubstrate_id'])


    def backwards(self, orm):
        
        # Adding model 'ConservationParameter'
        db.create_table('scenario_conservationparameter', (
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['ConservationParameter'])

        # Adding model 'FishingSubstrate'
        db.create_table('scenario_fishingsubstrate', (
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['FishingSubstrate'])

        # Adding model 'FishingParameter'
        db.create_table('scenario_fishingparameter', (
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['FishingParameter'])

        # Adding model 'ConservationSubstrate'
        db.create_table('scenario_conservationsubstrate', (
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['ConservationSubstrate'])

        # Adding model 'ShellfishParameter'
        db.create_table('scenario_shellfishparameter', (
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['ShellfishParameter'])

        # Adding model 'TidalParameter'
        db.create_table('scenario_tidalparameter', (
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['TidalParameter'])

        # Adding model 'WindParameter'
        db.create_table('scenario_windparameter', (
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['WindParameter'])

        # Adding model 'WindSubstrate'
        db.create_table('scenario_windsubstrate', (
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['WindSubstrate'])

        # Adding model 'TidalSubstrate'
        db.create_table('scenario_tidalsubstrate', (
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['TidalSubstrate'])

        # Adding model 'DevelopmentParameter'
        db.create_table('scenario_developmentparameter', (
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Parameter'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['DevelopmentParameter'])

        # Adding model 'ShellfishSubstrate'
        db.create_table('scenario_shellfishsubstrate', (
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['ShellfishSubstrate'])

        # Adding model 'DevelopmentSubstrate'
        db.create_table('scenario_developmentsubstrate', (
            ('substrate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scenario.Substrate'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('scenario', ['DevelopmentSubstrate'])

        # Deleting model 'ShoresideDevelopmentParameter'
        db.delete_table('scenario_shoresidedevelopmentparameter')

        # Deleting model 'ShoresideDevelopmentSubstrate'
        db.delete_table('scenario_shoresidedevelopmentsubstrate')

        # Deleting model 'NearshoreConservationSubstrate'
        db.delete_table('scenario_nearshoreconservationsubstrate')

        # Deleting model 'OffshoreConservationSubstrate'
        db.delete_table('scenario_offshoreconservationsubstrate')

        # Deleting model 'OffshoreFishingSubstrate'
        db.delete_table('scenario_offshorefishingsubstrate')

        # Deleting model 'WaterColumnConservationSubstrate'
        db.delete_table('scenario_watercolumnconservationsubstrate')

        # Deleting model 'TidalEnergySubstrate'
        db.delete_table('scenario_tidalenergysubstrate')

        # Deleting model 'WaterColumnConservationParameter'
        db.delete_table('scenario_watercolumnconservationparameter')

        # Deleting model 'ShellfishAquacultureParameter'
        db.delete_table('scenario_shellfishaquacultureparameter')

        # Deleting model 'ShellfishAquacultureSubstrate'
        db.delete_table('scenario_shellfishaquaculturesubstrate')

        # Deleting model 'OffshoreConservationParameter'
        db.delete_table('scenario_offshoreconservationparameter')

        # Deleting model 'NearshoreConservationParameter'
        db.delete_table('scenario_nearshoreconservationparameter')

        # Deleting model 'WindEnergyParameter'
        db.delete_table('scenario_windenergyparameter')

        # Deleting model 'TidalEnergyParameter'
        db.delete_table('scenario_tidalenergyparameter')

        # Deleting model 'OffshoreFishingParameter'
        db.delete_table('scenario_offshorefishingparameter')

        # Deleting model 'WindEnergySubstrate'
        db.delete_table('scenario_windenergysubstrate')

        # Deleting model 'WaveEnergyParameter'
        db.delete_table('scenario_waveenergyparameter')

        # Deleting model 'WaveEnergySubstrate'
        db.delete_table('scenario_waveenergysubstrate')

        # Adding M2M table for field input_substrate_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('conservationsubstrate', models.ForeignKey(orm['scenario.conservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_conservation', ['scenario_id', 'conservationsubstrate_id'])

        # Adding M2M table for field input_parameters_development on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('developmentparameter', models.ForeignKey(orm['scenario.developmentparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_development', ['scenario_id', 'developmentparameter_id'])

        # Adding M2M table for field input_parameters_wind on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_wind', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('windparameter', models.ForeignKey(orm['scenario.windparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_wind', ['scenario_id', 'windparameter_id'])

        # Adding M2M table for field input_substrate_development on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('developmentsubstrate', models.ForeignKey(orm['scenario.developmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_development', ['scenario_id', 'developmentsubstrate_id'])

        # Adding M2M table for field input_parameters_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('conservationparameter', models.ForeignKey(orm['scenario.conservationparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_conservation', ['scenario_id', 'conservationparameter_id'])

        # Adding M2M table for field input_parameters_shellfish on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_shellfish', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('shellfishparameter', models.ForeignKey(orm['scenario.shellfishparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_shellfish', ['scenario_id', 'shellfishparameter_id'])

        # Adding M2M table for field input_substrate_wind on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_wind', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('windsubstrate', models.ForeignKey(orm['scenario.windsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_wind', ['scenario_id', 'windsubstrate_id'])

        # Adding M2M table for field input_substrate_shellfish on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_shellfish', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('shellfishsubstrate', models.ForeignKey(orm['scenario.shellfishsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_shellfish', ['scenario_id', 'shellfishsubstrate_id'])

        # Adding M2M table for field input_substrate_fishing on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('fishingsubstrate', models.ForeignKey(orm['scenario.fishingsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_fishing', ['scenario_id', 'fishingsubstrate_id'])

        # Adding M2M table for field input_parameters_fishing on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('fishingparameter', models.ForeignKey(orm['scenario.fishingparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_fishing', ['scenario_id', 'fishingparameter_id'])

        # Adding M2M table for field input_parameters_tidal on 'Scenario'
        db.create_table('scenario_scenario_input_parameters_tidal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('tidalparameter', models.ForeignKey(orm['scenario.tidalparameter'], null=False))
        ))
        db.create_unique('scenario_scenario_input_parameters_tidal', ['scenario_id', 'tidalparameter_id'])

        # Adding M2M table for field input_substrate_tidal on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_tidal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('tidalsubstrate', models.ForeignKey(orm['scenario.tidalsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_tidal', ['scenario_id', 'tidalsubstrate_id'])

        # Removing M2M table for field input_parameters_tidal_energy on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_tidal_energy')

        # Removing M2M table for field input_parameters_wind_energy on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_wind_energy')

        # Removing M2M table for field input_parameters_wave_energy on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_wave_energy')

        # Removing M2M table for field input_parameters_offshore_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_offshore_conservation')

        # Removing M2M table for field input_parameters_nearshore_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_nearshore_conservation')

        # Removing M2M table for field input_parameters_water_column_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_water_column_conservation')

        # Removing M2M table for field input_parameters_shoreside_development on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_shoreside_development')

        # Removing M2M table for field input_parameters_shellfish_aquaculture on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_shellfish_aquaculture')

        # Removing M2M table for field input_parameters_offshore_fishing on 'Scenario'
        db.delete_table('scenario_scenario_input_parameters_offshore_fishing')

        # Removing M2M table for field input_substrate_tidal_energy on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_tidal_energy')

        # Removing M2M table for field input_substrate_wave_energy on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_wave_energy')

        # Removing M2M table for field input_substrate_wind_energy on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_wind_energy')

        # Removing M2M table for field input_substrate_offshore_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_offshore_conservation')

        # Removing M2M table for field input_substrate_nearshore_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_nearshore_conservation')

        # Removing M2M table for field input_substrate_water_column_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_water_column_conservation')

        # Removing M2M table for field input_substrate_shoreside_development on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_shoreside_development')

        # Removing M2M table for field input_substrate_shellfish_aquaculture on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_shellfish_aquaculture')

        # Removing M2M table for field input_substrate_offshore_fishing on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_offshore_fishing')

        # Adding field 'MultiObjectiveScenario.input_dist_port_development'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_development'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_development'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_development'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_tidal_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_tidal_energy')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_tidal_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_tidal_energy')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_tidal_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_tidal_energy')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_tidal_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_tidal_energy')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_wind_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_wind_energy')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_wind_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_wind_energy')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_wind_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_wind_energy')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_wind_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_wind_energy')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_wave_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_wave_energy')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_wave_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_wave_energy')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_wave_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_wave_energy')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_wave_energy'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_wave_energy')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_offshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_offshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_offshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_offshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_offshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_offshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_offshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_offshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_nearshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_nearshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_nearshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_nearshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_nearshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_nearshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_nearshore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_nearshore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_water_column_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_water_column_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_water_column_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_water_column_conservation')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_water_column_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_water_column_conservation')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_water_column_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_water_column_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_shoreside_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_shoreside_development')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_shoreside_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_shoreside_development')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_shoreside_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_shoreside_development')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_shoreside_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_shoreside_development')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_shellfish_aquaculture'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_shellfish_aquaculture')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_shellfish_aquaculture'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_shellfish_aquaculture')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_shellfish_aquaculture'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_shellfish_aquaculture')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_shellfish_aquaculture'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_shellfish_aquaculture')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_offshore_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_offshore_fishing')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_offshore_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_offshore_fishing')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_offshore_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_offshore_fishing')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_offshore_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_offshore_fishing')

        # Adding M2M table for field input_substrate_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('conservationsubstrate', models.ForeignKey(orm['scenario.conservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_conservation', ['multiobjectivescenario_id', 'conservationsubstrate_id'])

        # Adding M2M table for field input_parameters_wind on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_wind', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('windparameter', models.ForeignKey(orm['scenario.windparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_wind', ['multiobjectivescenario_id', 'windparameter_id'])

        # Adding M2M table for field input_parameters_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('conservationparameter', models.ForeignKey(orm['scenario.conservationparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_conservation', ['multiobjectivescenario_id', 'conservationparameter_id'])

        # Adding M2M table for field input_parameters_shellfish on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_shellfish', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shellfishparameter', models.ForeignKey(orm['scenario.shellfishparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_shellfish', ['multiobjectivescenario_id', 'shellfishparameter_id'])

        # Adding M2M table for field input_substrate_shellfish on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_shellfish', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('shellfishsubstrate', models.ForeignKey(orm['scenario.shellfishsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_shellfish', ['multiobjectivescenario_id', 'shellfishsubstrate_id'])

        # Adding M2M table for field input_substrate_fishing on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('fishingsubstrate', models.ForeignKey(orm['scenario.fishingsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_fishing', ['multiobjectivescenario_id', 'fishingsubstrate_id'])

        # Adding M2M table for field input_substrate_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('developmentsubstrate', models.ForeignKey(orm['scenario.developmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_development', ['multiobjectivescenario_id', 'developmentsubstrate_id'])

        # Adding M2M table for field input_parameters_tidal on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_tidal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalparameter', models.ForeignKey(orm['scenario.tidalparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_tidal', ['multiobjectivescenario_id', 'tidalparameter_id'])

        # Adding M2M table for field input_substrate_tidal on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_tidal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalsubstrate', models.ForeignKey(orm['scenario.tidalsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_tidal', ['multiobjectivescenario_id', 'tidalsubstrate_id'])

        # Adding M2M table for field input_parameters_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('developmentparameter', models.ForeignKey(orm['scenario.developmentparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_development', ['multiobjectivescenario_id', 'developmentparameter_id'])

        # Adding M2M table for field input_substrate_wind on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_wind', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('windsubstrate', models.ForeignKey(orm['scenario.windsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_wind', ['multiobjectivescenario_id', 'windsubstrate_id'])

        # Adding M2M table for field input_parameters_fishing on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_parameters_fishing', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('fishingparameter', models.ForeignKey(orm['scenario.fishingparameter'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_parameters_fishing', ['multiobjectivescenario_id', 'fishingparameter_id'])

        # Removing M2M table for field input_parameters_tidal_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_tidal_energy')

        # Removing M2M table for field input_substrate_tidal_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_tidal_energy')

        # Removing M2M table for field input_parameters_wind_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_wind_energy')

        # Removing M2M table for field input_substrate_wind_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_wind_energy')

        # Removing M2M table for field input_parameters_wave_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_wave_energy')

        # Removing M2M table for field input_substrate_wave_energy on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_wave_energy')

        # Removing M2M table for field input_parameters_offshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_offshore_cf012')

        # Removing M2M table for field input_substrate_offshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_offshore_cocdc2')

        # Removing M2M table for field input_parameters_nearshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_nearshore_63d6')

        # Removing M2M table for field input_substrate_nearshore_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_nearshore_c5cf5')

        # Removing M2M table for field input_parameters_water_column_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_water_colufc6f')

        # Removing M2M table for field input_substrate_water_column_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_water_columde71')

        # Removing M2M table for field input_parameters_shoreside_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_shoreside_eb56')

        # Removing M2M table for field input_substrate_shoreside_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_shoreside_d2510')

        # Removing M2M table for field input_parameters_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_shellfish_4669')

        # Removing M2M table for field input_substrate_shellfish_aquaculture on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_shellfish_a0000')

        # Removing M2M table for field input_parameters_offshore_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_parameters_offshore_f4ee9')

        # Removing M2M table for field input_substrate_offshore_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_offshore_fi69e4')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
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
        'scenario.multiobjectivescenario': {
            'Meta': {'object_name': 'MultiObjectiveScenario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scenario_multiobjectivescenario_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
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
            'input_objectives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['scenario.Objective']", 'null': 'True', 'blank': 'True'}),
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
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'scenario_multiobjectivescenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'support_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scenario_multiobjectivescenario_related'", 'to': "orm['auth.User']"})
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
