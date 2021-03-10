from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from .models import Article
from django.urls import reverse_lazy

context_name = 'articles'


class Index(ListView):
    model = Article
    context_object_name = context_name
    template_name = 'blogging/index.html'


class BlogDetailView(DetailView):
    model = Article
    context_object_name = context_name
    template_name = 'blogging/article_detail.html'


class BlogCreateView(CreateView):
    model = Article
    context_object_name = context_name
    template_name = 'blogging/new_post.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Article
    context_object_name = context_name
    template_name = 'blogging/edit_post.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Article
    context_object_name = context_name
    template_name = 'blogging/delete_post.html'
    success_url = reverse_lazy('index')
