"""Blogging App Urls Patterns"""
from django.urls import path
from .views import Index, BlogDetailView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('posts/<int:pk>', BlogDetailView.as_view(), name='article_detail'),
]
