from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Article


class Index(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blogging/index.html'


class BlogDetailView(DetailView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blogging/article_detail.html'


class BlogCreateView(CreateView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blogging/new_post.html'
    fields = ['title', 'author', 'body']
