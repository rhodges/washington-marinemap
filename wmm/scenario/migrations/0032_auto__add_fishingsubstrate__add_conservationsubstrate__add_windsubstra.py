# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FishingSubstrate'
        db.create_table('scenario_fishingsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scenario', ['FishingSubstrate'])

        # Adding model 'ConservationSubstrate'
        db.create_table('scenario_conservationsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scenario', ['ConservationSubstrate'])

        # Adding model 'WindSubstrate'
        db.create_table('scenario_windsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scenario', ['WindSubstrate'])

        # Adding model 'TidalSubstrate'
        db.create_table('scenario_tidalsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scenario', ['TidalSubstrate'])

        # Adding model 'ShellfishSubstrate'
        db.create_table('scenario_shellfishsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scenario', ['ShellfishSubstrate'])

        # Adding model 'DevelopmentSubstrate'
        db.create_table('scenario_developmentsubstrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('substrate', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('scenario', ['DevelopmentSubstrate'])

        # Removing M2M table for field input_substrate on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate')

        # Adding M2M table for field input_substrate_tidal on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_tidal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('tidalsubstrate', models.ForeignKey(orm['scenario.tidalsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_tidal', ['scenario_id', 'tidalsubstrate_id'])

        # Adding M2M table for field input_substrate_wind on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_wind', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('windsubstrate', models.ForeignKey(orm['scenario.windsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_wind', ['scenario_id', 'windsubstrate_id'])

        # Adding M2M table for field input_substrate_conservation on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('conservationsubstrate', models.ForeignKey(orm['scenario.conservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_conservation', ['scenario_id', 'conservationsubstrate_id'])

        # Adding M2M table for field input_substrate_development on 'Scenario'
        db.create_table('scenario_scenario_input_substrate_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('developmentsubstrate', models.ForeignKey(orm['scenario.developmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate_development', ['scenario_id', 'developmentsubstrate_id'])

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

        # Adding field 'MultiObjectiveScenario.input_dist_shore_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_tidal'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_tidal', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_wind'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_wind', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_conservation'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_conservation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_development'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_development'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_development'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_development'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_development', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_shellfish'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_shellfish', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_shore_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_shore_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_dist_port_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_dist_port_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_min_depth_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_min_depth_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'MultiObjectiveScenario.input_max_depth_fishing'
        db.add_column('scenario_multiobjectivescenario', 'input_max_depth_fishing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding M2M table for field input_substrate_tidal on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_tidal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('tidalsubstrate', models.ForeignKey(orm['scenario.tidalsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_tidal', ['multiobjectivescenario_id', 'tidalsubstrate_id'])

        # Adding M2M table for field input_substrate_wind on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_wind', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('windsubstrate', models.ForeignKey(orm['scenario.windsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_wind', ['multiobjectivescenario_id', 'windsubstrate_id'])

        # Adding M2M table for field input_substrate_conservation on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_conservation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('conservationsubstrate', models.ForeignKey(orm['scenario.conservationsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_conservation', ['multiobjectivescenario_id', 'conservationsubstrate_id'])

        # Adding M2M table for field input_substrate_development on 'MultiObjectiveScenario'
        db.create_table('scenario_multiobjectivescenario_input_substrate_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('multiobjectivescenario', models.ForeignKey(orm['scenario.multiobjectivescenario'], null=False)),
            ('developmentsubstrate', models.ForeignKey(orm['scenario.developmentsubstrate'], null=False))
        ))
        db.create_unique('scenario_multiobjectivescenario_input_substrate_development', ['multiobjectivescenario_id', 'developmentsubstrate_id'])

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


    def backwards(self, orm):
        
        # Deleting model 'FishingSubstrate'
        db.delete_table('scenario_fishingsubstrate')

        # Deleting model 'ConservationSubstrate'
        db.delete_table('scenario_conservationsubstrate')

        # Deleting model 'WindSubstrate'
        db.delete_table('scenario_windsubstrate')

        # Deleting model 'TidalSubstrate'
        db.delete_table('scenario_tidalsubstrate')

        # Deleting model 'ShellfishSubstrate'
        db.delete_table('scenario_shellfishsubstrate')

        # Deleting model 'DevelopmentSubstrate'
        db.delete_table('scenario_developmentsubstrate')

        # Adding M2M table for field input_substrate on 'Scenario'
        db.create_table('scenario_scenario_input_substrate', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm['scenario.scenario'], null=False)),
            ('substrate', models.ForeignKey(orm['scenario.substrate'], null=False))
        ))
        db.create_unique('scenario_scenario_input_substrate', ['scenario_id', 'substrate_id'])

        # Removing M2M table for field input_substrate_tidal on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_tidal')

        # Removing M2M table for field input_substrate_wind on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_wind')

        # Removing M2M table for field input_substrate_conservation on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_conservation')

        # Removing M2M table for field input_substrate_development on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_development')

        # Removing M2M table for field input_substrate_shellfish on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_shellfish')

        # Removing M2M table for field input_substrate_fishing on 'Scenario'
        db.delete_table('scenario_scenario_input_substrate_fishing')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_tidal')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_tidal')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_tidal')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_tidal'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_tidal')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_wind')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_wind')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_wind')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_wind'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_wind')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_conservation')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_conservation')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_conservation'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_conservation')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_development')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_development')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_development')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_development'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_development')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_shellfish'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_shellfish')

        # Deleting field 'MultiObjectiveScenario.input_dist_shore_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_shore_fishing')

        # Deleting field 'MultiObjectiveScenario.input_dist_port_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_dist_port_fishing')

        # Deleting field 'MultiObjectiveScenario.input_min_depth_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_min_depth_fishing')

        # Deleting field 'MultiObjectiveScenario.input_max_depth_fishing'
        db.delete_column('scenario_multiobjectivescenario', 'input_max_depth_fishing')

        # Removing M2M table for field input_substrate_tidal on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_tidal')

        # Removing M2M table for field input_substrate_wind on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_wind')

        # Removing M2M table for field input_substrate_conservation on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_conservation')

        # Removing M2M table for field input_substrate_development on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_development')

        # Removing M2M table for field input_substrate_shellfish on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_shellfish')

        # Removing M2M table for field input_substrate_fishing on 'MultiObjectiveScenario'
        db.delete_table('scenario_multiobjectivescenario_input_substrate_fishing')


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
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'scenario.developmentparameter': {
            'Meta': {'object_name': 'DevelopmentParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.developmentsubstrate': {
            'Meta': {'object_name': 'DevelopmentSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'scenario.fishingparameter': {
            'Meta': {'object_name': 'FishingParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.Parameter']", 'null': 'True', 'blank': 'True'})
        },
        'scenario.fishingsubstrate': {
            'Meta': {'object_name': 'FishingSubstrate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'substrate': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['scenario']
