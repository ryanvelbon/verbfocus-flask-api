import requests
from bs4 import BeautifulSoup

SUPPORTED_LANGS = ['DE', 'EN', 'ES', 'FR', 'IT', 'TR']


"""
	auxiliary verbs found in every Cooljugator verb's conjugation
"""
UNWANTED_DE = ['-', 'bin', 'bist', 'ist', 'habe', 'haben', 'habest', 'habet', 'habt', 'hast', 'hat', 'hatte', 'hatten', 'hattest', 'hattet', 'hätte', 'hätten', 'hättest', 'hättet', 'sei', 'seid', 'seien', 'seiet', 'sein', 'seist', 'sind', 'war', 'waren', 'warst', 'wart', 'werde', 'werden', 'werdest', 'werdet', 'wird', 'wirst', 'wäre', 'wären', 'wärst', 'wärt', 'würde', 'würden', 'würdest', 'würdet']
UNWANTED_EN = ['am', 'are', 'be', 'been', 'had', 'has', 'have', 'is', 'was', 'were', 'will', 'would']
UNWANTED_ES = ['ha', 'habremos', 'habrá', 'habrán', 'habrás', 'habré', 'habréis', 'habéis', 'había', 'habíais', 'habíamos', 'habían', 'habías', 'han', 'has', 'haya', 'hayamos', 'hayan', 'hayas', 'hayáis', 'he', 'hemos', 'hubiera', 'hubierais', 'hubieran', 'hubieras', 'hubiere', 'hubiereis', 'hubieren', 'hubieres', 'hubiese', 'hubieseis', 'hubiesen', 'hubieses', 'hubiéramos', 'hubiéremos', 'hubiésemos', 'no', 'me', 'nos', 'os', 'se', 'te']
UNWANTED_FR = ['-', 'a', 'aie', 'aient', 'aies', 'ait', 'as', 'aura', 'auraient', 'aurais', 'aurait', 'auras', 'aurez', 'auriez', 'aurions', 'aurons', 'auront', 'avaient', 'avais', 'avait', 'avez', 'aviez', 'avions', 'avons', 'ayez', 'ayons', 'es', 'est', 'eurent', 'eus', 'eussent', 'eusses', 'eussiez', 'eussions', 'eut', 'eûmes', 'eût', 'eûtes', 'furent', 'fus', 'fusse', 'fussent', 'fusses', 'fussiez', 'fussions', 'fut', 'fûmes', 'fût', 'fûtes', 'il/elle/on', 'ils/elles', 'je', 'j’ai', 'j’aie', 'j’aurai', 'j’aurais', 'j’avais', 'j’eus', 'j’eusse', 'j’étais', 'nous', 'ont', 'que', 'qu’il/elle/on', 'qu’ils/elles', 'sera', 'serai', 'seraient', 'serais', 'serait', 'seras', 'serez', 'seriez', 'serions', 'serons', 'seront', 'soient', 'sois', 'soit', 'sommes', 'sont', 'soyez', 'soyons', 'suis', 'tu', 'vous', 'étaient', 'étais', 'était', 'étiez', 'étions', 'êtes']
UNWANTED_ID = [] # INDONESIAN
UNWANTED_IT = ['-', 'abbia', 'abbiamo', 'abbiano', 'abbiate', 'avete', 'aveva', 'avevamo', 'avevano', 'avevate', 'avevi', 'avevo', 'avrai', 'avranno', 'avrebbe', 'avrebbero', 'avrei', 'avremmo', 'avremo', 'avreste', 'avresti', 'avrete', 'avrà', 'avrò',  'era', 'erano', 'eravamo', 'eravate', 'eri', 'ero', 'ha', 'hai', 'hanno', 'ho', 'sarai', 'saranno', 'sarebbe', 'sarebbero', 'sarei', 'saremmo', 'saremo', 'sareste', 'saresti', 'sarete', 'sarà', 'sarò', 'sei', 'sia', 'siamo', 'siano', 'siate', 'siete', 'sono', 'è']
UNWANTED_TR = ['mu?', 'musun?', 'musunuz?', 'muydu?', 'muyduk?', 'muydum?', 'muydun?', 'muydunuz?', 'muyum?', 'muyuz?', 'mı?', 'mısın?', 'mısınız?', 'mıydı?', 'mıyım?', 'mıyız?', 'mi?', 'misin?', 'misiniz?', 'miyim?', 'miyiz?']



headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


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

	if lang.upper() not in SUPPORTED_LANGS:
		choices = ''
		for item in settings.SUPPORTED_LANGS:
			choices += item + ' '
		raise Exception("Invalid param. Choose one of the following languages:" + choices)

	# check if there is a DRY solution perhaps using eval()
	elif lang == 'de':
		unwanted = UNWANTED_DE
	elif lang == 'en':
		unwanted = UNWANTED_EN
	elif lang == 'es':
		unwanted = UNWANTED_ES
	elif lang == 'fr':
		unwanted = UNWANTED_FR
	elif lang == 'it':
		unwanted = UNWANTED_IT
	elif lang == 'tr':
		unwanted = UNWANTED_TR
	else:
		pass
		# report error

	for item in results:
		if(item not in unwanted):
			filtered_results.append(item)

	return filtered_results


"""
	This function returns all the conjugations for a given verb by scraping cooljugator.com
	example: cooljugate('en', 'think')
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



