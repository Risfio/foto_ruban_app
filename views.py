# -*- coding:utf-8 -*-

from datetime import date
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# importing all available models
from .models import Portfolio
from .models import portfolio_choices
from .models import Articles
from .models import Blog
from .models import BlogImage
from .models import PortfolioVideo

from .models import TestNewFotoApp
# Create your views here.


def index(request):
    title = u'Свадебный фотограф в Москве.Рубан Илья.'
    return render(request, 'index.html', {'title': title})
    #from django.http import HttpResponse
    #return HttpResponse('helllo')


def get_page(get_query, num_per_page, tottal):
    page = get_query.get('page')
    items = []
    paginator = Paginator(tottal, num_per_page, allow_empty_first_page=True)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return items, paginator.page_range


def portfolio(request, razdel):
    template_file = 'portfolio.html'
    # set page title
    title_choices = (
        ('portreit', u'портретная съемка'),
        ('lovestory', u'лавстори'),
        ('semeynie', u'семейная фотография'),
        ('svadbi', u'свадьбы'),
	('video', u'Видео'),
    )
    keywords_choices = (
	('portreit', u'Портретная фотография.Лучшие фотопортреты'),
	('lovestory', u'Love Story.Лавстори.Фотографии прогулок влюбленных пар.'),
	('semeynie', u'Семейные фотографии.Фотосессии семейных торжеств, фото семейных мероприятий, семейная фотосессия.'),
	('svadbi', u'Свадебные фотографии.Фото со свадеб.Серии фото свадебных мероприятий.'),
	('video', u'Видео свадебные фотосессии, постановочное фото,видео о работе фотографа.'),
    )
    description_choices = (
	('portreit', u'Галлерея портретной фотографии'),
	('lovestory', u'Фотосессия в стиле Лавстори LoveStory'),
	('semeynie', u'Семейные фотосессии с професиональным фотографом'),
	('svadbi', u'Профессиональная свадебная съемка.'),
	('video', u'Видео о работе фотографа и видеослайдшоу.'),
    )

    def get_title(input, choices):
        return [rus for en, rus in choices if en == input][0] or None

    # end debug
    items = []
    # if url not endthwith '?page=' - set page to 1
    page = request.GET.get('page') or 1
    pages = []
    get_active = lambda x, current: x == current and True or False
    if not razdel is None:
        for razdel_id, razdel_name in portfolio_choices:
            if razdel_name == razdel:
		if razdel == 'video':
		    template_file = 'portfolio_video.html'
		    items, num_pages = get_page(request.GET, 20, PortfolioVideo.objects.filter(razdel=razdel_id))
		elif razdel != 'video':
		    items, num_pages = get_page(request.GET, 40, Portfolio.objects.filter(razdel=razdel_id))
                pages = [{'url': '?page=' + str(num), 'text': num, 'active': get_active(num, int(page))} for num in num_pages]
    elif razdel is None:
        items, num_pages = get_page(request.GET, 2, Portfolio.objects.filter(razdel=1))
        pages = [{'url': '?page=' + str(num), 'text': num, 'active': get_active(num, 1)} for num in num_pages]
    #return render(request, template_file, {'items': items,
    return render(request, template_file, {'items': sorted(items, key=lambda x: x.index),
					      'keywords': get_title(razdel, keywords_choices),
					      'description': get_title(razdel, description_choices),
                                              'paginator': pages,
                                              'title': get_title(razdel, title_choices)})


def articles(request, articles=None):
	# Head html attributes
	title, description, keywords = None, None, None
	# End head attributes declaration
	get_active = lambda x, current: x == current and True or False
	article = None
	articles_list = None
	pages = None
	if articles is None:
		articles_list, num_pages = get_page(request.GET, 2, Articles.objects.all())
		pages = [{'url': '?page=' + str(num), 'text': num, 'active': get_active(num, 1)} for num in num_pages]
		title = u'Статьи на тему свадебной фотографии и на сопутствующие работе фотографа темы'
	elif not articles is None:
		article = Articles.objects.get(url_name=' '.join(articles.split('-')))
		title = u'Статья ' + article.caption;
	return render(request, 'articles.html', {'articles': articles_list, 
		'article': article, 
		'paginator': pages,
		'title': title,})


def blog(request):
    get_active = lambda x, current: x == current and True or False
    page = 1
    if not request.GET.get('page') is None:
        page = int(request.GET.get('page'))
    paginator = Paginator(Blog.objects.all(), 8)
    posts = paginator.page(page)
    for post in posts:
        post.url = post.get_absolute_url()
    return render(request, "blog.html", 
                  {'posts': posts,
                   'paginator': [{'url': '?page=' + str(num), 'text': num, 'active': get_active(num, page)} for num in range(1, paginator.num_pages + 1)]
		  })


def blog_entryes(request, data):
#    get_active = lambda x, current: x == current and True or False
    year, month, day = data.split('-')
#    page = 1
#    if not request.GET.get('page') is None:
#        page = int(request.GET.get('page'))
    post = Blog.objects.get(date=date(year=int(year), month=int(month), day=int(day)))
#    paginator = Paginator(BlogImage.objects.filter(post=post), 8, allow_empty_first_page=True)
    return render(request, "blog_post.html",
                  {'post': post,
				   'entryes': BlogImage.objects.filter(post=post),
#                  'entryes': paginator.page(page),
#                  'paginator': [{'url': '?page=' + str(num), 'text': num, 'active': get_active(num, int(page))} for num in range(1, paginator.num_pages + 1)]
		})
