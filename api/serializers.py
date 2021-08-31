from rest_framework import serializers
from .models import CoinbaseKeys, Orders
class CoinbaseKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinbaseKeys 
        fields = ('id', 'key', 'secret', 'passphrase', 'nickname')

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('currency_name', 'frequency', 'funds', "coinbase_account")