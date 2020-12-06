import cooljugator.functions as f


lang = 'en'

verbs = ['ask', 'cry', 'die', 'fly']

d = {} # empty dictionary for storing verb and its conjugations


for verb in verbs:
	d[verb] = f.cooljugate(lang, verb)
	# bug: what if invalid verb given, or verb page does not exist


for key, value in d.items():
	print(key, value)



# print(d)
