import pickle, os, logging
from typing import *

logging.basicConfig(filename='example.log', level=logging.DEBUG)

class Global:
    sparql_query: str = """
    SELECT ?serial_killer ?serial_killerLabel WHERE {
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
          
          OPTIONAL {  }
          
          
          ?serial_killer wdt:P106 wd:Q484188.
        }
        LIMIT 1000
    """
    sparql_page_label: str = "serial_killerLabel"

    # pickles
    titles_url: str = 'data/titles.p'

    # text files
    raw_text_url = 'data/group2.raw.txt'


class DataManagment:

    @staticmethod
    def purge():
        try:
            os.remove(Global.titles_url)
        except:
            logging.info('exception removing file')

    @staticmethod
    def get_titles() -> Optional[List[str]]:
        try:
            f = open(Global.titles_url, "rb")
            return pickle.load(f)
        finally:
            return None

    @staticmethod
    def save_titles(titles: List[str]):
        pickle.dump(titles, open(Global.titles_url, 'wb'))

    @staticmethod
    def write_raw_text(texts: List[str]):
        with open(Global.raw_text_url, 'w') as f:
            f.writelines("%s\n" % text for text in texts)