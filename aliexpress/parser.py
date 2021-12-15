from bs4 import BeautifulSoup

class AEOrderParser:
    """Ali Express Order Parser
    Parses the HTML content on AliExpress order details page."""

    def __init__(self, source:str):
        self.soup = self.__prepare_soup(source) 

    def __prepare_soup(self, source):
        return BeautifulSoup(source, "lxml")

    def update_source(self, new_source:str):
        return BeautifulSoup(new_source, "lxml")

    def fetch_order_no(self) -> str:
        elem = self.soup.find("dd", {"class":"order-no"})
        order_no = elem.text.strip()
        return order_no

    def fetch_order_status(self) -> str:
        elem = self.soup.find("dd", {"class":"order-status"})
        status = elem.text.strip()
        return status
