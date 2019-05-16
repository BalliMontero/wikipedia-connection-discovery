# Wikipedia Connection Discovery
Code base forked from: https://github.com/Mgancita/wikipedia_connection_finder/
## About
  Web crawling application which finds the most efficient internal wikipedia webpage connection between two wikipedia webpages based on a supplied topic.

  It is intended for use in knowledge graph generation and idea linkage. Students and researchers are encouraged to test and critique this use case.

  Development is ongoing so your feedback is useful

## Requirements
  * Python 3+
    * wikipedia
    * bs4
    * networkx
    * requests
    * urllib.parse

* Python 2 may be used by replacing `urllib.parse` with `urllib` in both *./requirements.txt* and *./modules/functions.py*

## Usage
Install dependencies:

  `pip install -r requirements.txt`

Run [test]:

  `python main.py`

  Test with any of the word pairs in the `results-images` folder

## To do
  + Asynchronous Discovery
  + Multiple words or phrases
  + Explore `wikipedia` module for opportunities to optimise
