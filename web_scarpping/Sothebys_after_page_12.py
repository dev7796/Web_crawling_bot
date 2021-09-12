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

paragraphs=[]
auctionId=[]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome('Driver/chromedriver')

# domain_list = [
# "https://www.sothebys.com/en/buy/auction/2021/british-art-modern-contemporary?locale=en","https://www.sothebys.com/en/buy/auction/2021/eclectic?locale=en"
# ]
Final_posts_list=[]
with open('Final_after12.csv', newline='') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        Final_posts_list.append(row['Final_Page_Posts_Links'])
#print(Final_posts_list)

#domain_list=["https://www.sothebys.com/en/auctions/2011/modern-contemporary-mi0315.html?locale=en","https://www.sothebys.com/en/auctions/2020/contemporary-art-evening-sale-hk0927.html?p=1"]
# pattern = re.compile(r"window\.BC\.product = (.*);", re.MULTILINE)
domain_list=Final_posts_list
#domain_list=['https://www.sothebys.com/en/auctions/2018/signals-ls1802.html?p=1']
for url in domain_list:
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    print("this is url",url)
    open_page = driver.get(url)
    wait = WebDriverWait(open_page, 2000)

    sleep(randint(1,2))

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    #json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text()).get("auctionId")

    # script = soup.find("script", text=lambda x: x and "window.BC.product" in x).text
    # data = json.loads(re.search(pattern, script).group(1))
    #data = json.loads(soup.find_all('script', type='application/ld+json').string)

    #print(data)
    estimate_low_list = []
    estimate_high_list = []
    url_list = []
    lot_sold_list = []
    lot_sold_list_final = []
    title_list = []
    description_list = []
    description_list_final = []
    page_title_list = []
    page_date_location=[]
    page_date = []
    page_location=[]
    page_date_location_looped = []
    dict_final = {}

    raw = soup.find('div',id='AuctionsModule-auctionsMain')
    auction_date_and_Location = soup.find('div',attrs={"class":'AuctionsModule-auction-info'})
    estimate = soup.findAll('div', attrs={"class": "estimate"})
    top = soup.findAll('div', attrs={"class": "top"})
    bottom = soup.findAll('div', attrs={"class": "bottom"})
    type = soup.findAll('div', attrs={"class": ["title","expandToThreeLines"]})
    description = soup.findAll('div', attrs={"class": "description"})
    page_title = soup.findAll('div', attrs={"class" : "AuctionsModule-auction-title"})

    #print(auction_date_and_Location)

    for t in type:
        url_list.append(re.split('<|>|: |"',str(t))[6])
    #print(url_list)

    for t in type:
        title_list.append(re.split('\d. |<|>',str(t))[5].upper())
    #print(title_list)

    for e in estimate:

        if len(re.split(' ',str(e))) == 2:
            estimate_low_list.append('upon request')
        else:

            if re.split(' ',str(e))[2]!='Upon':
                estimate_low_list.append(re.split(' ',str(e))[2])
            else:
                estimate_low_list.append('upon request')
    print(len(estimate_low_list))

    for e in estimate:
        if len(re.split(' ',str(e))) == 2:
            estimate_high_list.append('upon request')
        else:
            if re.split(' ',str(e))[2]!='Upon':
                estimate_high_list.append(re.split(' ',str(e))[4])
            else:
                estimate_high_list.append('upon request')


    print(len(estimate_high_list))

    for t in top:
        lot_sold_list.append(re.split('<|>|: ',str(t)))

    for e in lot_sold_list:
        if len(e)>5:
            lot_sold_list_final.append(e[8])
        else:
            lot_sold_list_final.append('Not specified')
    #print(len(lot_sold_list_final))

    for d in description:
        description_list.append(re.split('<|>',str(d))[2])
    #print(description_list)

    for d in description_list:
        if len(d)>1:
            description_list_final.append(d)
        else:
            description_list_final.append('Not specified')
    #print(description_list_final)

    for pt in page_title:
        page_title_list.append(re.split('<|>',str(pt))[2])

    for i in range(len(title_list)-1):
        page_title_list.append(page_title_list[0])
    #print(page_title_list)

    #for m in range(len(title_list)-1):

    page_date_location.append(re.split('>|<|<|>|• ',str(auction_date_and_Location)))
    #print(page_date_location[0][4])

    for i in range(len(title_list)):
        page_date.append(page_date_location[0][4])
        page_location.append(page_date_location[0][5])
    #print(len(page_date_location_looped))
    dict_final={'auction_title':page_title_list, 'date':page_date, 'location':page_location, 'title':title_list, 'description':description_list_final, 'estimate_low(GBP)':estimate_low_list, 'estimate_high(GBP)':estimate_high_list, 'lot_sold':lot_sold_list_final, 'urls':url_list}

    df = pd.DataFrame(dict_final)

    df.to_csv('after12(F).csv',mode='a')

