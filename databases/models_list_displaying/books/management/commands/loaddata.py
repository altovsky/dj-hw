import os
import json
from django.conf import settings
from books.models import Book

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'json_path',
            nargs=1,
            type=str,
        )

    def handle(self, *args, **options):

        if options['json_path']:
            with open(os.path.join(settings.BASE_DIR, options['json_path'][0]), 'r') as json_file:
                books = json.load(json_file)
                for book in books:
                    bk = Book(
                        book['pk'],
                        book['fields']['name'],
                        book['fields']['author'],
                        book['fields']['pub_date'],
                    )
                    bk.save()
