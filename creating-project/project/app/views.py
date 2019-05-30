from django.shortcuts import render

# Create your views here.

from .models import Station, Route


def stations_view(request):
    routes = Route.objects.all()

    context = {
        'routes': routes,
        # 'center': {'x': '37.6551636', 'y': '55.72566817'},
        # 'stations': ''
    }

    route = request.GET.get('route')

    if route:
        stations = Station.objects.filter(routes__name=route)

        context['stations'] = stations

        stations_x_order = stations.order_by('latitude')
        stations_y_order = stations.order_by('longitude')

        stations_x_first = stations_x_order.first()
        stations_x_last = stations_x_order.last()

        stations_y_first = stations_y_order.first()
        stations_y_last = stations_y_order.last()

        x = (stations_x_first.longitude + stations_x_last.longitude) / 2
        y = (stations_y_first.latitude + stations_y_last.latitude) / 2

        context['center'] = {'x': x, 'y': y}

    return render(request, 'stations.html', context)
