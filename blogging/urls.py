"""Blogging App Urls Patterns"""
from django.urls import path
from .views import (
    Index,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView
)

urlpatterns = [
    # homd page
    path('', Index.as_view(), name='index'),
    # article
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='article_detail'),
    # new article
    path('posts/new/', BlogCreateView.as_view(), name='new_post'),
    # edit article
    path('posts/<int:pk>/edit/',
         BlogUpdateView.as_view(), name='edit_post')
]
