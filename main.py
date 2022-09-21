import requests as r
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"
page = r.get(URL)

soup = BeautifulSoup(page.content, "lxml")

results = soup.find_all('h3', class_='country-name')

for result in results:
    print(result.prettify())