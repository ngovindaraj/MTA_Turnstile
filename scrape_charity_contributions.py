from bs4 import BeautifulSoup
import requests
import re

def zipcode_to_capita(zipcode):
url = "http://www.city-data.com/zips/10001.html"
page = requests.get(url).text
soup = BeautifulSoup(page, features="html5lib")
b = soup.findAll('div',{'class':'hgraph'})
    str1 = str(b[15])
    charity_contribution = re.findall(r"\$[^ ]+", str1)[0].split('<')[0]
    return(int(charity_contribution.strip('$').replace(',', '')))

print(zipcode_to_capita(10002))
