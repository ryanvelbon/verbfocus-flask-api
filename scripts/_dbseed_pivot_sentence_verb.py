from pkgs.lang.text_proc import VocabTagger
import mysql.connector
import sys


lang = 'pt'

vt = VocabTagger(lang)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database=lang,
    use_unicode=True,
    charset="utf8",
)

cursor = conn.cursor(dictionary=True)
cursor.execute("TRUNCATE TABLE sentence_verb")
cursor.execute("SELECT * FROM sentence ORDER BY id ASC")
rows = cursor.fetchall()


insert_stmt = u"INSERT INTO sentence_verb (sentence_id, verb_id) VALUES (%s, %s)"


for sentence in rows:
	
	verbs = vt.find_verbs(sentence['title'])

	for verb in verbs:
		# handle exception
		cursor.execute(insert_stmt, (sentence['id'], verb['id']))

	sys.stdout.write("\r%d" % sentence['id'])
	sys.stdout.flush()


conn.commit()