from django.views.generic import ListView, DetailView
from .models import Article

class Index(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blogging\\index.html'

class BlogDetailView(DetailView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blogging\\article_detail.html'
