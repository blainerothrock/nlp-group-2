from fetch_raw_data import fetch_raw_text, fetch_articles
from wiki_parser import WikiParser

def main():
    print('hello NLP')


def fetch_data():
    parser = WikiParser()
    # articles = parser.parse_list_page("https://en.wikipedia.org/wiki/List_of_dinosaur_genera")
    # articles = fetch_articles()
    topic = 'battles-1901-2000'
    articles = parser.parse_list_page("https://en.wikipedia.org/wiki/List_of_battles_1901%E2%80%932000", "li", topic)
    fetch_raw_text(articles, topic)

if __name__ == '__main__':
    main()
