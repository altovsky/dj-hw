from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from django.core.paginator import Paginator
import csv
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = request.GET.get('page')

    if page:
        current_page_num = int(page)
    else:
        current_page_num = 1

    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as bus_station_file:
        bus_station_reader = csv.DictReader(bus_station_file)

        p = Paginator(list(bus_station_reader), settings.PAGINATOR_PER_PAGE)
        total_pages_num = p.num_pages

        if current_page_num > total_pages_num:
            current_page_num = total_pages_num

        if current_page_num < 1:
            current_page_num = 1

        current_page = p.page(current_page_num)

        if current_page.has_previous():
            prev_page_url = f'?page={current_page_num - 1}'
        else:
            prev_page_url = None

        if current_page.has_next():
            next_page_url = f'?page={current_page_num + 1}'
        else:
            next_page_url = None

        return render_to_response('index.html', context={
            'bus_stations': p.page(current_page_num),
            'current_page': current_page_num,
            'prev_page_url': prev_page_url,
            'next_page_url': next_page_url,
        })
