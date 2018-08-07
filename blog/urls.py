# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 16:35
# @Author  : sssssjd
# @Email   : sssssjd@163.com
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
]
