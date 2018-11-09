from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import requests
import json
import string
from urllib.parse import urlparse
import re

def get_all_urls():
#   Get all the deal links from deal list page
#   Since list page needs refresh to show all the deals,  
    all_deal_link = []
    for i in range(1,20):
        all_deal_link.append('https://meh.com/forum/topics.json?page&{0}&category=deals&sort=date-created'.format(i))
    double_url = []
    for link in all_deal_link:
        raw_data = json.loads(requests.get(link).text)
        for x in raw_data:
            double_url.append(x['text']['raw'])
    table = str.maketrans(dict.fromkeys("()"))
    urls = []
    for s in enumerate(double_url):
        if ']' in s:
            urls.append(s.split(']')[1].translate(table))
        else:
            urls.append(s)
    return (urls)

def feature_scrapping(url):
    soup = BeautifulSoup(resp = requests.get(url).content,'html.parser')
    time = soup.find('time')['datetime']
    item_features = soup.find(class_='features').find('ul').text.strip()
    spec_url = soup.find(class_='specs')['href']
    spe_soup = BeautifulSoup(requests.get(spec_url).content,'html.parser')
    item = spe_soup.find(class_='p-name').text
    item_id = spe_soup.find(class_='h-entry topic unread')['id']
    condition = re.compile(r'Condition')
    specs = spe_soup.find('li', class_='comment')
    condition = specs.find(text=condition)
    story = soup.find(class_='story').text.strip()
    visits = int(soup.find(class_='primary').find('strong').text.strip())
    phone_visit = float(soup.find(class_='secondary').find_all('strong')[0].text.strip('%'))/100
    tablet_visit = float(soup.find(class_='secondary').find_all('strong')[1].text.strip('%'))/100
    mehs = int(soup.find(id='total-mehs').text)
    type_meh = float(soup.find(id='referrals').find(class_='primary').find('strong').text.strip('%'))/100
    sale_num = int(soup.find(id='sold-quantity').text)
    sale_revenue = int(soup.find(id = 'sold-revenue').text.strip('$'))
    poll_num = int(soup.find(class_='vote-count').text.split()[0])
    