import requests


class RSSReader:
    def __init__(self, currency):
        self.currency = currency

    def process(self):
        try:
            content = self.download()
            fields = self.parse(content)
            self.create_or_update(fields)
        except:
            return False
        return True

    def download(self):
        url = 'https://www.ecb.europa.eu/rss/fxref-{}.html'.format(self.currency.lower())
        return requests.get(url).content

    def parse(self, content):
        return []

    def create_or_update(self, fields):
        pass


if __name__ == '__main__':
    reader = RSSReader('usd')
    result = reader.download()
    print(result)
