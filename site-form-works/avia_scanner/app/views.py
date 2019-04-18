# import time
# import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


CACHE_TIMEOUT = 60


class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    term = request.GET.get('term')

    cache_key = f'cities-{term}'
    cached = cache.get(cache_key)
    if cached is not None:
        return JsonResponse(cached, safe=False)

    if not term:
        results = []
    else:
        query = City.objects.filter(name__icontains=term)
        results = [c.name for c in query]
        cache.set(cache_key, results, CACHE_TIMEOUT)

    return JsonResponse(results, safe=False)
