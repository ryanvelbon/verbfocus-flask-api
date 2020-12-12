# functions for processing text
import nltk


def fix_casing(s):
	""" 
	Capitalizes first character and any character occurring right after .?!

	Parameters: 
	    s (str): The text to be processed
	  
	Returns: 
	    str
	"""
	pass

def fix_punctuation(s):
	pass


def fix_spacing(s):
	""" 
	Removes extra whitespace

	Parameters: 
	    s (str): The text to be processed
	  
	Returns: 
	    str
	"""
	return ' '.join(s.split())


def fix_syntax(s):
	pass


def validate_syntax(s):
	return fix_syntax(s) == s


def validate_chars(s, lang):
	pass


def get_all_chars(text):
	""" 
	Scans a string and returns an array of all unique characters

	Parameters: 
	    text (str): The text to be processed. The longer the better.
	  
	Returns: 
	    array : of all characters found

	Notes:
		useful for scanning long documents to validate characters
	"""

	chars = set()

	for c in text.lower():
		chars.add(c)

	temp = []

	for c in chars:
		temp.append(c)

	temp.sort()

	return temp

def get_vocab(text):

	tokens = nltk.word_tokenize(text.lower())

	temp = set(tokens)

	vocab = []

	for item in temp:
		vocab.append(item)

	vocab.sort()

	return vocab


