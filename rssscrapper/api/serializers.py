from rest_framework.serializers import ModelSerializer

from api.models import ExchangeRate


class ExchangeRateSerializer(ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('base_currency', 'target_currency', 'value')
