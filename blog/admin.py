# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    BlogArticle,
    BlogLabel
)

# Register your models here.

class BlogLabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publish', 'describe')
    list_filter = ('name', 'author')
    search_fields = ('name', 'author')
    # raw_id_fields =
    date_hierarchy = 'publish'
    ordering = ['publish', 'author']


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title',)
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['publish', 'author']

admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(BlogLabel, BlogLabelAdmin)

