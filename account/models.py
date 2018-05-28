# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)  #unique =True 代表全表唯一的
    birth = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

class UserInfo(models.Model):
    user =models.OneToOneField(User, unique=True)
    school = models.CharField(max_length=50, blank=True) # 允许该字段为空值
    company = models.CharField(max_length=50, blank=True)
    profession = models.CharField()
