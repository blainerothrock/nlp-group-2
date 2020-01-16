from fetch_raw_data import fetch
from constants import DataManagment

def main():
    print('hello NLP')
    DataManagment.purge()
    fetch()

if __name__ == '__main__':
    main()
