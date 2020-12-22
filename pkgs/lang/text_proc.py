# functions for processing text
import nltk
from nltk.tokenize import word_tokenize
import mysql.connector


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





# with VocabTagger() as text_proc:
   # do what you need
# at this point, the connection is safely closed.

class VocabTagger:
	def __init__(self, lang):
		"""
			lang
				de, en, es, fr, it, pt, tr

		"""

		self._db_connection = mysql.connector.connect(
			host="localhost",
			user="root",
			password="12345678",
			database=lang
			)
		self._db_cursor = self._db_connection.cursor()



	def find_verbs(self, text):

		verbs = []

		tokens = word_tokenize(text)

		for token in tokens:

			self._db_cursor.execute("SELECT verb_id FROM vconj WHERE conj_verb = %s", (token, ))
			
			result = self._db_cursor.fetchone()

			if result is not None:
				verb_id = result[0]
				self._db_cursor.execute("SELECT title FROM verb WHERE id='{}'".format(verb_id))
				verb_title = self._db_cursor.fetchone()[0]
				verbs.append(verb_title)

		return verbs

	def find_adjectives(self, text):
		pass

	def find_interjections(self, text):
		pass


	def __del__(self):
		self._db_connection.close()


	def __exit__(self, type, value, traceback):
		self._db_connection.close()



