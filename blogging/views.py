from django.views.generic import ListView
from .models import Article

class Index(ListView):
    model = Article
    context_object_name = 'posts'
    template_name = 'blogging\\index.html'
