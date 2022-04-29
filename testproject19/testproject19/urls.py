"""testproject19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
]
