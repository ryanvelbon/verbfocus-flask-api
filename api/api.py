import flask
from flask import request, jsonify
import mysql.connector


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


@app.route('/api/v1/resources/<lang>/verbs/all', methods=['GET'])
def verbs_all(lang):
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database=lang,
        use_unicode=True,
        charset="utf8",
    )

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, title FROM {}.verb ORDER BY id ASC".format(lang))

    results = cursor.fetchall()

    return jsonify(results)



def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()