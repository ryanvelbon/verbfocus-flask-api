import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="fr"
)

cursor = db.cursor()

sql = "INSERT INTO tense (title) VALUES (%s)"
val = [
	('infinitive',),
	('gerund',),
	('past participle',),
	('present indicative',),
	('imperfect indicative',),
	('past historic indicative',),
	('future indicative',),
	('conditional',),
	('present subjunctive',),
	('imperfect subjunctive',),
	('imperative',),
]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, " entries were inserted.")