# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.template.response import TemplateResponse

from django.shortcuts import (
    render, redirect, resolve_url)
from django.http import (
    HttpResponse, HttpResponseRedirect)
from django.contrib.auth import (
    authenticate, login)
from .forms import (
    LoginForm, RegistrationForm, UserprofileForm)
from django.contrib.auth.forms import (
    PasswordChangeForm)


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                # return HttpResponse('Welcome You. You have been authenticate successfully.')
                return render(request, 'blog/index.html')
                # return HttpResponse('Welcome Login my website!')
            else:
                return HttpResponse('Invalid Login')

    if request.method == 'GET':
        login_form = LoginForm()
        # print login_form
        return render(request, 'account/login.html', {"form": login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserprofileForm(request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            # ModelForm 对象拥有save的方法，其作用就是将数据存入数据库，而commit=false则只生城一个数据对象并不保存
            new_user = user_form.save(commit=False)
            print user_form.cleaned_data
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('Successfully')
        else:
            return HttpResponse("Sorry, your can't register.")
    else:
        user_form = RegistrationForm()
        profile_form = UserprofileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': profile_form})












