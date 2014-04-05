from django.contrib import admin

from django.conf import settings

from .models import Portfolio
from .models import Articles
from .models import Blog
from .models import BlogImage
from .models import PortfolioVideo

# Register your models here.


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    fields = ('caption', 'image', 'date', 'text')
    inlines = [BlogImageInline]



class PortfolioVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'alternateName')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'alternateName')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Articles)
admin.site.register(PortfolioVideo, PortfolioVideoAdmin)


# testings
if settings.DEBUG:
    from .models import TestNewFotoApp
    admin.site.register(TestNewFotoApp)
