# -*- coding:utf-8 -*-

import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Manager
from django.db.models.signals import pre_save

# Create your models here.


portfolio_choices = [
    (1, 'lovestory'),
    (2, 'svadbi'),
    (3, 'portreit'),
    (4, 'semeynie'),
	(5, 'video'),
]

class Portfolio(models.Model):
    razdel = models.PositiveIntegerField(null=False, choices=portfolio_choices, verbose_name=u'Номер раздела')
    image = models.ImageField(upload_to='media/', verbose_name=u'Изображение', blank=True, null=True)
    outer_image = models.CharField(max_length=1024, blank=True, verbose_name=u'Ссылка на изображение, если картинка на \
                                                                             внешнем ресурсе - типа яндекс фотки')
    alternateName = models.CharField(max_length=256, verbose_name= u'Содержимое тега альт! Надо поменять на schema.org аттрибут')
    index = models.PositiveIntegerField(default=0)
    #video = models.CharField(max_length=1024, verbose_name = u'Видео', null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return '/portfolio/%s/%i' % (self.razdel, self.id)

class PortfolioVideo(Portfolio):
    # video field contains just iframe code from youtube
    video = models.CharField(max_length="1024", blank=False)
    # player url - needed for sitemap.xml
    player = models.CharField(max_length="1024", blank=False)
    thumbnail = models.ImageField(upload_to='media/tumbnails/', null=True, blank=True)

def fix_youtube_link(sender, instance, *args, **kwargs):
    pat = re.compile(r'.*src=?((\").+(\"))')
    parts = []
    for part in instance.video.split(' '):
	result = re.match(pat, part)
	if not result is None:
	    part = part[:-1] + u'?wmode=opaque"'
	parts.append(part)
    instance.video = ' '.join(parts)
    return instance.video

pre_save.connect(fix_youtube_link, PortfolioVideo)

class Articles(models.Model):
    date = models.DateTimeField(verbose_name='Creating date', auto_now=True)
    caption = models.CharField(max_length=256, verbose_name="Caption")
    url_name = models.CharField(max_length=256, verbose_name="Same as caption , but in translit")
    shot_text = models.CharField(max_length=1024, verbose_name="Short part of text")
    text = models.TextField(max_length=10000, verbose_name="Article text")
    image = models.ImageField(upload_to='media/')
    image_thumbnail = models.ImageField(upload_to='media/thumbnails/')

    def get_absolute_url(self):
        return "/articles/%s/" % '-'.join(self.url_name.split(' '))

    def get_full_article_link(self):
        pass

    def __str__(self):
        return ' '.join(['[', self.date.isoformat(), ']', self.caption])

    def __unicode__(self):
        return self.__str__()

    class Meta:
        ordering = ['date']


class Blog(models.Model):
    caption = models.CharField(max_length=64)
    image = models.ImageField(upload_to='media/', default="images/temporary-anavailable.png")
    date = models.DateField(auto_now=False)
    text = models.TextField(max_length=2000)

    def get_absolute_url(self):
        return str(self.date)

    def __unicode__(self):
        return self.caption

    class Meta:
        unique_together = (('caption', 'date'),)
        ordering = ['-date']


class BlogImage(models.Model):
    post = models.ForeignKey(Blog)
    image = models.ImageField(upload_to='media/', verbose_name=_(u'Image'),
                              default='images/temporary_anavailable.png',
                              blank=True, null=True)
    text = models.TextField(max_length=2000, verbose_name=_(u'Text for image'), blank=True, null=True)


class BlogImageUpdated(BlogImage):
	fotki = models.CharField(max_length=512, blank=True, null=True)


# end of testings
class TestNewFotoApp(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='media/')
