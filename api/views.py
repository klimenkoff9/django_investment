from rest_framework import generics, serializers, status
from .serializers import StoreSerializer, CreateStoreSerializer, PlaceOrderSerializer
from .models import Store
from rest_framework.response import Response
from rest_framework.views import APIView
import cbpro

def buy(account):
    account.place_market_order(product_id='BTC-USD', side='buy',funds='102.00')

# account/login
class StoreView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# account/create
class CreateStoreView(APIView):
    serializer_class = CreateStoreSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            key = serializer.data.get('key')
            secret = serializer.data.get('secret')
            passphrase = serializer.data.get('passphrase')
            store = Store(key=key, secret=secret, passphrase=passphrase)
            store.save()
            print(store)
            return Response(StoreSerializer(store).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# account/get
class PlaceOrder(APIView):
    serializer_class = PlaceOrderSerializer
    lookup_url_kwarg = 'pk'

    def get(self, request, format=None):
        pk = request.GET.get(self.lookup_url_kwarg)
        if pk != None:
            api = Store.objects.filter(id=pk)
            if len(api) > 0:
                data = StoreSerializer(api[0]).data
                auth_client = cbpro.AuthenticatedClient(data["key"], data['secret'], data['passphrase'], api_url="https://api-public.sandbox.pro.coinbase.com")
                
                buy(auth_client);

                # auth_client.place_market_order(product_id='BTC-USD', side='buy',funds='101.00')
                # print(data["key"], data['secret'], data['passphrase'])

                return Response(data, status=status.HTTP_200_OK)
            return Response({'Key Not Found': 'Invalid Primary Key.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Key paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)
