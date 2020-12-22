import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="de"
)

cursor = db.cursor()

sql = "INSERT INTO tense (title) VALUES (%s)"
val = [
	('infinitive',),
	('present participle',),
	('past participle',),
	('auxiliary',),
	('present indicative',),
	('present subjunctive',),
	('preterite indicative',),
	('preterite subjunctive',),
	('imperative',),
]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, " entries were inserted.")