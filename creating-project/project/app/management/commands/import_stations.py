from django.core.management.base import BaseCommand
from app.models import Station, Route
import csv

CSV_FILE = 'moscow_bus_stations.csv'
ENCODING = 'cp1251'


class Command(BaseCommand):
    help = 'Загружает данные об остановках и маршрутах.'

    def handle(self, *args, **options):
        with open(CSV_FILE, 'r', encoding=ENCODING) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')

            for line in reader:
                station_value = Station(
                    latitude=line['Latitude_WGS84'],
                    longitude=line['Longitude_WGS84'],
                    name=line['Name'],
                )
                station_value.save()

                route_values = [i.strip() for i in line['RouteNumbers'].split(';')]

                for value in route_values:
                    route = Route.objects.get_or_create(name=value)
                    station_value.routes.add(route[0])
                    station_value.save()
