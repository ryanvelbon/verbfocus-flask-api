"""
	This module is a collection of functions for webscraping Wiktionary.org
"""


import requests
from bs4 import BeautifulSoup

import re

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


def scrape_all_vconj(verb, lang):
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

    # to avoid mistakenly web scraping "Old Spanish" section instead of "Spanish"
    # we scan the h2 element's text to see that it contains this unique HTML code
    x = '<span class="mw-headline" id="{}">{}</span>'.format(lang, lang)

    lang_header = soup.find(lambda tag:tag.name=="h2" and x in str(tag))

    for h4_tag in lang_header.find_next_siblings('h4'):
        if "Conjugation" in h4_tag.text:
            conj_header = h4_tag
            break

    # REVIEW: perhaps above forloop can be written something like this:
    # conj_header = soup.find_next_siblings(lambda tag:tag.name=="h4" and "Conjugation" in tag.text)


    # if Conjugation h4 tag not found, scan the h5 tags
    if 'conj_header' not in locals():
        for h5_tag in lang_header.find_next_siblings('h5'):
            if "Conjugation" in h5_tag.text:
                conj_header = h5_tag
                break

    # print(conj_header)







    conj_not_found_error = "BeautifulSoup failed to find the Conjugation section for :   {}".format(verb)

    # if neither h4 nor h5 tag found for Conjugation
    if 'conj_header' not in locals():
        if(verb.endswith("se")):
            # print("{} \n Searching {} instead".format(
            #     conj_not_found_error, verb.removesuffix('se')))
            try:
                return scrape_all_vconj(verb.removesuffix('se'), lang)
            except ValueError as err:
                print(err.args)
                return
            # return
        else:
            raise ValueError(conj_not_found_error)
            # return # is this necessary?
            # abort

    conj_div = conj_header.find_next_sibling("div")

    conj_content_div = conj_div.find("div", {"class": "NavContent"})
    td_tags = conj_content_div.find_all("td")

    for index, item in enumerate(td_tags):
        if item.text.strip() == "":
            del td_tags[index]

    conjs = []

    # conjugations without a hyperlink are inside a <div> tag instead of <span>
    for td_tag in td_tags:

        # print(td_tag.text)

        span_tag = td_tag.find("span")

        if span_tag is None:
            div_tag = td_tag.find("div")
            conj = div_tag.text.strip()
        else:
            conj = span_tag.text.strip()
            
        conjs.append(conj)

    return conjs

