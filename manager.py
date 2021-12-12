import config
from shopify import Shop

class Manager:
    def __init__(self):
        __shop_name = "pyjama-femme-com"
        self.shop = Shop(config.API_KEYS_FILE, __shop_name, )

if __name__ == "__main__":
    manager = Manager()
    info = manager.shop.get_order_info('3735160094849') 


