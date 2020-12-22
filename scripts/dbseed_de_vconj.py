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
        pass
        # print("{:<10} {}".format(i, td.text))
        conjs.append(td.text)


    # indexes = [0,1,2,3,6,10,14,7,11,15,8,12,16,9,13,17,19,23,27,20,24,28,21,25,29,22,26,30,32,33]

    # for i in indexes:
    #     print(i)
    #     print(td_tags[i].text)

    # exit()


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
        conjs = scrape_all_vconj(verb['title'], 'German')
    except:
        return

    # ***EDIT***
    expected = 35

    if len(conjs) != expected:
        msg = "FAILED : expected {} conjugations, scraped {}".format(expected, len(conjs))
        print(output.format(verb['id'], verb['title'], msg))
        return

    # ***EDIT***
    sql = """INSERT INTO de.vppppa (verb_id, present_participle, past_participle, auxiliary)
                    VALUES ('{}', '{}', '{}', '{}')""".format(
                        verb['id'], conjs[1], conjs[2], conjs[3])

    try:
        cursor.execute(sql)
    except:
        print("sql statement failed.....")
        return


    sql = "INSERT INTO de.vconj (person_id, tense_id, verb_id, conj_verb) VALUES (%s, %s, %s, %s)"

    
    for p, i in enumerate([6, 10, 14, 7, 11, 15]):
        cursor.execute(sql, (1+p, 5, verb['id'], conjs[i]))
    for p, i in enumerate([8, 12, 16, 9, 13, 17]):
        cursor.execute(sql, (1+p, 6, verb['id'], conjs[i]))
    for p, i in enumerate([19, 23, 27, 20, 24, 28]):
        cursor.execute(sql, (1+p, 7, verb['id'], conjs[i]))
    for p, i in enumerate([21, 25, 29, 22, 26, 30]):
        cursor.execute(sql, (1+p, 8, verb['id'], conjs[i]))
    cursor.execute(sql, (2, 9, verb['id'], conjs[32][:39]))
    cursor.execute(sql, (5, 9, verb['id'], conjs[33][:39]))


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

    cursor.execute("SELECT id, title FROM de.verb ORDER BY id ASC")

    results = cursor.fetchall()

    print("Warning! If this script freezes, restart PC. There is a problem pending diagnosis. Possibly something concering cache or RAM")

    for result in results[1830:]:

        if(exists(result['title'], 'German')):
            
            # print("{} found".format(result['title']))

            try:
                seed_vconj(result)
            except:
                pass

        else:
            print("Verb #{}    {} --------------------------NOT FOUND--------------------------------------------------".format(result['id'], result['title']))
