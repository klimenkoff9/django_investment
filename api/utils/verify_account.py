from copy import Error
from cbpro import AuthenticatedClient
from requests import auth

def verify_account(api_key, api_secret, api_passphrase):
    try:
        if len(api_secret) % 4 != 0:
            raise ValueError("api_secret must be a multiple of 4 ")
        auth_client = AuthenticatedClient(api_key, api_secret, api_passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")
        if not type(auth_client.get_accounts()).__name__ == 'list':
            return False
        return auth_client
    except ValueError as e:
        print(e)
        return False
