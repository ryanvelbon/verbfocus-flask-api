"""
	This module is a collection of functions for webscraping Wiktionary.org
"""


import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def exists(word, lang):
	"""

    Parameters
    ----------
    word
        the word (search item)
    lang
        language; this has to be specified in English as a full
        word e.g., 'German' not 'DE'
        

    Returns
    -------
    bool
        True if there is a Wiktionary entry ``word`` for ``lang``
        else False; N.B. retuns false even if the word does exist
        but not for the specified language

    Notes
    -----
    A better solution would be to check for a URL which includes
    a fragment identifier specifying the language
    """

	url = "https://en.wiktionary.org/wiki/{}".format(word)
	req = requests.get(url, headers)
	soup = BeautifulSoup(req.content, 'html.parser')

	if 'Wiktionary does not yet have an entry' in str(req.content):
		return False
	elif soup.find_all(id=lang):
		return True
	else:
		# else the word does exist, but not in the requested language
		return False



