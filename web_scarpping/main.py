import urllib.request
import requests
from bs4 import BeautifulSoup

URL = "https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&q="
with urllib.request.urlopen("https://www.sothebys.com/en/results    ") as url:
    s = url.read()
soup = BeautifulSoup(s)
#soup = BeautifulSoup(page.content, "html.parser")
print(soup)
