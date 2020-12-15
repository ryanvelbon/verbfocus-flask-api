import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="es"
)

cursor = db.cursor()

sql = "INSERT INTO tense (title) VALUES (%s)"
val = [
	('infinitive',),
	('gerund',),
	('past participle',),
	('present indicative',),
	('imperfect indicative',),
	('preterite indicative',),
	('future indicative',),
	('conditional indicative',),
	('present subjunctive',),
	('imperfect (ra) subjunctive',),
	('imperfect (se) subjunctive',),
	('future subjunctive',),
	('imperative affirmative',),
	('imperative negative',)
]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, " entries were inserted.")