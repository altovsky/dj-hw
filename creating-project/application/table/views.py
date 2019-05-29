import csv
from django.shortcuts import render
from django.views import View

from .models import TableSettings, CSVPath
# Create your views here.

csv_filename = 'phones.csv'
csv_path = CSVPath().get_path()

if csv_path == '' or csv_path != csv_filename:
    CSVPath().set_path(csv_filename)
else:
    csv_filename = csv_path

columns = TableSettings.objects.values()

if len(columns) == 0:
    TableSettings.objects.create(name='id', width=1, index=1)
    TableSettings.objects.create(name='name', width=3, index=2)
    TableSettings.objects.create(name='price', width=2, index=3)
    TableSettings.objects.create(name='release_date', width=2, index=4)
    TableSettings.objects.create(name='lte_exists', width=1, index=5)
    columns = TableSettings.objects.values()


class TableView(View):

    def get(self, request):
        with open(csv_filename, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)

            result = render(request, 'table.html', {'columns': columns, 'table': table, 'csv_file': csv_filename})
        return result
