# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EventType'
        db.create_table('events_eventtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('events', ['EventType'])

        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['events.EventType'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hosts', to=orm['localboats.Place'])),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal('events', ['Event'])

        # Adding model 'RaceResult'
        db.create_table('events_raceresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='results', to=orm['events.Event'])),
            ('report', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('full_results', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('events', ['RaceResult'])

        # Adding model 'RaceTrophy'
        db.create_table('events_racetrophy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('boat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='race_trophies', to=orm['localboats.Boat'])),
            ('helm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='helming_trophies', to=orm['localboats.Person'])),
            ('crew', self.gf('django.db.models.fields.related.ForeignKey')(related_name='crewing_tropies', to=orm['localboats.Person'])),
            ('raceresult', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trophies', to=orm['events.RaceResult'])),
        ))
        db.send_create_signal('events', ['RaceTrophy'])

        # Adding model 'RacePosition'
        db.create_table('events_raceposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('boat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='race_positions', to=orm['localboats.Boat'])),
            ('helm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='helming_positions', to=orm['localboats.Person'])),
            ('crew', self.gf('django.db.models.fields.related.ForeignKey')(related_name='crewing_positions', to=orm['localboats.Person'])),
            ('points', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('raceresult', self.gf('django.db.models.fields.related.ForeignKey')(related_name='positions', to=orm['events.RaceResult'])),
        ))
        db.send_create_signal('events', ['RacePosition'])


    def backwards(self, orm):
        
        # Deleting model 'EventType'
        db.delete_table('events_eventtype')

        # Deleting model 'Event'
        db.delete_table('events_event')

        # Deleting model 'RaceResult'
        db.delete_table('events_raceresult')

        # Deleting model 'RaceTrophy'
        db.delete_table('events_racetrophy')

        # Deleting model 'RacePosition'
        db.delete_table('events_raceposition')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'to': "orm['localboats.Place']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['events.EventType']"})
        },
        'events.eventtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'EventType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.raceposition': {
            'Meta': {'object_name': 'RacePosition'},
            'boat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'race_positions'", 'to': "orm['localboats.Boat']"}),
            'crew': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crewing_positions'", 'to': "orm['localboats.Person']"}),
            'helm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'helming_positions'", 'to': "orm['localboats.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'raceresult': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': "orm['events.RaceResult']"})
        },
        'events.raceresult': {
            'Meta': {'object_name': 'RaceResult'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['events.Event']"}),
            'full_results': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'events.racetrophy': {
            'Meta': {'object_name': 'RaceTrophy'},
            'boat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'race_trophies'", 'to': "orm['localboats.Boat']"}),
            'crew': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crewing_tropies'", 'to': "orm['localboats.Person']"}),
            'helm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'helming_trophies'", 'to': "orm['localboats.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'raceresult': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trophies'", 'to': "orm['events.RaceResult']"})
        },
        'localboats.boat': {
            'Meta': {'ordering': "['-sail_number']", 'unique_together': "(('name', 'sail_number'),)", 'object_name': 'Boat'},
            'builder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'built'", 'blank': 'True', 'to': "orm['localboats.Boatbuilder']"}),
            'construction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'examples'", 'blank': 'True', 'to': "orm['localboats.Construction']"}),
            'design': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'examples'", 'blank': 'True', 'to': "orm['localboats.Design']"}),
            'handicap': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loa': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localboats.Person']", 'symmetrical': 'False', 'through': "orm['localboats.Ownership']", 'blank': 'True'}),
            'previous_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sail_number': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'year_built': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'localboats.boatbuilder': {
            'Meta': {'ordering': "['name']", 'object_name': 'Boatbuilder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'localboats.construction': {
            'Meta': {'object_name': 'Construction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'localboats.design': {
            'Meta': {'ordering': "['name']", 'object_name': 'Design'},
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'designed'", 'blank': 'True', 'to': "orm['localboats.Designer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'localboats.designer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Designer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'localboats.ownership': {
            'Meta': {'ordering': "['-owned_from', '-owned_to']", 'object_name': 'Ownership'},
            'boat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ownership'", 'to': "orm['localboats.Boat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owned_from': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owned_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localboats.Person']"})
        },
        'localboats.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'localboats.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['events']
