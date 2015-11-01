# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portfolio'
        db.create_table(u'new_foto_app_portfolio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('razdel', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('outer_image', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('alternateName', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('index', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, unique=True)),
        ))
        db.send_create_signal(u'new_foto_app', ['Portfolio'])

        # Adding model 'PortfolioVideo'
        db.create_table(u'new_foto_app_portfoliovideo', (
            (u'portfolio_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['new_foto_app.Portfolio'], unique=True, primary_key=True)),
            ('video', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('player', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'new_foto_app', ['PortfolioVideo'])

        # Adding model 'Articles'
        db.create_table(u'new_foto_app_articles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('url_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('shot_text', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'new_foto_app', ['Articles'])

        # Adding model 'Blog'
        db.create_table(u'new_foto_app_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/temporary-anavailable.png', max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=2000)),
        ))
        db.send_create_signal(u'new_foto_app', ['Blog'])

        # Adding unique constraint on 'Blog', fields ['caption', 'date']
        db.create_unique(u'new_foto_app_blog', ['caption', 'date'])

        # Adding model 'BlogImage'
        db.create_table(u'new_foto_app_blogimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['new_foto_app.Blog'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='images/temporary_anavailable.png', max_length=100, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'new_foto_app', ['BlogImage'])

        # Adding model 'BlogImageUpdated'
        db.create_table(u'new_foto_app_blogimageupdated', (
            (u'blogimage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['new_foto_app.BlogImage'], unique=True, primary_key=True)),
            ('fotki', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal(u'new_foto_app', ['BlogImageUpdated'])

        # Adding model 'TestNewFotoApp'
        db.create_table(u'new_foto_app_testnewfotoapp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'new_foto_app', ['TestNewFotoApp'])


    def backwards(self, orm):
        # Removing unique constraint on 'Blog', fields ['caption', 'date']
        db.delete_unique(u'new_foto_app_blog', ['caption', 'date'])

        # Deleting model 'Portfolio'
        db.delete_table(u'new_foto_app_portfolio')

        # Deleting model 'PortfolioVideo'
        db.delete_table(u'new_foto_app_portfoliovideo')

        # Deleting model 'Articles'
        db.delete_table(u'new_foto_app_articles')

        # Deleting model 'Blog'
        db.delete_table(u'new_foto_app_blog')

        # Deleting model 'BlogImage'
        db.delete_table(u'new_foto_app_blogimage')

        # Deleting model 'BlogImageUpdated'
        db.delete_table(u'new_foto_app_blogimageupdated')

        # Deleting model 'TestNewFotoApp'
        db.delete_table(u'new_foto_app_testnewfotoapp')


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
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'unique': 'True'}),
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