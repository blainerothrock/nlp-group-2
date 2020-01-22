from fetch_raw_data import fetch
from constants import DataManagement, Global
from prepare_corpus import Corpus
from create_vocab import create_vocab
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

    if not os.path.exists(Global.vocab_pickle_url):
        create_vocab()

if __name__ == '__main__':
    main()
