import requests
from bs4 import BeautifulSoup
import typing


class WikiParser():

    def __init__(self):
        self.S = requests.Session()
        self.URL = "https://en.wikipedia.org/w/api.php"

    def fetch_page(self, url: str) -> str:
        index = requests.get(url).text
        soup = BeautifulSoup(index, 'html.parser')
        text = "\n".join([x.get_text() for x in soup.findAll('p')])

        return text
