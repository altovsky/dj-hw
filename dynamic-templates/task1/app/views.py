from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings
import os
import csv


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        context = super().get_context_data(**kwargs)
        month_set = ('Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек')

        with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csv'), 'r') as inflation_file:
            file_reader = csv.DictReader(inflation_file, delimiter=';')
            file_fieldnames = file_reader.fieldnames
            value_stack = []

            for row in file_reader:
                field_values = []
                for name in file_fieldnames:
                    field_value = row[name]
                    bg_color = ''
                    field = {}

                    if name in month_set:

                        if field_value == '':
                            field_value = '-'
                        elif float(field_value) < 0:
                            bg_color = '#008000'
                        elif 1 <= float(field_value) < 2:
                            bg_color = '#fcd3d3'
                        elif 2 <= float(field_value) < 5:
                            bg_color = '#f98c8c'
                        elif float(field_value) >= 5:
                            bg_color = '#ff0000'

                    elif name == 'Суммарная':
                        bg_color = '#808080'

                    field['value'] = field_value
                    field['color'] = bg_color
                    field_values.append(field)

                value_stack.append(field_values)

        context['field_names'] = file_fieldnames
        context['field_values'] = value_stack

        return render(
            request,
            self.template_name,
            context
        )
