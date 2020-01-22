from constants import Global, DataManagement
from wiki_parser import WikiParser
from SPARQLWrapper import SPARQLWrapper, JSON
from time import sleep
import sys


def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def fetch_articles():
    endpoint_url = "https://query.wikidata.org/sparql"
    query = Global.sparql_query

    results = get_results(endpoint_url, query)
    bindings = list(filter(
        lambda x: Global.sparql_page_label in x and Global.sparql_page_label in x, results['results']['bindings']
    ))
    pages = set([ele[Global.sparql_page_label]['value'] for ele in bindings])
    names = set([ele[Global.sparql_name_label]['value'] for ele in bindings])
    DataManagement.save_pages(pages)
    DataManagement.save_names(names)
    print(list(names))
    return pages


def fetch_text_from_urls(urls, parser):

    print('fetching %i wikipedia pages' % len(urls))
    with open(Global.raw_text_url, 'w') as f:
        count: float = 0.0
        for url in urls:
            print("fetching text for %s | progress: %f%%" % (url, count/len(urls)*100))
            raw_text = parser.fetch_page(url)
            f.write('%s\n' % raw_text)
            count += 1
            sleep(0.25)
        f.close()
