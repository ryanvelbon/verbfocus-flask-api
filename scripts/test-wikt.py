import pkgs.lang.wikt as w







# assert w.exists('think', 'English')



verb = 'decir'
lang = 'Spanish'






conjs = w.get_all_vconj(verb, lang)


# print(type(conjs))

for conj in conjs:
	print(conj)


# w.seed_vconj_table_for_verb(verb, lang)


