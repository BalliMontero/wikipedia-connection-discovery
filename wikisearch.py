'''
Docs --> https://pypi.org/project/wikipedia/
get search suggestion or search based on keyword (results=1)
use suggestion in page module in order to access url
get suggestion link
supply link to connection finder
'''

import wikipedia
import testpy3 as wiki


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
    
    wiki.wikilinker(suggestK1[0], suggestK2[0])

# get page url when exact title is known
def getPageUrl(pTitle):
    page = wikipedia.page(pTitle)
    if None not in page:
        page = page.url
    return page


#ny = wikipedia.page("Death")

#print (ny1, ny2)

wikiSearch("heat", "light")
