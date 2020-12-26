import mysql.connector
import os
import io
import sys

"""
You must specify two arguments when running this script:

>>> python -m scripts._dbseed_sentence tr my-turkish-sentences.txt
>>> python -m scripts._dbseed_sentence pt portuguese-romance.txt
"""


def main(argv):

	if(len(argv) != 2):
		print("No value assigned for 'lang' and 'filename'.")
		exit()

	lang = argv[0]
	filename = argv[1]

	db = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="12345678",
	  database=lang,
	  use_unicode=True,
	  charset="utf8",
	)

	cursor = db.cursor()

	filepath = os.path.join(os.path.dirname(__file__), filename)
	f = io.open(filepath, mode="r", encoding="utf-8")

	# rstrip() removes \n and any white space
	lines = [line.rstrip() for line in f]

	new_count = 0
	duplicate_count = 0

	failed = []
	duplicates = []

	for i, item in enumerate(lines):

		sql = u"SELECT 1 FROM sentence WHERE title = %s"

		try:
			cursor.execute(sql, (item,))
		except:
			failed.append(item)
			continue

		result = cursor.fetchone()
		if result is None:
			new_count += 1
			sql = u"INSERT INTO sentence (title) VALUES (%s)"
			try:
				cursor.execute(sql, (item,))
			except mysql.connector.IntegrityError as err:
				print("Error: {}".format(err))
		else:
			duplicates.append((i, item))

	print("\n\nFile contained a total of {} items of which:\n".format(len(lines)))
	print("{:>20} new items        will be inserted".format(new_count))
	print("{:>20} duplicates       will be ignored".format(len(duplicates)))
	print("{:>20} failed".format(len(failed)))
	print("\n")

	user_input = ''

	while user_input.lower() != 'z':

		print("\n"*2)
		print("Press D to view duplicates")
		print("Press F to view the failed to execute")
		print("Press C to commit changes to database")
		print("Press Z to exit without committing any changes to database")

		user_input = input()

		if user_input.lower() == 'c':
			db.commit()
			print("Congratulations! {} new sentences were INSERTED into DB".format(new_count))
			exit()
		elif user_input.lower() == 'd':
			for x in duplicates:
				print(x)
		elif user_input.lower() == 'f':
			for x in failed:
				print(x)


	print("Commit aborted")
	# db.close()



if __name__ == "__main__":
	main(sys.argv[1:])