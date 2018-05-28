# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import (
    BlogLabel,
    BlogArticle
)

# Create your views here.

def blog_label(request):
    labels = BlogLabel.objects.all()
    # print type(labels)
    return render(request, 'blog/index.html', {'labels': labels})

def blog_article(request, label_id):
    dirs = BlogArticle.objects.filter(label_id=label_id)
    labels = BlogLabel.objects.all()
    # print dirs
    return render(request, 'blog/index.html', {'dirs': dirs, 'labels': labels})


