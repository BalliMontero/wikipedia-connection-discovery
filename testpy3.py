import functionspy3
import operator

import networkx as nx

'''
async exploration and job execution
search for keywords and link (other crawler)
'''

#key1, key2 = "Health", "Fashion"

def wikilinker(key1, key2):
    base_url = 'https://en.wikipedia.org/wiki/'+key1
    end_url = 'https://en.wikipedia.org/wiki/'+key2

    G = functionspy3.find_connection(base_url,end_url)

    G.number_of_nodes()

    nx.average_clustering(G)

    page_rank_dict = nx.pagerank(G)
    ordered_page_rank = sorted(page_rank_dict.items(),key = operator.itemgetter(1),reverse = True)
    ordered_page_rank[1:10]
