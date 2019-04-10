import os
import json
from django.conf import settings
from articles.models import Article

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
                articles = json.load(json_file)
                for article in articles:
                    art = Article(
                        article['pk'],
                        article['fields']['title'],
                        article['fields']['text'],
                        article['fields']['published_at'],
                        article['fields']['image'],
                    )
                    art.save()
