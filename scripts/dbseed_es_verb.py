import mysql.connector
import os
import io

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  # database="es", example it en de etc.
  use_unicode=True,
  charset="utf8",
)

cursor = db.cursor()

filepath = os.path.join(os.path.dirname(__file__),'dbseed_es_verb.txt')
f = io.open(filepath, mode="r", encoding="utf-8")

# rstrip() removes \n and any white space
lines = [line.rstrip() for line in f]


for item in lines:
	
	sql = u"INSERT INTO verb (title) VALUES (%s)"

	try:
		cursor.execute(sql, (item,))
	except mysql.connector.IntegrityError as err:
		print("Error: {}".format(err))


db.commit()

