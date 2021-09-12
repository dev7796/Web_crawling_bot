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
next_page_var1=[]
with open('Final_posts_Links_before_page12.csv', newline='') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        Final_posts_list.append(row['Final_Posts_Links'])
#print(Final_posts_list)
#domain_list=['https://www.sothebys.com/en/buy/auction/2020/contemporary-art-evening-auction-2']
domain_list = Final_posts_list
# pattern = re.compile(r"window\.BC\.product = (.*);", re.MULTILINE)


for url in domain_list:
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    print(url)
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
    auction_title_list=[]
    auction_date=[]
    auction_location=[]
    auctionId_list=[]
    Final_price=[]
    title_list=[]
    url_list=[]
    starting_bid_list = []
    current_bid_list = []
    estimate_low_list=[]
    estimate_high_list = []
    displayName_list = []
    number_of_bids_list = []
    sold_list = []
    auction_date_and_Location = soup.find('p', attrs={"class": 'paragraph-module_paragraph18Regular__34C1i css-cgm4gv'})
    auction_title = soup.find('h1', attrs={"class": 'headline-module_headline24Regular__39bo- css-1xbkwaj'})
    print(auction_title)
    raw = soup.find('script', type='application/json').string.strip()
    data = json.loads(raw)
    #print(data['props']['pageProps']['lotsJson'])
    Final_dict = data['props']['pageProps']['lotsJson']['data']['auction']['lots']
    # for i in Final_dict:
    #     i.popitem()
    print(Final_dict)
    for i in Final_dict:
        Final_price.append(i['premiums'])
        title_list.append(i['title'])
        url_list.append(i['url'])
        starting_bid_list.append(i['startingBid'])
        current_bid_list.append(i['currentBid'])
        number_of_bids_list.append(i['numberOfBids'])
        auctionId_list.append(i['auctionId'])
        sold_list.append(i['sold'])
        if i['objectSet']!=None:
               if i['objectSet']['objects'][0]['object_']['creators']!=[]:
                    displayName_list.append(i['objectSet']['objects'][0]['object_']['creators'][0]['creator']['displayName'])
               else:
                   displayName_list.append('None')
        else:
            displayName_list.append('None')

        estimate_low_list.append(i['estimates']['low'])
        estimate_high_list.append(i['estimates']['high'])

        auction_date.append(re.split('>|<|<|> ', str(auction_date_and_Location))[2])
        auction_location.append(re.split('>|<|<|>|• ', str(auction_date_and_Location))[8])
        auction_title_list.append(re.split('>|<|<|>', str(auction_title))[2])

    df_final_price = pd.DataFrame(Final_price)
    df_final_price['auctionId'] = auctionId_list
    df_final_price['auctionTitle'] = auction_title_list
    df_final_price['auctionDate'] = auction_date
    df_final_price['auctionLocation'] = auction_location
    df_final_price['estimate_low'] = estimate_low_list
    df_final_price['estimate_high'] = estimate_high_list
    df_final_price['title'] = title_list
    df_final_price['displayName'] = displayName_list
    df_final_price['url'] = url_list
    df_final_price['startingBid'] = starting_bid_list
    df_final_price['currentBid'] = current_bid_list
    df_final_price['numberOfBids'] = number_of_bids_list
    df_final_price['sold'] = sold_list

    print(df_final_price)
    df = pd.DataFrame(Final_dict)
    #df_final_price.to_csv('first.csv')
    df_final_price.to_csv('before12.csv',mode='a')
