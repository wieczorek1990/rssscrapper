from rest_framework.generics import ListAPIView

from api.models import ExchangeRate
from api.serializers import ExchangeRateSerializer


class ExchangeRateView(ListAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
