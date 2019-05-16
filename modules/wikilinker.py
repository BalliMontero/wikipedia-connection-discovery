from modules import functions
import operator

import networkx as nx
import wikipedia

def wikiSearch(key1, key2):
    # obtain suggestions if input exists
    if key1 and key2:
        suggestK1 = wikipedia.suggest(key1)
        suggestK2 = wikipedia.suggest(key2)
        # perform search if suggestion returns None
        if suggestK1 == None:
            suggestK1 = wikipedia.search(key1, results=1)
        if suggestK2 == None:
            suggestK2 = wikipedia.search(key2, results=1)
    else:
        return 0
    # identify links
    wikilinker(suggestK1[0], suggestK2[0])


def wikilinker(key1, key2):
    base_url = 'https://en.wikipedia.org/wiki/'+key1
    end_url = 'https://en.wikipedia.org/wiki/'+key2

    G = functions.find_connection(base_url,end_url)

    G.number_of_nodes()

    nx.average_clustering(G)

    page_rank_dict = nx.pagerank(G)
    ordered_page_rank = sorted(page_rank_dict.items(),key = operator.itemgetter(1),reverse = True)
    ordered_page_rank[1:10]
