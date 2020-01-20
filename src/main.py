from fetch_raw_data import fetch
from constants import DataManagement
from prepare_corpus import Corpus

def main():
    # get raw data
    DataManagment.purge()
    fetch()

    # create corpus
    c = Corpus()
    c.load_and_clean()
    c.train_valid_test_split()

if __name__ == '__main__':
    main()
