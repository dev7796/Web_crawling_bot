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
Final_page_post_links_all_resolved=[]
Final_posts_list=[]
next_page_var1=[]
with open('after12.csv', newline='') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        if row['Final_Page_Posts_Links'] == 'Page Deleted' or row['Page_links'] == 'Page_links':
            print('NONE')
        else:
            Final_posts_list.append(row['Page_links'])
print(Final_posts_list)

for i in Final_posts_list:
    link=i.split('=')[0]
    for j in range(1,int(i.split('=')[1])+1):
        Final_page_post_links_all_resolved.append(link+'='+str(j))
print(Final_page_post_links_all_resolved)
df = pd.DataFrame({'Final_Page_Posts_Links': Final_page_post_links_all_resolved})
df.to_csv("Final_after12.csv")

