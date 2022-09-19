import requests as r
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = r.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

print(results.prettify())