#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/4/25 下午7:40
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : urls.py


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_label, name='blog_label'),
    url(r'(?P<label_id>\d)/$', views.blog_article, name='blog_article'),
]


