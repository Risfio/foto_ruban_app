# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'Creating date')),
                ('caption', models.CharField(max_length=256, verbose_name=b'Caption')),
                ('url_name', models.CharField(max_length=256, verbose_name=b'Same as caption , but in translit')),
                ('shot_text', models.CharField(max_length=1024, verbose_name=b'Short part of text')),
                ('text', models.TextField(max_length=10000, verbose_name=b'Article text')),
                ('image', models.ImageField(upload_to=b'media/')),
                ('image_thumbnail', models.ImageField(upload_to=b'media/thumbnails/')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=64)),
                ('image', models.ImageField(default=b'images/temporary-anavailable.png', upload_to=b'media/')),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=2000)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default=b'images/temporary_anavailable.png', upload_to=b'media/', null=True, verbose_name='Image', blank=True)),
                ('text', models.TextField(max_length=2000, null=True, verbose_name='Text for image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'media/', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
                ('outer_image', models.CharField(max_length=1024, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435, \u0435\u0441\u043b\u0438 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043d\u0430                                                                              \u0432\u043d\u0435\u0448\u043d\u0435\u043c \u0440\u0435\u0441\u0443\u0440\u0441\u0435 - \u0442\u0438\u043f\u0430 \u044f\u043d\u0434\u0435\u043a\u0441 \u0444\u043e\u0442\u043a\u0438', blank=True)),
                ('alternateName', models.CharField(max_length=256, verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0442\u0435\u0433\u0430 \u0430\u043b\u044c\u0442! \u041d\u0430\u0434\u043e \u043f\u043e\u043c\u0435\u043d\u044f\u0442\u044c \u043d\u0430 schema.org \u0430\u0442\u0442\u0440\u0438\u0431\u0443\u0442')),
                ('index', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestNewFotoApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to=b'media/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImageUpdated',
            fields=[
                ('blogimage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='new_foto_app.BlogImage')),
                ('fotki', models.CharField(max_length=512, null=True, blank=True)),
            ],
            bases=('new_foto_app.blogimage',),
        ),
        migrations.CreateModel(
            name='PortfolioVideo',
            fields=[
                ('portfolio_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='new_foto_app.Portfolio')),
                ('video', models.CharField(max_length=b'1024')),
                ('player', models.CharField(max_length=b'1024')),
                ('thumbnail', models.ImageField(null=True, upload_to=b'media/tumbnails/', blank=True)),
            ],
            bases=('new_foto_app.portfolio',),
        ),
        migrations.AddField(
            model_name='blogimage',
            name='post',
            field=models.ForeignKey(to='new_foto_app.Blog'),
        ),
        migrations.AlterUniqueTogether(
            name='blog',
            unique_together=set([('caption', 'date')]),
        ),
    ]
