# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 16:35
# @Author  : sssssjd
# @Email   : sssssjd@163.com
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name = 'article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name = 'edit_page'),
    re_path(r'^edit/action$', views.edit_action, name = 'edit_action'),
]
app_name='blog'