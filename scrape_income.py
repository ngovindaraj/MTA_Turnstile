from bs4 import BeautifulSoup
import requests

def zipcode_to_capita(zipcode):
    url = "https://www.incomebyzipcode.com/newyork/{}".format(zipcode)
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html5lib")
    a = soup.findAll('table',{'class':'table table-responsive'})
    income_per_capita = a[2].findAll('td')[0].text
    return(int(income_per_capita.strip('$').replace(',', '')))
