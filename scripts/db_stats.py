import mysql.connector
import os
import io


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="",
  use_unicode=True,
  charset="utf8",
)

cursor = db.cursor()


print("="*70 + "\n" + "VERBS" + "\n" + "-"*70)
alignment = '{:>5}{:>15} verbs{:>15} conjugated'


langs = ('de',
		 # 'en',
		 'es',
		 # 'fr',
		 'it',
		 'pt',
		 'tr'
)


for lang in langs:
	cursor.execute("SELECT COUNT(*) FROM {}.verb".format(lang))
	n_verbs = cursor.fetchone()[0]
	cursor.execute("SELECT DISTINCT verb_id FROM {}.vconj".format(lang))
	n_conjs = len(cursor.fetchall())
	print(alignment.format(lang.upper(), n_verbs, n_conjs))




