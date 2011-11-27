# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Place'
        db.create_table('localboats_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('localboats', ['Place'])

        # Adding model 'Person'
        db.create_table('localboats_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('localboats', ['Person'])

        # Adding model 'Boatbuilder'
        db.create_table('localboats_boatbuilder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('localboats', ['Boatbuilder'])

        # Adding model 'Designer'
        db.create_table('localboats_designer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('localboats', ['Designer'])

        # Adding model 'Design'
        db.create_table('localboats_design', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='designed', blank=True, to=orm['localboats.Designer'])),
        ))
        db.send_create_signal('localboats', ['Design'])

        # Adding model 'Construction'
        db.create_table('localboats_construction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('localboats', ['Construction'])

        # Adding model 'Boat'
        db.create_table('localboats_boat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sail_number', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('loa', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('handicap', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('construction', self.gf('django.db.models.fields.related.ForeignKey')(related_name='examples', blank=True, to=orm['localboats.Construction'])),
            ('year_built', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('builder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='built', blank=True, to=orm['localboats.Boatbuilder'])),
            ('design', self.gf('django.db.models.fields.related.ForeignKey')(related_name='examples', blank=True, to=orm['localboats.Design'])),
            ('previous_names', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('localboats', ['Boat'])

        # Adding unique constraint on 'Boat', fields ['name', 'sail_number']
        db.create_unique('localboats_boat', ['name', 'sail_number'])

        # Adding model 'Note'
        db.create_table('localboats_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('refers_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notes', to=orm['localboats.Boat'])),
        ))
        db.send_create_signal('localboats', ['Note'])

        # Adding model 'Ownership'
        db.create_table('localboats_ownership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('boat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ownership', to=orm['localboats.Boat'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localboats.Person'])),
            ('owned_from', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('owned_to', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('localboats', ['Ownership'])

        # Adding model 'Picture'
        db.create_table('localboats_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='picture_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('created', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('localboats', ['Picture'])

        # Adding model 'BoatDepiction'
        db.create_table('localboats_boatdepiction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localboats.Picture'])),
            ('top', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('left', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='depictions', to=orm['localboats.Boat'])),
        ))
        db.send_create_signal('localboats', ['BoatDepiction'])

        # Adding model 'PersonDepiction'
        db.create_table('localboats_persondepiction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localboats.Picture'])),
            ('top', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('left', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='depictions', to=orm['localboats.Person'])),
        ))
        db.send_create_signal('localboats', ['PersonDepiction'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Boat', fields ['name', 'sail_number']
        db.delete_unique('localboats_boat', ['name', 'sail_number'])

        # Deleting model 'Place'
        db.delete_table('localboats_place')

        # Deleting model 'Person'
        db.delete_table('localboats_person')

        # Deleting model 'Boatbuilder'
        db.delete_table('localboats_boatbuilder')

        # Deleting model 'Designer'
        db.delete_table('localboats_designer')

        # Deleting model 'Design'
        db.delete_table('localboats_design')

        # Deleting model 'Construction'
        db.delete_table('localboats_construction')

        # Deleting model 'Boat'
        db.delete_table('localboats_boat')

        # Deleting model 'Note'
        db.delete_table('localboats_note')

        # Deleting model 'Ownership'
        db.delete_table('localboats_ownership')

        # Deleting model 'Picture'
        db.delete_table('localboats_picture')

        # Deleting model 'BoatDepiction'
        db.delete_table('localboats_boatdepiction')

        # Deleting model 'PersonDepiction'
        db.delete_table('localboats_persondepiction')


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
            'boats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'pictures'", 'blank': 'True', 'through': "orm['localboats.BoatDepiction']", 'to': "orm['localboats.Boat']"}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'picture_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'pictures'", 'blank': 'True', 'through': "orm['localboats.PersonDepiction']", 'to': "orm['localboats.Person']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
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
