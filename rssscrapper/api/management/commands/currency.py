from django.core.management.base import BaseCommand

from api.rss_reader import RSSReader


class Command(BaseCommand):
    help = 'Fetches currency'

    def add_arguments(self, parser):
        parser.add_argument('currencies', nargs='+', type=str)

    def handle(self, *args, **options):
        for currency in options['currencies']:
            result = RSSReader(currency).process()
            if result:
                message = 'Success processing currency {}'.format(currency)
            else:
                message = 'Failure processing currency {}'.format(currency)
            self.stdout.write(message)
