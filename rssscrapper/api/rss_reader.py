import logging

import requests
from xml.etree import ElementTree

from api.models import ExchangeRate


class RSSReader:
    NAMESPACES = {
        'cb': 'http://www.cbwiki.net/wiki/index.php/Specification_1.1'
    }

    def __init__(self, currency):
        self.currency = currency

    def process(self):
        try:
            content = self.download()
            currencies = self.parse(content)
            self.update_or_create(currencies)
        except ElementTree.ParseError as e:
            logging.error(e)
            return False
        return True

    def download(self):
        url = 'https://www.ecb.europa.eu/rss/fxref-{}.html'\
                .format(self.currency.lower())
        return requests.get(url).content

    def parse(self, content):
        currencies = []
        root = ElementTree.fromstring(content)
        exchange_rate = root.find('.//cb:exchangeRate',
                                  self.NAMESPACES)
        base_currency = exchange_rate.find('./cb:baseCurrency',
                                           self.NAMESPACES)
        target_currency = exchange_rate.find('./cb:targetCurrency',
                                             self.NAMESPACES)
        value = exchange_rate.find('./cb:value',
                                   self.NAMESPACES)
        currencies.append((base_currency, target_currency, value))
        return currencies

    def update_or_create(self, currencies):
        for base_currency, target_currency, value in currencies:
            ExchangeRate.objects.update_or_create(
                base_currency=base_currency.text,
                target_currency=target_currency.text,
                defaults={'value': value.text}
            )
