
from bs4 import BeautifulSoup
from datetime import datetime
import re
from random import randint
from time import sleep
from Driver import chromedriver

import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


from random import randint
from time import sleep
import json


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install())

domain_list = [
"https://www.sothebys.com/en/buy/auction/2021/british-art-modern-contemporary?locale=en"
]



with open("Link_New.csv", "a", encoding="utf-8") as f:
    wr = csv.writer(f)
    for url in domain_list:
        print(url)
        open_page = driver.get(url)
        wait = WebDriverWait(open_page, 2000)

        sleep(randint(1,2))


        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

        areas = soup.findAll("div", {"class": "css-1up9enl"})

        for area in areas:
            get_link_link = area.find("a", {"class", "css-lys2zi"})
            try:
                get_artworkLINK_link = get_link_link.get("href")
                get_artworkLINK = "https://www.sothebys.com" + get_artworkLINK_link
            except:
                get_artworkLINK = ""
            if area.find("p", {"class": "css-8908nx"}) is not None:
                get_artist = area.find("p", {"class": "css-8908nx"}).get_text().strip()
            else:
                get_artist = ''
            if area.find("p", {"class", "css-17ei96f"}) is not None:
                get_title = area.find("p", {"class", "css-17ei96f"}).get_text().strip()
            else:
                get_title = ""
            if area.findAll("p", {"class", "css-1czdecl"})[1] is not None:
                get_price = area.findAll("p", {"class", "css-1czdecl"})[1].get_text().strip()
            else:
                get_price = "0"
            if area.find("p", {"class", "css-2r8rz8"}) is not None:
                get_final = area.find("p", {"class", "css-2r8rz8"}).get_text().strip()
            else:
                get_final = "0"



            print(get_artist, get_title, get_price, get_final)


            wr.writerows([[url,get_artist.title(), get_title.title(),get_price, get_final, get_artworkLINK]])