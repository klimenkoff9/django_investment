from rest_framework import generics, serializers, status
from .serializers import CoinbaseKeysSerializer, OrdersSerializers
from .models import CoinbaseKeys, Orders
from rest_framework.response import Response
from rest_framework.views import APIView

# account/view


class KeysView(generics.ListAPIView):
    queryset = CoinbaseKeys.objects.all()
    serializer_class = CoinbaseKeysSerializer

# account/add-key

# add check if account exists


class AddKeyView(APIView):
    serializer_class = CoinbaseKeysSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            key = serializer.data.get('key')
            secret = serializer.data.get('secret')
            passphrase = serializer.data.get('passphrase')
            nickname = serializer.data.get('nickname')
            key_exists = CoinbaseKeys.objects.filter(key=key)
            if len(key_exists) == 0:
                key = CoinbaseKeys(key=key, secret=secret,
                                   passphrase=passphrase, nickname=nickname)
                key.save()
                return Response(CoinbaseKeysSerializer(key).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# account/place-order


class OrderView(APIView):
    serializer_class = OrdersSerializers

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            frequency = serializer.data.get('frequency')
            currency_name = serializer.data.get('currency_name')
            funds = serializer.data.get('funds')
            coinbase_account = serializer.data.get('coinbase_account')
            print(coinbase_account, funds, frequency, currency_name)

            if frequency != None and currency_name != None and funds != None and coinbase_account != None:
                order = Orders(frequency=frequency,
                               currency_name=currency_name, funds=funds, coinbase_account=CoinbaseKeys.objects.get(id=coinbase_account))
                order.save()
                return Response(OrdersSerializers(order).data, status=status.HTTP_201_CREATED)
            return Response({'Bad Request': 'Missing a param'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers

# def buy(account, currency, funds):
#     account.place_market_order(product_id=currency, side='buy',funds=funds)
