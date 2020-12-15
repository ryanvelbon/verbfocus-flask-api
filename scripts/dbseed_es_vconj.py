
import sys, os

# sys.path.insert(1, os.path.join(sys.path[0], '../..'))
# import pkgs.lang.cooljugator as cool
import pkgs.lang.wikt as w

import mysql.connector


def seed_vconj_es(verb):

    try:
        conjs = w.scrape_all_vconj(verb['title'], 'Spanish')
    except ValueError as err:
        print(err.args)
        return


    # except AttributeError as err:




    expected = 70 # expected number of conjugations (depends on language)

    if len(conjs) != expected:
        print("WARNING: expected {} conjugations, scraped {}".format(expected, len(conjs)))
        print("Press [Y]es to proceed \n")
        print("      ENTER or any other key to terminate script")
        ans = input()
        if ans.lower() == 'y':
            pass
        else:
            exit()



    sql = "INSERT INTO vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    
    # for i in range(6): # 6 personal pronouns
    #     cursor.execute(sql, (1+i, 4, verb['id'], conjs[6+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 5, verb['id'], conjs[12+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 6, verb['id'], conjs[18+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 7, verb['id'], conjs[24+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 8, verb['id'], conjs[30+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 9, verb['id'], conjs[36+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 10, verb['id'], conjs[42+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 11, verb['id'], conjs[48+i]))
    # for i in range(6):
    #     cursor.execute(sql, (1+i, 12, verb['id'], conjs[54+i]))
    # for i in range(5):
    #     cursor.execute(sql, (1+i, 13, verb['id'], conjs[60+i]))
    # for i in range(5):
    #     cursor.execute(sql, (1+i, 14, verb['id'], conjs[65+i]))

    db.commit()

    print("Verb #{}    {}         has been conjugated".format(verb['id'], verb['title']))




if __name__ == "__main__":

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="polly_es",
        use_unicode=True,
        charset="utf8",
    )

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT id, title FROM verb ORDER BY id ASC")

    results = cursor.fetchall()


    not_found = [] # a list of verbs which weren't found

    cursor.execute("TRUNCATE TABLE vconj")

    for result in results[2100:]:

        if(w.exists(result['title'], 'Spanish')):
            
            # print("{} found".format(result['title']))

            seed_vconj_es(result)

        else:
            print("Wiktionary entry not found for :     {}".format(result['title']))
            not_found.append(result)





