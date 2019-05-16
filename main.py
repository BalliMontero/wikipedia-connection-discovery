from modules import wikilinker as wiki

run_again = 'y'
while run_again == 'y' or run_again == 'yes':
    wiki.wikiSearch(input('Enter starting topic: '), input('Enter ending topic: '))

    run_again = input('Run again? (y/n): ').lower()
