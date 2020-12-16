import mysql.connector
import os
import io


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="de",
  use_unicode=True,
  charset="utf8",
)

cursor = db.cursor()

filepath = os.path.join(os.path.dirname(__file__),'coolj_de_verbs.txt')
f = io.open(filepath, mode="r", encoding="utf-8")

# rstrip() removes \n and any white space
lines = [line.rstrip() for line in f]

new_count = 0
duplicate_count = 0


for item in lines:


	
	sql = "SELECT 1 FROM verb WHERE title = '{}'".format(item)
	cursor.execute(sql)
	result = cursor.fetchone()
	if result is None:
		new_count += 1
		sql = u"INSERT INTO verb (title) VALUES (%s)"
		try:
			cursor.execute(sql, (item,))
		except mysql.connector.IntegrityError as err:
			print("Error: {}".format(err))
	else:
		duplicate_count += 1


print("File contained a total of {} items of which: \n ...... {} duplicates IGNORED \n ...... {} new items INSERTED into DB ".format(len(lines), duplicate_count, new_count))


db.commit()

