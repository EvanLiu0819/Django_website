#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time     : 2018/4/28 下午2:35
# @Author   : Evan Liu
# @Email    : liuzhihao@growingio.com
# @File     : forms.py

from django import forms
from django.contrib.auth.models import User  #Django默认用户模型User类
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '请输入你的用户名'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '请输入你的密码'}))

class RegistrationForm(forms.ModelForm):  #相比前面的forms.Form有区别，如果表单的数据写入数据或者修改使用ModelForm模块
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:  #Django内部类，声明表单中使用的数据模型
        model = User  #user表的username和email字段
        fields = ('username', 'email')

    def clean_password2(self):  #以clean_+ 属性的名称会有is_valid()的功能，检查数据是否合法
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password is not match.')
        return cd['password2']


class UserprofileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')





