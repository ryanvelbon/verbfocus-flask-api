from pkgs.lang.text_proc import VocabTagger


vt = VocabTagger('tr')

import io
import os

filepath = os.path.join(os.path.dirname(__file__), 'tr_sentences.txt')

f = io.open(filepath, mode="r", encoding="utf-8")
	
lines = f.readlines()

for i, sent in enumerate(lines):

	print(sent)

	# print("{:<10}{:<50}".format(i, sent))
	
	verbs = vt.find_verbs(sent)

	# with VocabTagger() as tp:
	# 	verbs = tp.find_verbs(sent)

	print(verbs)

	

	print("\n"*3)