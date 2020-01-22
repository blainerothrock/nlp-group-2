import pickle, os, logging
from typing import *

logging.basicConfig(filename='example.log', level=logging.DEBUG)

class Global:
    sparql_query: str = """
    PREFIX schema: <http://schema.org/>
    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    
    SELECT ?ship ?shipLabel ?article WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      ?ship wdt:P31 wd:Q11446.
      
      OPTIONAL {
        ?ship rdfs:label ?country filter (lang(?country) = "en") .
      }
          
      OPTIONAL {
        ?article schema:about ?ship .
        ?article schema:inLanguage "en" .
        ?article schema:isPartOf <https://en.wikipedia.org/> .
      }
    }
    LIMIT 10
    """
    sparql_page_label: str = 'article'
    sparql_name_label: str = 'shipLabel'

    # pickles
    pages_url: str = 'data/page_links.p'
    names_url: str = 'data/page_titles.p'

    # text files
    raw_text_url = 'data/group2.raw.txt'


class DataManagment:

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
    def get_names() -> Optional[Set[str]]:
        try:
            f = open(Global.names_url, "rb")
            return pickle.load(f)
        finally:
            return None

    @staticmethod
    def save_names(titles: Set[str]):
        pickle.dump(titles, open(Global.names_url, 'wb'))

    @staticmethod
    def write_raw_text(texts: List[str]):
        with open(Global.raw_text_url, 'w') as f:
            f.writelines("%s\n" % text for text in texts)