#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/4/28 下午2:29
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : urls.py

from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'login/$', views.user_login, name='user_login'),
    # url(r'login/$', auth_views.login, name='user_login'),
    url(r'logout/$', auth_views.logout, {'template_name': 'account/logout.html'}, name='user_logout'),
    url(r'register/$', views.register, name='user_register'),
    # 用户需要登陆后才能访问这个页面否则无法访问
    url(r'password-change/', auth_views.password_change, {'post_change_redirect': '/account/password-change/'}, name='password_change'),
    # url(r'password-change/', views.password_change, name='password_change'),
    url(r'password-change-done/$', auth_views.password_change_done, name='password_change-done'),
]






