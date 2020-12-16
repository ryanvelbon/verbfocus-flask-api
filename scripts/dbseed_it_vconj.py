
import sys, os

import pkgs.lang.wikt_it as w

import mysql.connector


f1 = open('it_vconj_failed.txt', 'a')
f1.write('-----------------------------------------------------------------\n')
f2 = open('it_vconj_not_found.txt', 'a')
f2.write('-----------------------------------------------------------------\n')


# failed = []
# not_found = []


def seed_vconj(verb):

    try:
        conjs = w.scrape_all_vconj(verb['title'], 'Italian')
    # except ValueError as err:
    #     print(err.args)
    #     return
    except:
        print("Verb #{}    {} --------------------------FAILED--------------------------------------------------".format(verb['id'], verb['title']))
        f1.write(str(verb))
        f1.write("\n")
        # failed.append(verb)
        return


    # except AttributeError as err:




    expected = 52 # expected number of conjugations (depends on language)

    if len(conjs) != expected:
        print("WARNING: expected {} conjugations, scraped {}".format(expected, len(conjs)))
        print("Press [Y]es to proceed \n")
        print("      ENTER or any other key to terminate script")
        ans = input()
        if ans.lower() == 'y':
            pass
        else:
            exit()

    bool_str = 0

    if(conjs[1]=='essere'):
        bool_str = 1

    sql = """INSERT INTO vppppga (verb_id, auxiliary_is_essere, gerund, present_participle, past_participle)
                    VALUES ('{}', {}, '{}', '{}', '{}')""".format(
                        verb['id'], bool_str ,conjs[2],conjs[3],conjs[4],conjs[5])

    try:
        cursor.execute(sql)
    except:
        print("sql statement failed.....")
        return


    sql = "INSERT INTO vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    
    for i in range(6): # 6 personal pronouns
        cursor.execute(sql, (1+i, 4, verb['id'], conjs[5+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 5, verb['id'], conjs[11+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 6, verb['id'], conjs[17+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 7, verb['id'], conjs[23+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 8, verb['id'], conjs[29+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 9, verb['id'], conjs[35+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 10, verb['id'], conjs[41+i]))
    for i in range(5):
        cursor.execute(sql, (2+i, 11, verb['id'], conjs[47+i]))

    db.commit()

    print("Verb #{}    {}         has been conjugated".format(verb['id'], verb['title']))




if __name__ == "__main__":

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="it",
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




    # cursor.execute("TRUNCATE TABLE vppppga")
    # cursor.execute("TRUNCATE TABLE vconj")

    print("Warning! If this script freezes, restart PC. There is a problem pending diagnosis. Possibly something concering cache or RAM")

    for result in results[14980:]:

        if(w.exists(result['title'], 'Italian')):
            
            # print("{} found".format(result['title']))

            seed_vconj(result)

        else:
            print("Verb #{}    {} --------------------------NOT FOUND--------------------------------------------------".format(result['id'], result['title']))
            # not_found.append(result)
            f2.write(str(result))
            f2.write("\n")





