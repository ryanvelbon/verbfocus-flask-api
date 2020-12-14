
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import pkgs.lang.cooljugator as cool
import pkgs.lang.wikt as w

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="polly_es",
  use_unicode=True,
  charset="utf8",
)

cursor = db.cursor()

cursor.execute("SELECT id, title FROM verb ORDER BY id ASC")

results = cursor.fetchall()

for result in results:

	if(w.exists(result[1], 'Spanish')):
		print("{} found".format(result[0]))
	else:
		print("Wiktionary entry not found for :     {}".format(result[1]))




	

