"""
Reads Credentials from JSON file.
"""
import json

class Credentials:
    def __init__(self, filename:str):
        self.filename = filename
        self.__creds = self.__read()

    def __read(self):
        fp = open(self.filename)
        return json.load(fp)

    def get_shopify_key(self):
        return self.__creds['shopify_api_key']

    def get_shopify_password(self):
        return self.__creds['shopify_password']

