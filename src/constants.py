import pickle, os, logging
from typing import *

logging.basicConfig(filename='example.log', level=logging.DEBUG)

class Global:
    sparql_query: str = """
    PREFIX schema: <http://schema.org/>
    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    
    SELECT ?serial_killer ?serial_killerLabel ?article WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      ?serial_killer wdt:P106 wd:Q484188.
      
      OPTIONAL {
          ?serial_killer rdfs:label ?country filter (lang(?country) = "en") .
        }
      
      OPTIONAL {
          ?article schema:about ?serial_killer .
          ?article schema:inLanguage "en" .
          ?article schema:isPartOf <https://en.wikipedia.org/> .
        }
      
    }
    LIMIT 1000
    """
    sparql_page_label: str = "article"

    # pickles
    pages_url: str = 'data/page_links.p'

    # text files
    raw_text_url = 'data/group2.raw.txt'


class DataManagement:

    @staticmethod
    def purge():
        try:
            os.remove(Global.pages_url)
        except:
            logging.info('exception removing file')

    @staticmethod
    def get_pages() -> Optional[Set[str]]:
        try:
            f = open(Global.pages_url, "rb")
            return pickle.load(f)
        finally:
            return None

    @staticmethod
    def save_pages(titles: Set[str]):
        pickle.dump(titles, open(Global.pages_url, 'wb'))

    @staticmethod
    def write_raw_text(texts: List[str]):
        with open(Global.raw_text_url, 'w') as f:
            f.writelines("%s\n" % text for text in texts)