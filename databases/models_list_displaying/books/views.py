from django.views import generic
from django.core.paginator import Paginator
# from django.shortcuts import get_object_or_404
# from django.conf import settings
from books.models import Book
from django.http import request


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['p'] = False

        return context


class BookView(generic.ListView):
    # model = Book
    # context_object_name = 'bk_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = self.get_queryset()
        context['site_url'] = "http://127.0.0.1:8000/books/"
        # context['site_url'] = f"{request.HttpRequest.scheme}://{request.HttpRequest.META['HTTP_HOST']}/books/"

        bk = context['book_list'][0]
        bk_list = Book.objects.all()

        p = Paginator(bk_list, 1)
        current_page_num = bk.pk
        current_page = p.page(current_page_num)

        if current_page.has_previous():
            prev_page_date = {bk_list[current_page.previous_page_number()].pub_date}
        else:
            prev_page_date = None

        if current_page.has_next():
            next_page_date = {bk_list[current_page.next_page_number()].pub_date}
        else:
            next_page_date = None

        context['prev_page_date'] = prev_page_date
        context['next_page_date'] = next_page_date
        context['p'] = True

        return context

    def get_queryset(self):

        return Book.objects.filter(pub_date=self.kwargs['pub_date'])
