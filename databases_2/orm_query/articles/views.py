from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'

    def get_queryset(self):

        return Article.objects.only('title', 'text', 'image', 'author', 'genre').select_related()

