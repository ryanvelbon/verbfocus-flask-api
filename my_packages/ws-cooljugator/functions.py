import settings
import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# a lot of sites have precautions to fend off scrapers from accessing their data
# The first thing we can do to get around this is spoofing the headers we send along with our requests to make our scraper look like a legitimate browser
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/


def remove_auxiliaries(items, lang):

	all_words = set()
	
	for item in items:
		for word in item.split():
			all_words.add(word)

	results = []

	for word in all_words:
		results.append(word)

	results.sort()

	filtered_results = []

	if lang.upper() not in settings.SUPPORTED_LANGS:
		choices = ''
		for item in settings.SUPPORTED_LANGS:
			choices += item + ' '
		raise Exception("Invalid param. Choose one of the following languages:" + choices)

	# check if there is a DRY solution perhaps using eval()
	elif lang == 'en':
		unwanted = settings.UNWANTED_EN
	elif lang == 'es':
		unwanted = settings.UNWANTED_ES
	elif lang == 'it':
		unwanted = settings.UNWANTED_IT
	elif lang == 'tr':
		unwanted = settings.UNWANTED_TR
	else:
		pass
		# report error

	for item in results:
		if(item not in unwanted):
			filtered_results.append(item)

	return filtered_results


"""
	This function returns all the conjugations for a given verb by scraping cooljugator.com
"""
def cooljugate(lang, verb):
	pass

	url = "https://cooljugator.com/{lang}/{verb}".format(lang = lang, verb = verb)
	req = requests.get(url, headers)
	soup = BeautifulSoup(req.content, 'html.parser')

	conjugations = set()

	for conjugation in soup.findAll("div", {"class": "meta-form"}):
		conjugations.add(conjugation.text.strip())

	foobarresult = remove_auxiliaries(conjugations, lang)

	return foobarresult




# my_results = cooljugate('enf', 'think')

# print(my_results)
