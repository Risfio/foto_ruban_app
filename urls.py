# -*- coding:utf-8 -*-

__author__ = 'Ivan'

from django.conf.urls import url, patterns
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', 'new_foto_app.views.index', name='index'),
                       url(r'^portfolio/$', 'new_foto_app.views.portfolio', name='portfolio'),
                       url(r'^video/$', 'new_foto_app.views.portfolio_videos', name='videos'),
                       url(r'^articles/$', 'new_foto_app.views.articles', name='articles-view'),
                       url(r'^articles/(?P<articles>[a-zA-Z\-]+)/$', 'new_foto_app.views.articles', name="article-concrete-view"),
                       url(r'^blog/$', 'new_foto_app.views.blog', name='blog-list-view'),
                       url(r'^blog/(?P<data>[\d\-]+)/$', 'new_foto_app.views.blog_entryes', name='blog-entryes'),
                       )

# flatpages

urlpatterns += patterns('django.contrib.flatpages.views',
                        url(r'^about-me/$', 'flatpage', {'url': '/about-me/'}, name='flatpage-about-us'),
                        url(r'^contacts/$', 'flatpage', {'url': '/contacts/'}, name='flat-contacts'),
			url(r'^prices/$', 'flatpage', {'url': '/prices/'}, name='flat-prices'),
      url(r'^confidentials/$', 'flatpage', {'url': '/confidentials/'}, name='confidentials'),
      url(r'^otzivi/$', 'flatpage', {'url': '/otzivi/'}, name='otzivi'),
)
