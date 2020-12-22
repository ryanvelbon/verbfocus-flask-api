import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="pt"
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
	('pluperfect indicative',),
	('future indicative',),

	('conditional',),

	('present subjunctive',),
	('imperfect subjunctive',),
	('future subjunctive',),
	
	('affirmative imperative',),
	('negative imperative',),
]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, " entries were inserted.")