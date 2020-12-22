
import sys, os
import mysql.connector


import requests
from bs4 import BeautifulSoup

import re

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

output = "  Verb  #{}{:>20}{:>50}"



def exists(word, lang):

    url = "https://en.wiktionary.org/wiki/{}".format(word)
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    if 'Wiktionary does not yet have an entry' in str(req.content):
        return False
    elif soup.find_all(id=lang):
        return True
    else:
        # else the word does exist, but not in the requested language
        return False


def scrape_all_vconj(verb, lang):

    url = "https://en.wiktionary.org/wiki/{}".format(verb)
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    x = '<span class="mw-headline" id="{}">{}</span>'.format(lang, lang)

    lang_header = soup.find(lambda tag:tag.name=="h2" and x in str(tag))


    for h in lang_header.find_next_siblings(['h4', 'h5']):          

        if "Conjugation" in h.text:
            try:
                td_sample = h.find_next_sibling("div").find("div", {"class": "NavContent"}).find_all("td")[8]
            except:
                raise ValueError("skipped...")

            # if "#{}".format(lang) in str(td_sample):
            if "lang-fr" in str(td_sample): # --------------------USE VARIABLE for language
                conj_header = h
                break # break out of loop

    conj_not_found_error = "BeautifulSoup failed to find the Conjugation section for :   {}".format(verb)

    # if neither h4 nor h5 tag found for Conjugation
    if 'conj_header' not in locals():
        raise ValueError(conj_not_found_error)

    conj_div = conj_header.find_next_sibling("div")



    conj_content_div = conj_div.find("div", {"class": "NavContent"})

    td_tags = conj_content_div.find_all("td")

    conjs = []

    for index, item in enumerate(td_tags):

        if item.find("span") == None:
            pass
        else:
            conj = item.find("span").text
            conjs.append(conj)

    # for index, b in enumerate(conjs):
    #     print("{:>10} {:>10}".format(index, b))


    return conjs





# f1 = open('it_vconj_failed.txt', 'a')
# f1.write('-----------------------------------------------------------------\n')
# f2 = open('it_vconj_not_found.txt', 'a')
# f2.write('-----------------------------------------------------------------\n')


# failed = []
# not_found = []


def seed_vconj(verb):

    try:
        conjs = scrape_all_vconj(verb['title'], 'French')
    except ValueError as err:
        print(err.args)
        return
    # except:
    #     print("Verb #{}    {} --------------------------FAILED--------------------------------------------------".format(verb['id'], verb['title']))
    #     # f1.write(str(verb))
    #     # f1.write("\n")
    #     # failed.append(verb)
    #     return


    # except AttributeError as err:




    expected = 47 # expected number of conjugations (depends on language)

    if len(conjs) != expected:
        msg = "FAILED : expected {} conjugations, scraped {}".format(expected, len(conjs))
        print(output.format(verb['id'], verb['title'], msg))
        return

    bool_str = 0


    sql = """INSERT INTO fr.vppg (verb_id, gerund, past_participle)
                    VALUES ('{}', '{}', '{}')""".format(
                        verb['id'], conjs[0],conjs[1])

    try:
        cursor.execute(sql)
    except:
        print("sql statement failed.....")
        return


    sql = "INSERT INTO fr.vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    
    for i in range(6): # 6 personal pronouns
        cursor.execute(sql, (1+i, 4, verb['id'], conjs[2+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 5, verb['id'], conjs[8+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 6, verb['id'], conjs[14+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 7, verb['id'], conjs[20+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 8, verb['id'], conjs[26+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 9, verb['id'], conjs[32+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 10, verb['id'], conjs[38+i]))

    cursor.execute(sql, (2, 11, verb['id'], conjs[44]))
    cursor.execute(sql, (4, 11, verb['id'], conjs[45]))
    cursor.execute(sql, (5, 11, verb['id'], conjs[46]))
        

    db.commit()

    msg = "conjugated"
    print(output.format(verb['id'], verb['title'], msg))
    # print("{:>10} {:>10}".format(index, b))




if __name__ == "__main__":

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="",
        use_unicode=True,
        charset="utf8",
    )

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT id, title FROM fr.verb ORDER BY id ASC")

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

    for result in results[497:]:

        if(exists(result['title'], 'French')):
            
            # print("{} found".format(result['title']))

            seed_vconj(result)

        else:
            print("Verb #{}    {} --------------------------NOT FOUND--------------------------------------------------".format(result['id'], result['title']))
            # not_found.append(result)
            # f2.write(str(result))
            # f2.write("\n")

