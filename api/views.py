from rest_framework import generics, serializers, status
from .serializers import StoreSerializer, CreateStoreSerializer, PlaceOrderSerializer
from .models import Store
from rest_framework.response import Response
from rest_framework.views import APIView
import cbpro

# account/view
class StoreView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# account/add-key
class CreateStoreView(APIView):
    serializer_class = CreateStoreSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            key = serializer.data.get('key')
            secret = serializer.data.get('secret')
            passphrase = serializer.data.get('passphrase')
            store_exists = Store.objects.filter(key=key)
            if len(store_exists) == 0:
                store = Store(key=key, secret=secret, passphrase=passphrase)
                store.save()
                return Response(StoreSerializer(store).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# account/place-order?pk=:pk&currency=:currency&funds=:funds
class PlaceOrder(APIView):
    serializer_class = PlaceOrderSerializer
    account_id = 'pk'
    currency_name = 'currency'
    funds = 'funds'

    def get(self, request, format=None):
        pk = request.GET.get(self.account_id)
        currency = request.GET.get(self.currency_name)
        funds = request.GET.get(self.funds)
        if pk != None and currency != None and funds != None:
            api = Store.objects.filter(id=pk)
            if len(api) > 0:
                data = StoreSerializer(api[0]).data
                auth_client = cbpro.AuthenticatedClient(data["key"], data['secret'], data['passphrase'], api_url="https://api-public.sandbox.pro.coinbase.com")
                
                buy(auth_client, currency, funds);

                return Response(data, status=status.HTTP_200_OK)
            return Response({'Key Not Found': 'Invalid Primary Key.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Key paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)

def buy(account, currency, funds):
    account.place_market_order(product_id=currency, side='buy',funds=funds)