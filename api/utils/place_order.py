from ..models import CoinbaseKeys
import cbpro

from .verify_account import verify_account
def place_order(funds, currency, api_id):
    credentials = CoinbaseKeys.objects.get(id=api_id)

    auth_client = verify_account(credentials.api_key, credentials.api_secret, credentials.api_passphrase)

    auth_client.place_market_order(product_id=currency, funds=funds, side='buy')