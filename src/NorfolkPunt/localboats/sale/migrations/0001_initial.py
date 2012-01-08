# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Sale'
        db.create_table('sale_sale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('contact', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('details', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('boat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='forsale', blank=True, to=orm['localboats.Boat'])),
        ))
        db.send_create_signal('sale', ['Sale'])


    def backwards(self, orm):
        
        # Deleting model 'Sale'
        db.delete_table('sale_sale')


    models = {
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
        'sale.sale': {
            'Meta': {'object_name': 'Sale'},
            'boat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forsale'", 'blank': 'True', 'to': "orm['localboats.Boat']"}),
            'contact': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sale']
