# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.pub_date'
        db.add_column('news_news', 'pub_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 3, 0, 0)),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'News.pub_date'
        db.delete_column('news_news', 'pub_date')

    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']