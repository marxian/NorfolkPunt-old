# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Picture.event'
        db.add_column('localboats_picture', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'], null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Picture.event'
        db.delete_column('localboats_picture', 'event_id')

    models = {
        'events.event': {
            'Meta': {'ordering': "['-start']", 'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'events'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['events.EventFlag']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'to': "orm['localboats.Place']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['events.EventType']"})
        },
        'events.eventflag': {
            'Meta': {'object_name': 'EventFlag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.eventtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'EventType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'licenses.license': {
            'Meta': {'ordering': "('name',)", 'object_name': 'License'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'licenses'", 'null': 'True', 'to': "orm['licenses.Organization']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'licenses.organization': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organization'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
            'preferred_pic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localboats.Picture']", 'null': 'True', 'blank': 'True'}),
            'previous_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sail_number': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'year_built': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'localboats.boatbuilder': {
            'Meta': {'ordering': "['name']", 'object_name': 'Boatbuilder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'localboats.boatdepiction': {
            'Meta': {'object_name': 'BoatDepiction'},
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localboats.Picture']"}),
            'left': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'depictions'", 'to': "orm['localboats.Boat']"}),
            'top': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
        'localboats.note': {
            'Meta': {'object_name': 'Note'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refers_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notes'", 'to': "orm['localboats.Boat']"}),
            'text': ('django.db.models.fields.TextField', [], {})
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
        'localboats.persondepiction': {
            'Meta': {'object_name': 'PersonDepiction'},
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localboats.Picture']"}),
            'left': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'depictions'", 'to': "orm['localboats.Person']"}),
            'top': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'localboats.picture': {
            'Meta': {'object_name': 'Picture'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'attribution': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photographs'", 'blank': 'True', 'to': "orm['localboats.Person']"}),
            'boats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'pictures'", 'blank': 'True', 'through': "orm['localboats.BoatDepiction']", 'to': "orm['localboats.Boat']"}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'picture_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'blank': 'True', 'to': "orm['licenses.License']"}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'pictures'", 'blank': 'True', 'through': "orm['localboats.PersonDepiction']", 'to': "orm['localboats.Person']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['localboats']