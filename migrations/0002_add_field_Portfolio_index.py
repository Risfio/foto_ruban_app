# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Portfolio.index'
        db.add_column(u'new_foto_app_portfolio', 'index',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Portfolio.index'
        db.delete_column(u'new_foto_app_portfolio', 'index')


    models = {
        u'new_foto_app.articles': {
            'Meta': {'ordering': "['date']", 'object_name': 'Articles'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'shot_text': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'url_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'new_foto_app.blog': {
            'Meta': {'ordering': "['-date']", 'unique_together': "(('caption', 'date'),)", 'object_name': 'Blog'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/temporary-anavailable.png'", 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '2000'})
        },
        u'new_foto_app.blogimage': {
            'Meta': {'object_name': 'BlogImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/temporary_anavailable.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['new_foto_app.Blog']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'})
        },
        u'new_foto_app.blogimageupdated': {
            'Meta': {'object_name': 'BlogImageUpdated', '_ormbases': [u'new_foto_app.BlogImage']},
            u'blogimage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['new_foto_app.BlogImage']", 'unique': 'True', 'primary_key': 'True'}),
            'fotki': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        u'new_foto_app.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'alternateName': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'outer_image': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'razdel': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'new_foto_app.portfoliovideo': {
            'Meta': {'object_name': 'PortfolioVideo', '_ormbases': [u'new_foto_app.Portfolio']},
            'player': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"}),
            u'portfolio_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['new_foto_app.Portfolio']", 'unique': 'True', 'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"})
        },
        u'new_foto_app.testnewfotoapp': {
            'Meta': {'object_name': 'TestNewFotoApp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['new_foto_app']