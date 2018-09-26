from bs4 import BeautifulSoup
import requests
import pprint
url = "http://web.mta.info/developers/turnstile.html"
page = requests.get(url).text
soup = BeautifulSoup(page, features="html5lib")

urls = []
for a in soup.find_all('a', href=True):
    urls.append(["http://web.mta.info/developers/data/nyct/turnstile/" + a['href']])

urls = urls[35:]

pprint.pprint(urls)

with open('MTA_urls.txt', 'w') as file_handler:
    for item in urls:
        file_handler.write("{}\n".format(item[0]))
