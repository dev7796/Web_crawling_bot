from bs4 import BeautifulSoup
from datetime import datetime
import json
import re
from bs4 import BeautifulSoup
import requests
import re
from random import randint
from time import sleep
import pandas as pd
import sqlalchemy
#from webdriver_manager.chrome import ChromeDriverManager


import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


from random import randint
from time import sleep
import json
matched=True
paragraphs=[]
auctionId=[]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome('Driver/chromedriver')
data = pd.read_csv('sourcepagelink.csv')
bottom = data.tail(1)

# domain_list = [
# "https://www.sothebys.com/en/buy/auction/2021/british-art-modern-contemporary?locale=en","https://www.sothebys.com/en/buy/auction/2021/eclectic?locale=en"
# ]
#domain_list=[bottom]
domain_list = ["https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&q=&"]
def next_page_ur():
    with open('sourcepagelink.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            next_page_var=row['Source_page_link']

    #print("this is page",next_page_var)
    return next_page_var

# fulltxt = open('sourcepagelink.csv', 'rb').read()
#
# laststring = fulltxt.split(b',')[-1]

# pattern = re.compile(r"window\.BC\.product = (.*);", re.MULTILINE)
next_page=[]

for url in range(50):
    if matched:


        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        print(url)
        open_page = driver.get(next_page_ur())
        wait = WebDriverWait(open_page, 2000)

        sleep(randint(1,2))

        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        #json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text()).get("auctionId")

        # script = soup.find("script", text=lambda x: x and "window.BC.product" in x).text
        # data = json.loads(re.search(pattern, script).group(1))
        #data = json.loads(soup.find_all('script', type='application/ld+json').string)

        #print(data)
        next_post = []
        repeat_post=[]


        tags = soup.find_all('a')
        tags = [tag for tag in tags if tag.has_attr('href')]
        links = [tag['href'] for tag in tags]
        #print(links)
        for i in links:
            if i.startswith('https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&q='):
                next_page.append(i)
            else:
                if i.startswith('https://www.sothebys.com/en/buy/auction/') or i.startswith('https://www.sothebys.com/en/auctions/'):
                    if i in next_post:
                        repeat_post.append(i)
                    else:
                        next_post.append(i)

        print(next_post)
        df = pd.DataFrame({'Post_links': [next_post]})

        df.to_csv("postlinks.csv", mode='a')
        df1= pd.DataFrame({'Source_page_link':[next_page[-1]]})
        df1.to_csv('sourcepagelink.csv',mode='a')
        # data = pd.read_csv('postlinks.csv')
        # bottom = data.tail(1)
        # print(bottom)
        # print(next_page)

        with open('sourcepagelink.csv', newline='') as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                next_page_var1 = row['Source_page_link']
            for i in range(len(next_page) - 1):

                if next_page_var1 == next_page[i]:

                    matched = False

        # print("this is next page", next_page[-1])


    else:
        break


