from constants import Global, DataManagment
from wiki_parser import WikiParser
from SPARQLWrapper import SPARQLWrapper, JSON
from time import sleep
import logging


endpoint_url = "https://query.wikidata.org/sparql"

query = Global.sparql_query

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def fetch():
    # fetch page labels
    parser = WikiParser()
    titles = DataManagment.get_titles()

    if titles is None:
        results = get_results(endpoint_url, query)
        titles = [ele[Global.sparql_page_label]['value'] for ele in results['results']['bindings']]
        DataManagment.save_titles(titles)

    texts = []

    for title in titles[0:1]:
        print('fetching text for %s' % title)
        parser = WikiParser()
        data = parser.fetch_page(title)
        text = data['parse']['text']['*']
        texts.append(text)
        sleep(1)

    DataManagment.write_raw_text(texts)
