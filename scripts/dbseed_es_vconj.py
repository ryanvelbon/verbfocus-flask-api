
import sys, os

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


    sql = """INSERT INTO vppg (verb_id, gerund, ms, fs, mp, fp)
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
                        verb['id'],conjs[1],conjs[2],conjs[3],conjs[4],conjs[5])
    cursor.execute(sql)


    sql = "INSERT INTO vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    
    for i in range(6): # 6 personal pronouns
        cursor.execute(sql, (1+i, 4, verb['id'], conjs[6+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 5, verb['id'], conjs[12+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 6, verb['id'], conjs[18+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 7, verb['id'], conjs[24+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 8, verb['id'], conjs[30+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 9, verb['id'], conjs[36+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 10, verb['id'], conjs[42+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 11, verb['id'], conjs[48+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 12, verb['id'], conjs[54+i]))
    for i in range(5):
        cursor.execute(sql, (1+i, 13, verb['id'], conjs[60+i]))
    for i in range(5):
        cursor.execute(sql, (1+i, 14, verb['id'], conjs[65+i]))

    db.commit()

    print("Verb #{}    {}         has been conjugated".format(verb['id'], verb['title']))




if __name__ == "__main__":

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        # database="es", example it en de etc.
        use_unicode=True,
        charset="utf8",
    )

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT id, title FROM verb ORDER BY id ASC")

    results = cursor.fetchall()




    # # ----------------------------------------------------------------------------
    # # for testing, uncomment this section
    # # below is a list of verbs which failed to be conjugated

    # results = []

    # ids_of_verbs_which_failed = [
    #             # 378,
    #             # 821,
    #             # 1184,
    #             # 1614,
    #             # 1637,
    #             # 2019,
    #             896, # conj_div is None line 126
    #             # 2025, 2105, # resolved : was scraping wrong language Conjugation header
    # ]

    # for i in ids_of_verbs_which_failed:
    #     cursor.execute("SELECT id, title FROM verb WHERE id={}".format(i))
    #     results.append(cursor.fetchone())


    # # ----------------------------------------------------------------------------

    not_found = [] # a list of verbs which weren't found

    cursor.execute("TRUNCATE TABLE vppg")
    cursor.execute("TRUNCATE TABLE vconj")

    print("Warning! If this script freezes, restart PC. There is a problem pending diagnosis. Possibly something concering cache or RAM")

    for result in results:

        if(w.exists(result['title'], 'Spanish')):
            
            # print("{} found".format(result['title']))

            seed_vconj_es(result)

        else:
            print("Wiktionary entry not found for :     {}".format(result['title']))
            not_found.append(result)





