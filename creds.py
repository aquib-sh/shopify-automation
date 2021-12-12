"""
Reads Credentials from JSON file.
"""
import json

class Credentials:
    def __init__(self, filename:str):
        self.__SHOPIFY_API_KEY      = 'shopify_api_key'
        self.__SHOPIFY_API_PASSWORD = 'shopify_api_password'
        self.__ALIEXPRESS_EMAIL     = 'aliexpress_email'
        self.__ALIEXPRESS_PASSWORD  = 'aliexpress_password'

        self.filename = filename
        self.__creds = self.__read()

    def __read(self):
        fp = open(self.filename)
        return json.load(fp)

    def __raise_error_if_not_exists(self, k) -> bool:
        """Raise Error if key does not exists in JSON file.
        
        Parameters
        ----------
        k : str
            key to check for existence in JSON file.
        """
        if not (k in self.__creds):
            raise Exception(f"{k} is not present in {self.filename}")

    def get_shopify_key(self):
        """Return Shopify API key."""
        self.__raise_error_if_not_exists(self.__SHOPIFY_API_KEY)
        return self.__creds[self.__SHOPIFY_API_KEY]

    def get_shopify_password(self):
        """Return Shopify API Password."""
        self.__raise_error_if_not_exists(self.__SHOPIFY_API_PASSWORD)
        return self.__creds[self.__SHOPIFY_API_PASSWORD]

    def get_aliexpress_email(self):
        """Return AliExpress account email."""
        self.__raise_error_if_not_exists(self.__ALIEXPRESS_EMAIL)
        return self.__creds[self.__ALIEXPRESS_EMAIL]

    def get_aliexpress_password(self):
        """Return AliExpress account password."""
        self.__raise_error_if_not_exists(self.__ALIEXPRESS_PASSWORD)
        return self.__creds[self.__ALIEXPRESS_PASSWORD]
