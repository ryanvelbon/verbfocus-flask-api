import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  # database="tr"
)

cursor = db.cursor()

val = []


for x in ["positive declarative", "positive interrogative", "negative declarative", "negative interrogative"]:
	for y in ["nonpast aorist", "nonpast imperfective", "nonpast prospective", "past perfective", "past imperfective"]:
		s = "{} direct {}".format(x,y)
		val.append((s,))
	for y in ["perfective", "aorist", "imperfective"]:
		s = "{} indirect {}".format(x,y)
		val.append((s,))


# for v in val:
# 	print(v)

sql = "INSERT INTO tr.tense (title) VALUES (%s)"


cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, " entries were inserted.")

