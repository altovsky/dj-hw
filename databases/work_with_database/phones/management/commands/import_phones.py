import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        bool_val = {
            'True': True,
            'False': False,
        }
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for phone in phone_reader:
                # TODO: Добавьте сохранение модели

                ph = Phone(
                    int(phone[0]),
                    phone[1],
                    phone[2],
                    int(phone[3]),
                    datetime.date(int(phone[4][:4]), int(phone[4][5:7]), int(phone[4][8:])),
                    bool_val[phone[5]],
                    )
                # ph.save()
                ph.slug = ph.get_slug()
                ph.save()
                # pass
