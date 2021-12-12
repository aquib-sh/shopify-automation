import requests
import pandas
from creds import Credentials

class Shop:
    """Performs various tasks via Shopify API.

    Parameters
    -----------
    api_keys_file: str
        JSON file containing API keys.

    name: str
        Name of the shop

    api_version: str (Default="2021-01")
        API version of shopify
    """
    def __init__(self, api_keys_file:str, name:str, api_version="2021-01"):
        creds = Credentials(api_keys_file)
        self.__SHOP_KEY = creds.get_shopify_key()
        self.__SHOP_PASSWORD = creds.get_shopify_password()
        self.SHOP_NAME = name
        self.SHOP_URL = f"https://{self.__SHOP_KEY}:{self.__SHOP_PASSWORD}@{self.SHOP_NAME}.myshopify.com/admin"
        self.API_VERSION = "2021-01"
    
    def __get_unfullfilled_orders_raw(self) -> pandas.DataFrame:
        """Fetches all the unfullfilled orders.
        
        Return
        ------
        orders :pandas.DataFrame
            A pandas dataframe containing all the order details.
        """
        resource = 'orders'
        last = 0
        orders = pandas.DataFrame()
        while True:
            url = (self.SHOP_URL 
                    + f"/api/{self.API_VERSION}/{resource}.json" 
                    + "?limit=250&fulfillment_status=unfulfilled&since_id={last}")
            response = requests.request("GET", url)
            df = pandas.DataFrame(response.json()['orders'])
            orders = pandas.concat([orders,df])
            last = df['id'].iloc[-1]
            if len(df) < 250:
                break
        return(orders)

    def __get_all_orders_raw(self) -> pandas.DataFrame:
        """Fetches all the orders.
        
        Return
        ------
        orders :pandas.DataFrame
            A pandas dataframe containing all the order details.
        """
        resource = 'orders'
        last = 0
        orders = pandas.DataFrame()
        while True:
            url = (self.SHOP_URL 
                    + f"/api/{self.API_VERSION}/{resource}.json"
                    + "?limit=250&since_id={last}")
            response = requests.request("GET", url)
            df = pandas.DataFrame(response.json()['orders'])
            orders = pandas.concat([orders,df])
            last = df['id'].iloc[-1]
            if len(df) < 250:
                break
        return(orders)

    def get_order_info(self, order_id:str):
        resource = 'orders'
        url = (self.SHOP_URL 
                + f"/api/{self.API_VERSION}/{resource}/{order_id}.json")
        response = requests.request("GET", url)
        return response

    def get_all_orders(self) -> pandas.DataFrame:
        """Fetches all the orders and returns a limited info.

        Returns
        -------
        refined_orders :pandas.DataFrame
            A pandas dataframe containing order details
            columns=(id, name, product_title, product_id, aliexpress_link).
        """
        orders = self.__get_all_orders_raw()
        orders_dict = {
                'id':[], 
                'name':[], 
                'product_title':[], 
                'product_id':[], 
                'aliexpress_link':[]
                } 
        dlength = len(orders['id'])

        for i in range(0, dlength):
            row = orders.loc[i]
            shipping_info = row['shipping_address'] # shipping details of customers
            items = row['line_items'] # list containing details all the items ordered
            number_of_items = len(items)

            _id = row['id']
            name = shipping_info['first_name'] +" "+ shipping_info['last_name']

    
