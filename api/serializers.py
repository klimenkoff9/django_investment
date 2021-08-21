from rest_framework import serializers
from .models import Store, Order

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'key', 'secret', 'passphrase')

class CreateStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('key', 'secret', 'passphrase')

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('product_id', 'side', 'funds')