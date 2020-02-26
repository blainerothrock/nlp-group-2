import requests, re, pickle
from bs4 import BeautifulSoup
from typing import *


class WikiParser():

    def __init__(self):
        self.S = requests.Session()
        self.baseURL = 'https://en.wikipedia.org/'
        self.URL = "https://en.wikipedia.org/w/api.php"

    def parse_list_page(self, url, list_tag, topic,) -> List[str]:
        index = requests.get(url).text
        soup = BeautifulSoup(index, 'html.parser')
        elements = soup.findAll(list_tag)
        links: List[str] = list(filter(lambda l: l and 'href' in l.attrs, [e.find('a') for e in elements]))

        links = set([self.baseURL + link['href'] for link in links])
        titles: List[str] = [l.split('/')[-1] for l in list(links)]
        pickle.dump(titles, open("data/" + topic + "_titles", 'wb'))

        return links

    def fetch_page(self, url: str) -> str:
        index = requests.get(url).text
        soup = BeautifulSoup(index, 'html.parser')
        text = "\n".join([x.get_text() for x in soup.findAll('p')])

        return text
