from fetch_raw_data import fetch
from constants import DataManagement, Global
from prepare_corpus import Corpus
import os

def main():
    # get raw data, don't repeat if already done
    if not os.path.exists(Global.raw_text_url):
        DataManagement.purge()
        fetch()

    # create corpus, don't repeat if already done
    if not os.path.exists(Global.train_txt_url):
        c = Corpus()
        c.load_and_clean()
        c.train_valid_test_split()

def fetch_data():
    parser = WikiParser()
    # articles = parser.parse_list_page("https://en.wikipedia.org/wiki/List_of_dinosaur_genera")
    # articles = fetch_articles()
    topic = 'battles-1901-2000'
    articles = parser.parse_list_page("https://en.wikipedia.org/wiki/List_of_battles_1901%E2%80%932000", "li", topic)
    fetch_raw_text(articles, topic)

if __name__ == '__main__':
    main()
