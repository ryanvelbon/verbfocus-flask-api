import re
import os
import io

from pkgs.lang.text_proc import get_vocab

filepath = os.path.join(os.path.dirname(__file__), 'dummy_tr.txt')
f = io.open(filepath, mode="r", encoding = "utf-8")


full_text = f.read()

vocab = get_vocab(full_text)


v_past_neg = re.compile(r"[dt](ım|ın|ı|ık|ınız|ılar|im|in|i|ik|iniz|iler|um|un|u|uk|unuz|ular|üm|ün|ü|ük|ünüz|üler)$")

# (ma|me) # negatives

# present simple positive
# Clashes with too many nouns
v_pres = re.compile(r"(rım|rim|rum|rüm|rsın|rsin|rsun|rsün|r|rız|riz|ruz|rüz|rsınız|rsiniz|rsunuz|rsünüz|rlar|rler|arım|erim|arsın|ersin|ar|er|arız|eriz|arsınız|ersini|arlar|erler|ırım|irim|urum|ürüm|ırsın|irsin|ursun|ürsün|ır|ir|ur|ür|ırız|iriz|uruz|ürüz|ırsınız|irsiniz|ursunuz|ürsünüz|ırlar|irler|urlar|ürler)$")

v_fut = re.compile(r"y?(aca|ece)[kğ](ım|sın|ız|sınız|lar|im|sin|iz|siniz|ler)?$")

location = re.compile(r"(ta|da|de)(yim|sin|yiz|siniz|ler)?$")



pattern = v_past_neg

for word in vocab:
	if(re.search(pattern, word)):
		print(word)



# The Rule of Consonant Mutation
# -k changes to -ğ is operates when a vowel suffix is being added to a hard consonant.



# A reminder about buffer letter -N-
# A noun with the possessive suffix can be subject to further suffixes.
# Buffer letter -n- is used when adding second suffixes to possessed noun.


# This should work with any Turkish noun (not just places)


# All Turkish suffixes
# https://www.dnathan.com/language/turkish/tsd/
