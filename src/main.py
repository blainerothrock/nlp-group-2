from fetch_raw_data import fetch_text_from_urls
from wiki_parser import WikiParser
from constants import DataManagement, Global
from prepare_corpus import Corpus
from create_vocab import create_vocab
import os

def main():
    # get raw data, don't repeat if already done
    if not os.path.exists(Global.raw_text_url):
        fetch_data()

    # create corpus, don't repeat if already done
    if not os.path.exists(Global.train_txt_url):
        c = Corpus()
        c.load_and_clean()
        c.train_valid_test_split()

    if not os.path.exists(Global.vocab_pickle_url):
        create_vocab()


def fetch_data():
    parser = WikiParser()

    urls = []
    for idx, list_url in enumerate(Global.list_urls):

        urls += parser.parse_list_page(
            list_url,
            Global.html_tags[idx],
            Global.topics[idx]
        )

    fetch_text_from_urls(urls, parser)

if __name__ == '__main__':
    main()
