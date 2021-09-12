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
Final_posts_list=[]
next_page_var1=[]
html_post_list=[]
JS_post_list=[]
with open('postlinks.csv', newline='') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        for k,v in row.items():
            for i in v:
                if len(i)>10:
                    res = i.strip('][').split(",")

                    for j in res:
                        Final_posts_list.append(j.strip(" ' ' "))

                else:
                    continue

for i in Final_posts_list:
    if i.endswith('html'):
        html_post_list.append(i)
    else:
        JS_post_list.append(i)

df = pd.DataFrame({'Final_Posts_Links': html_post_list})
df2 = pd.DataFrame({'Final_Posts_Links': JS_post_list})
df2.to_csv("Final_posts_Links_before_page12.csv")
df.to_csv("Final_post_Links_after_page12.csv")




