import flask
from flask import request, jsonify
import mysql.connector


app = flask.Flask(__name__)
app.config["DEBUG"] = True



def connect_to_db(lang):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database=lang,
        use_unicode=True,
        charset="utf8",
    )

    return connection



# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Polly</h1>
            <p>Welcome to Polly!</p>'''


@app.route('/api/v1/resources/<lang>/verbs/all', methods=['GET'])
def verbs_all(lang):
    
    conn = connect_to_db(lang)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title FROM {}.verb ORDER BY id ASC".format(lang))
    results = cursor.fetchall()
    return jsonify(results)


@app.route('/api/v1/resources/<lang>/verbs', methods=['GET'])
def verbs_filter(lang):
    return
    # transitive/intransitive, reflexive, topic
    return jsonify(results)


@app.route('/api/v1/resources/<lang>/sentences/all', methods=['GET'])
def sentences_all(lang):
    
    conn = connect_to_db(lang)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title FROM {}.sentence ORDER BY id ASC".format(lang))
    results = cursor.fetchall()
    return jsonify(results)




def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()