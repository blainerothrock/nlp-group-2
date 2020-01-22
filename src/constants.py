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
    train_pickle_url = 'data/group2.train.p'
    valid_pickle_url = 'data/group2.valid.p'
    test_pickle_url = 'data/group2.test.p'
    vocab_pickle_url = 'data/group2.vocab.p'
    vocab_dict_pickle_url = 'data/group2.vocab_dict.p'

    # text files
    raw_text_url = 'data/group2.raw.txt'
    train_txt_url = 'data/group2.train.txt'
    valid_txt_url = 'data/group2.valid.txt'
    test_txt_url = 'data/group2.test.txt'

    # train/valid/test sizes
    train_percent = .9

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

    @staticmethod
    def write_train_valid_test(train: List[str], valid: List[str], test: List[str]):
        # dump to lists pickle and write as string to txt file
        pickle.dump(train, open(Global.train_pickle_url, 'wb'))
        with open(Global.train_txt_url, 'w') as f:
            f.writelines("%s " % tok for tok in train)

        pickle.dump(valid, open(Global.valid_pickle_url, 'wb'))
        with open(Global.valid_txt_url, 'w') as f:
            f.writelines("%s " % tok for tok in valid)

        pickle.dump(test, open(Global.test_pickle_url, 'wb'))
        with open(Global.test_txt_url, 'w') as f:
            f.writelines("%s " % tok for tok in test)

    @staticmethod
    def save_vocab_data(vocab: List[str], vocab_dict: Dict[str, int]):
        pickle.dump(vocab, open(Global.vocab_pickle_url, 'wb'))
        pickle.dump(vocab_dict, open(Global.vocab_dict_pickle_url, 'wb'))