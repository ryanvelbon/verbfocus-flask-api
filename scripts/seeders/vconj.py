"""
	conjugates every verb for any given language

	uses en_verbs to produce en_vconjs
"""

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import pkgs.lang.cooljugator as cool


lang = 'es'
# catch

filepath = os.path.dirname(os.path.dirname(os.getcwd())) + '/db/{0}/{0}_verbs.txt'.format(lang)
# catch

with open(filepath, encoding = 'utf-8') as f:
	content = f.readlines()

verbs = [line.strip() for line in content]

d = {} # empty dictionary for storing verb and its conjugations

print('cooljugating...  this may take minutes')

for verb in verbs:
	d[verb] = cool.cooljugate(lang, verb)
	# catch: what if invalid verb given, or verb page does not exist

for key, value in d.items():
	print(key, value)

