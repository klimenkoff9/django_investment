from rest_framework import serializers
from .models import CoinbaseKeys, Orders
class CoinbaseKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinbaseKeys 
        fields = ('id', 'api_key', 'api_secret', 'api_passphrase', 'nickname')

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('currency_name', 'frequency', 'funds', "coinbase_account")