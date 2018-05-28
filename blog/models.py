# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BlogLabel(models.Model):
    name = models.CharField(max_length=200)
    describe = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='labels_author')
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    label = models.ForeignKey('BlogLabel', on_delete=models.CASCADE, related_name='blog_labels')
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title





