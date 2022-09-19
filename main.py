import requests as r
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"
page = r.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="countries")

print(results.prettify())