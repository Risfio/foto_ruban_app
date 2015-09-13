from django.contrib import admin

from django.conf import settings

from .models import Portfolio
from .models import Articles
from .models import Blog
from .models import BlogImage
from .models import BlogImageUpdated
from .models import PortfolioVideo

# Register your models here.

# Trying yandex fotki
class BlogImageUpdAdmin(admin.ModelAdmin):
	model = BlogImageUpdated


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    fields = ('caption', 'image', 'date', 'text')
    inlines = [BlogImageInline]



class PortfolioVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'alternateName')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'alternateName', 'index', 'razdel')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Articles)
admin.site.register(PortfolioVideo, PortfolioVideoAdmin)

# Addin yandex fotki link
admin.site.register(BlogImageUpdated, BlogImageUpdAdmin)


# testings
if settings.DEBUG:
    from .models import TestNewFotoApp
    admin.site.register(TestNewFotoApp)
