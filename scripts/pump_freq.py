# This script pumps the frequency for the verbs read from a file containing a list of common verbs



import mysql.connector
import os
import io


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="es",
  use_unicode=True,
  charset="utf8",
)

cursor = db.cursor()

filepath = os.path.join(os.path.dirname(__file__),'es_verbs_500basicverbs.txt')
f = io.open(filepath, mode="r", encoding="utf-8")

# rstrip() removes \n and any white space
lines = [line.rstrip() for line in f]

new_count = 0
duplicate_count = 0


for item in lines:


	
	# sql = "SELECT id FROM verb WHERE title = '{}'".format(item)
	# cursor.execute(sql)
	# result = cursor.fetchone()
	sql = "UPDATE verb SET freq=1 WHERE title='{}'".format(item)
	cursor.execute(sql)


# print("File contained a total of {} items of which: \n ...... {} duplicates IGNORED \n ...... {} new items INSERTED into DB ".format(len(lines), duplicate_count, new_count))


db.commit()

