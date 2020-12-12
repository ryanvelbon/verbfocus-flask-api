import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


url_infixes = ['a',   'a1',   'a2',   'b',   'c',   'c1',   'd',   'd1',   'e',   'e1',   'f',   'g',   'h',   'i',   'j',   'k',   'l',   'm',   'n',   'o',   'p',   'p1',   'q',   'r',   'r1',   's',   't',   'u',   'v',   'w',   'x',   'y',   'z']

verbs = []

for infix in url_infixes:
	url = "https://www.vocabulix.com/conjugacion2/{}_spanish.html".format(infix)
	req = requests.get(url, headers)
	soup = BeautifulSoup(req.content, 'html.parser')

	divTag = soup.find_all("div", {"class": "indexWrapper"})[0]


	for item in divTag.find_all("a"):
		verb = item.text.strip()
		verbs.append(verb)
		print(verb)

# Remove every instance of 'más...' manually from the list.