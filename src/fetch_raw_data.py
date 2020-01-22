from constants import Global, DataManagement
from wiki_parser import WikiParser
from SPARQLWrapper import SPARQLWrapper, JSON
from time import sleep


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


def fetch_raw_text(pages, topic):
    # fetch page labels
    parser = WikiParser()
    texts = []

    print('fetching %i wikipedia pages' % len(pages))
    with open("data/" + topic + "_raw.txt", 'w') as f:
        count: float = 0.0
        for url in pages:
            print('  fetching text for %s -- %d' % (url, count/len(pages)))
            parser = WikiParser()
            raw_text = parser.fetch_page(url)
            f.write('%s\n' % raw_text)
            count += 1
            sleep(0.25)
        f.close()
