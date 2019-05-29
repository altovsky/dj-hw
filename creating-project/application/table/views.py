from django.shortcuts import render
from django.views import View
import csv

from .models import TableSettings, FilePath
# Create your views here.

CSV_FILENAME = 'phones.csv'
FilePath = FilePath().get_path()

if FilePath == '' or FilePath != CSV_FILENAME:
    FilePath().set_path(CSV_FILENAME)
else:
    CSV_FILENAME = FilePath

columns = TableSettings.objects.values()

if len(columns) == 0:
    TableSettings.objects.create(name='id', width=1, index_number=1)
    TableSettings.objects.create(name='name', width=3, index_number=2)
    TableSettings.objects.create(name='price', width=2, index_number=3)
    TableSettings.objects.create(name='release_date', width=2, index_number=4)
    TableSettings.objects.create(name='lte_exists', width=1, index_number=5)
    columns = TableSettings.objects.values()


class TableView(View):

    def get(self, request):
        with open(CSV_FILENAME, 'rt') as csv_file:
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

            result = render(request, 'table.html', {'columns': columns, 'table': table, 'csv_file': CSV_FILENAME})
        return result
