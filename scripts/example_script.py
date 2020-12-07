import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import pkgs.lang.cooljugator as cool



lang = 'en'

verbs = ['ask', 'cry', 'die', 'fly']

d = {} # empty dictionary for storing verb and its conjugations


for verb in verbs:
	d[verb] = cool.cooljugate(lang, verb)
	# bug: what if invalid verb given, or verb page does not exist


for key, value in d.items():
	print(key, value)



# print(d)
