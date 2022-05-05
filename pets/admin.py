from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
