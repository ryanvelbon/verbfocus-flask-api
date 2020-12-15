import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="es"
)

cursor = db.cursor()

sql = "INSERT INTO person (id, title) VALUES (%s, %s)"
val = [
	(1, '1s'),
	(2, '2s'),
	(3, '3s'),
	(4, '1p'),
	(5, '2p'),
	(6, '3p')

]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, " entries were inserted.")