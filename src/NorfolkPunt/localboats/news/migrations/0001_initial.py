# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('news_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('news', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('news_news')


    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']
