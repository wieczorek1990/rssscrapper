from django.db import models


# TODO(lwieczorek): figure out rateType
class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    value = models.DecimalField(max_digits=16, decimal_places=4)

    def __str__(self):
        return '{} -> {}: {}'.format(self.base_currency,
                                     self.target_currency,
                                     self.value)
