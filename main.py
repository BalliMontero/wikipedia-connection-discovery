import wikipedia
import wikilinker as wiki

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
    wiki.wikilinker(suggestK1[0], suggestK2[0])

wikiSearch(input('Enter starting topic: '), input('Enter ending topic: '))
