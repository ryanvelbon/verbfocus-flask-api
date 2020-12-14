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


def get_all_vconj(verb, lang):
    """
    Parameters
    ----------
    verb
        the verb to be conjugated
    lang
        language; this has to be specified in English as a full
        word e.g., 'German' not 'DE'
        

    Returns
    -------
    list
        returns a list of all conjugations in the exact same order
        as found on the Wiktionary page

    Notes
    -----
    This function currently supports Italian, Spanish
    """
    url = "https://en.wiktionary.org/wiki/{}".format(verb)
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    lang_header = soup.find(lambda tag:tag.name=="h2" and lang in tag.text)

    h4_tags = lang_header.find_next_siblings('h4')

    for h4_tag in h4_tags:
        if "Conjugation" in h4_tag.text:
            conj_header = h4_tag
            break

    if 'conj_header' not in locals():   
        print("BeautifulSoup failed to find the 'Conjugation' section for :   {}".format(verb))\
        # abort

    conj_div = conj_header.find_next_sibling("div")

    td_tags = conj_div.find_all("td")

    for index, item in enumerate(td_tags):
        if item.text.strip() == "":
            del td_tags[index]

    conjs = []

    for td_tag in td_tags:

        span_tag = td_tag.find("span")

        conj = span_tag.text.strip()

        conjs.append(conj)

    return conjs


def seed_vconj_table_for_verb(verb, lang):
    pass

