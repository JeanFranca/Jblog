from django.contrib import admin
#from .models import Category
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('published_at', 'title')

admin.site.register(Article, ArticleAdmin)