from unittest import mock

from django.test import TransactionTestCase

from api import models
from api import rss_reader


class RSSReaderTestCase(TransactionTestCase):
    @mock.patch('api.rss_reader.RSSReader.download')
    def test_reader(self, download_mock):
        download_mock.return_value = open('../prototype/sample-rss.xml', 'r')\
                                     .read()

        count = models.ExchangeRate.objects.count()
        self.assertEqual(count, 0)

        result = rss_reader.RSSReader('eur').process()
        self.assertTrue(result)

        count = models.ExchangeRate.objects.count()
        self.assertEqual(count, 1)

    @mock.patch('api.rss_reader.RSSReader.download')
    def test_reader_error(self, download_mock):
        download_mock.return_value = 'error'

        result = rss_reader.RSSReader('eur').process()
        self.assertFalse(result)
