from pkgs.lang.text_proc import VocabTagger
import mysql.connector


lang = 'pt'

vt = VocabTagger('pt')




conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database=lang,
    use_unicode=True,
    charset="utf8",
)

cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM {}.sentence ORDER BY id ASC".format(lang))
rows = cursor.fetchall()

for row in rows:
	
	sentence = row['title']

	verbs = vt.find_verbs(sentence)

	print(sentence)
	print(verbs)

	print("\n"*2)












# import io
# import os

# filepath = os.path.join(os.path.dirname(__file__), 'dummy_tr.txt')

# f = io.open(filepath, mode="r", encoding="utf-8")
	
# lines = f.readlines()

# for i, sent in enumerate(lines):

# 	print(sent)

# 	# print("{:<10}{:<50}".format(i, sent))
	
# 	verbs = vt.find_verbs(sent)

# 	# with VocabTagger() as tp:
# 	# 	verbs = tp.find_verbs(sent)

# 	print(verbs)

	

# 	print("\n"*3)