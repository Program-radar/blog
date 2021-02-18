"""Blogging App Urls Patterns"""
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]