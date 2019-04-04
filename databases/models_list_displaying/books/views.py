from django.views import generic
from django.core.paginator import Paginator
from books.models import Book


class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'bk_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()

        return context
