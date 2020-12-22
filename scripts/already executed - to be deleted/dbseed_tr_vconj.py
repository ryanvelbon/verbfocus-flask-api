
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
            nf1 = h.find_next_sibling("div", {"class":"NavFrame"})
            nf2 = nf1.find_next_sibling("div", {"class":"NavFrame"})
            nf3 = nf2.find_next_sibling("div", {"class":"NavFrame"})
            nf4 = nf3.find_next_sibling("div", {"class":"NavFrame"})
            break

    conjs = []

    for i, td in enumerate(nf1.find_all("td")):
        conjs.append(td.text)
    for i, td in enumerate(nf2.find_all("td")):
        conjs.append(td.text)
    for i, td in enumerate(nf3.find_all("td")):
        conjs.append(td.text)
    for i, td in enumerate(nf4.find_all("td")):
        conjs.append(td.text)


    # for i, conj in enumerate(conjs):
    #   print("{:<10} {}".format(i, conj))


    return conjs


def seed_vconj(verb):

    try:
        conjs = scrape_all_vconj(verb['title'], 'Turkish')
    except ValueError as err:
        print(err.args)
        return





    expected = 192 # expected number of conjugations (depends on language)

    if len(conjs) != expected:
        msg = "FAILED : expected {} conjugations, scraped {}".format(expected, len(conjs))
        print(output.format(verb['id'], verb['title'], msg))
        return

    sql = "INSERT INTO tr.vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    
    # cursor.execute(sql, (3, 30, verb['id'], "ihhampja"))



    # ---------------------------------------------------------------------------------


    tense_id = 0 # tense_id actually starts from 1.

    

    for i, conj in enumerate(conjs):
    
        person_id = (i%6)+1
        if person_id == 1:
            tense_id = tense_id+1



        # print("{} person, tense id : {} = {}".format(person_id, tense_id, conj))

        try:
            cursor.execute(sql, (person_id, tense_id, verb['id'], conj))
        except:
            print("sql statement failed... ")
            return


    # -----------------------------------------------------------------------------------



        

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

    cursor.execute("SELECT id, title FROM tr.verb ORDER BY id ASC")

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

    for result in results[5322:]:

        if(exists(result['title'], 'Turkish')):
            
            # print("{} found".format(result['title']))

            try:
                seed_vconj(result)
            except:
                pass

        else:
            print("Verb #{}    {} --------------------------NOT FOUND--------------------------------------------------".format(result['id'], result['title']))
            # not_found.append(result)
            # f2.write(str(result))
            # f2.write("\n")

