from rest_framework import serializers
from .models import CoinbaseKeys, Orders

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinbaseKeys
        fields = ('id', 'key', 'secret', 'passphrase')

class CoinbaseKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinbaseKeys
        fields = ('key', 'secret', 'passphrase')

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('currency_name', 'schedule', 'funds')