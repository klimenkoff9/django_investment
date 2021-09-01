from copy import Error
import cbpro
from cbpro import authenticated_client

def verify_account(api_key, api_secret, api_passphrase):
    try:
        if len(api_secret) % 4 != 0:
            raise ValueError("api_secret must be a multiple of 4 ")
        auth_client = cbpro.AuthenticatedClient(api_key, api_secret, api_passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")
        if not type(auth_client.get_accounts()).__name__ == 'list':
            return False
        return True
    except ValueError as e:
        print(e)
        return False
