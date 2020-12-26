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


@app.route('/api/v1/resources/<lang>/sentences', methods=['GET'])
def sentences_filter(lang):

    query_parameters = request.args

    verb = query_parameters.get('verb')
    # adjective = query_parameters.get('adjective')
    # noun = query_parameters.get('noun')
    # theme = query_parameters.get('theme')
    # grammar = query_parameters.get('grammar')
    # min_char = query_parameters.get('min_char')
    # max_char = query_parameters.get('max_char')

    # query = "SELECT * FROM sentences WHERE"
    # to_filter = []

    if verb:
        
        conn = connect_to_db(lang)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM verb WHERE title = %s", (verb, ))
        result = cursor.fetchone()
        verb_id = result['id']

        cursor.execute("SELECT * FROM sentence_verb WHERE verb_id = %s", (verb_id, ))
        results = cursor.fetchall()

        sentences = []

        for result in results:
            id = result['sentence_id']
            cursor.execute("SELECT * FROM sentence WHERE id = %s", (id, ))
            sentence = cursor.fetchone()
            sentences.append(sentence)

        return jsonify(sentences)

    if not (verb or adjective or noun or theme or grammar or min_char or max_char):
        return page_not_found(404)


def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()