from constants import Global, DataManagment
from wiki_parser import WikiParser
from SPARQLWrapper import SPARQLWrapper, JSON
from time import sleep

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def fetch():
    # fetch page labels
    endpoint_url = "https://query.wikidata.org/sparql"
    query = Global.sparql_query
    parser = WikiParser()
    pages = DataManagment.get_pages()

    if pages is None:
        results = get_results(endpoint_url, query)
        bindings = filter(lambda x: Global.sparql_page_label in x, results['results']['bindings'])
        pages = set([ele[Global.sparql_page_label]['value'] for ele in bindings])
        DataManagment.save_pages(pages)

    texts = []

    print('fetching %i wikipedia pages' % len(pages))
    for url in pages:
        print('  fetching text for %s' % url)
        parser = WikiParser()
        raw_text = parser.fetch_page(url)
        texts.append(raw_text)
        sleep(0.25)

    DataManagment.write_raw_text(texts)
