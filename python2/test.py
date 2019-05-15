import functions
import operator

import networkx as nx

base_url = 'https://en.wikipedia.org/wiki/Health'
end_url = 'https://en.wikipedia.org/wiki/Disease'

G = functions.find_connection(base_url,end_url)

G.number_of_nodes()

nx.average_clustering(G)

page_rank_dict = nx.pagerank(G)
ordered_page_rank = sorted(page_rank_dict.items(),key = operator.itemgetter(1),reverse = True)
ordered_page_rank[1:10]
