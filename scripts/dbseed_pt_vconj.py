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

    # print(str(lang_header))

    for h in lang_header.find_next_siblings(['h4', 'h5']):
        
        if "Conjugation" in h.text:
            nf = h.find_next_sibling("div", {"class":"NavFrame"})
            ncont = nf.find_all("div", {"class": "NavContent"})[0]
            # print(str(ncont))
            break

    td_tags = ncont.find_all("td")

    conjs = []

    for i, td in enumerate(td_tags):
        # print("{:<10} {}".format(i, td.text))
        conjs.append(td.text)


    # for index, item in enumerate(td_tags):

    #     if item.find("span") == None:
    #         pass
    #     else:
    #         conj = item.find("span").text
    #         conjs.append(conj)


    # for index, b in enumerate(conjs):
    #     print("{:>10} {:>10}".format(index, b))


    return conjs



def seed_vconj(verb):

    try:
        conjs = scrape_all_vconj(verb['title'], 'Portuguese')
    except:
        return

    # ***EDIT***
    expected = 80 # actually it's 76 there's 4 usless cells

    if len(conjs) != expected:
        msg = "FAILED : expected {} conjugations, scraped {}".format(expected, len(conjs))
        print(output.format(verb['id'], verb['title'], msg))
        return


    # # ***EDIT***
    sql = """INSERT INTO pt.vppg (verb_id, gerund, ms, mp, fs, fp)
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
                        verb['id'], conjs[9], conjs[10], conjs[11], conjs[12], conjs[13],)

    try:
        cursor.execute(sql)
    except:
        print("sql statement failed.....")
        return


    sql = "INSERT INTO pt.vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    
    for i in range(6):
        cursor.execute(sql, (1+i, 1, verb['id'], conjs[2+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 4, verb['id'], conjs[14+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 5, verb['id'], conjs[20+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 6, verb['id'], conjs[26+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 7, verb['id'], conjs[32+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 8, verb['id'], conjs[38+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 9, verb['id'], conjs[44+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 10, verb['id'], conjs[50+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 11, verb['id'], conjs[56+i]))
    for i in range(6):
        cursor.execute(sql, (1+i, 12, verb['id'], conjs[62+i]))

    for i in range(5):
        cursor.execute(sql, (2+i, 13, verb['id'], conjs[69+i]))
    for i in range(5):
        cursor.execute(sql, (2+i, 14, verb['id'], conjs[75+i]))
   

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

    cursor.execute("SELECT id, title FROM pt.verb ORDER BY id ASC")

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

    for result in results[4287:]:

        if(exists(result['title'], 'Portuguese')):
            
            # print("{} found".format(result['title']))

            seed_vconj(result)

        else:
            print("Verb #{}    {} --------------------------NOT FOUND--------------------------------------------------".format(result['id'], result['title']))
