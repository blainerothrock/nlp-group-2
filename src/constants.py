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

    topics: str = ['battles-1901-2000', 'war']
    list_urls: str = ['https://en.wikipedia.org/wiki/List_of_battles_(alphabetical)', 'https://en.wikipedia.org/wiki/Outline_of_war#Wars']
    html_tags: str = ['li', 'li']
    # topics: str = ['Egyptian_American_writers']
    # list_urls: str = ['https://en.wikipedia.org/wiki/List_of_Egyptian-American_writers']
    # html_tags: str = ['li']

    vocab_freq_threshold = 3

    # pickles
    pages_url: str = 'data/page_links.p'
    train_pickle_url = 'data/group2.train.p'
    valid_pickle_url = 'data/group2.valid.p'
    test_pickle_url = 'data/group2.test.p'

    tagged_train_pickle_url = 'data/group2.tagged_train.p'
    tagged_valid_pickle_url = 'data/group2.tagged_valid.p'
    tagged_test_pickle_url = 'data/group2.tagged_test.p'

    vocab_pickle_url = 'data/group2.vocab.p'
    vocab_dict_pickle_url = 'data/group2.vocab_dict.p'

    tagged_vocab_pickle_url = 'data/group2.tagged_vocab.p'
    tagged_vocab_dict_pickle_url = 'data/group2.tagged_vocab_dict.p'

    names_url: str = 'data/page_titles.p'

    assignment1_stats_url = "data/assignment1_stats.p"

    # text files
    raw_text_url = 'data/group2.raw.txt'
    train_txt_url = 'data/group2.train.txt'
    valid_txt_url = 'data/group2.valid.txt'
    test_txt_url = 'data/group2.test.txt'

    tagged_train_txt_url = 'data/group2.tagged_train.txt'
    tagged_valid_txt_url = 'data/group2.tagged_valid.txt'
    tagged_test_txt_url = 'data/group2.tagged_test.txt'

    # train/valid/test sizes
    train_percent = .9


class DataManagement:

    @staticmethod
    def purge():
        try:
            os.remove(Global.pages_url)
            os.remove(Global.train_pickle_url)
            os.remove(Global.valid_pickle_url)
            os.remove(Global.test_pickle_url)
            os.remove(Global.vocab_pickle_url)
            os.remove(Global.vocab_dict_pickle_url)
            os.remove(Global.raw_text_url)
            os.remove(Global.train_txt_url)
            os.remove(Global.valid_txt_url)
            os.remove(Global.test_txt_url)
            os.remove(Global.tagged_train_txt_url)
            os.remove(Global.tagged_valid_txt_url)
            os.remove(Global.tagged_test_txt_url)
            os.remove(Global.tagged_train_pickle_url)
            os.remove(Global.tagged_valid_pickle_url)
            os.remove(Global.tagged_test_pickle_url)
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
    def write_tagged_train_valid_test(train: List[str], valid: List[str], test: List[str]):
        # dump to lists pickle and write as string to txt file
        pickle.dump(train, open(Global.tagged_train_pickle_url, 'wb'))
        with open(Global.tagged_train_txt_url, 'w') as f:
            f.writelines("%s " % tok for tok in train)

        pickle.dump(valid, open(Global.tagged_valid_pickle_url, 'wb'))
        with open(Global.tagged_valid_txt_url, 'w') as f:
            f.writelines("%s " % tok for tok in valid)

        pickle.dump(test, open(Global.tagged_test_pickle_url, 'wb'))
        with open(Global.tagged_test_txt_url, 'w') as f:
            f.writelines("%s " % tok for tok in test)

    @staticmethod
    def save_vocab_data(vocab: List[str], vocab_dict: Dict[str, int]):
        pickle.dump(vocab, open(Global.vocab_pickle_url, 'wb'))
        pickle.dump(vocab_dict, open(Global.vocab_dict_pickle_url, 'wb'))

    @staticmethod
    def save_tagged_vocab_data(vocab: List[str], vocab_dict: Dict[str, int]):
        pickle.dump(vocab, open(Global.tagged_vocab_pickle_url, 'wb'))
        pickle.dump(vocab_dict, open(Global.tagged_vocab_dict_pickle_url, 'wb'))