from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import json
import string
from urllib.parse import urlparse
import re
import time 

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
    for i,s in enumerate(double_url):
        if ']' in s:
            urls.append(s.split(']')[1].translate(table))
        else:
            urls.append(s)
    return urls

def feature_scrapping(url):
    features = {}
    soup = BeautifulSoup(requests.get(url).content,'html.parser')
    item_features = soup.find(class_='features').find('ul').text.strip()
    spec_url = soup.find(class_='specs')['href']
    spe_soup =BeautifulSoup(requests.get(spec_url).content,'html.parser')
    item = spe_soup.find(class_='p-name').text
    item_id = spe_soup.find(class_='h-entry topic unread')['id']
    date = spe_soup.find('time')['datetime']
    condition = re.compile(r'Condition')
    specs = spe_soup.find('li', class_='comment')
    condition = specs.find(text=condition)
    story = soup.find(class_='story').text.strip()
    visits = int(soup.find(class_='primary').find('strong').text.strip())
    phone_visit = float(soup.find(class_='secondary').find_all('strong')[0].text.strip('%'))/100
    tablet_visit = float(soup.find(class_='secondary').find_all('strong')[1].text.strip('%'))/100
    mehs = int(soup.find(id='total-mehs').text)
    type_meh = float(soup.find(id='referrals').find(class_='primary').find('strong').text.strip('%'))/100
    referrals = soup.find_all(class_='referrer')
    ref_dict = {}
    for ref in referrals:
        link = ref.find(class_='base')['href']
        parsed_uri = urlparse(link)
        web = parsed_uri.netloc.split('.')[-2]
        ref_dict[web] = float(ref['data-percentage'])
    sale_num = int(soup.find(id='sold-quantity').text)
    sale_revenue = int(soup.find(id = 'sold-revenue').text.strip('$'))
    poll_num = int(soup.find(class_='vote-count').text.split()[0])
    features['datetime']=date
    features['item_id']=item_id
    features['item_name']=item
    features['item_features']=item_features
    features['condition']=condition
    features['story']=story
    features['visits']= visits
    features['phone_visits']=phone_visit
    features['tablet_visits']=tablet_visit
    features['mehs']=mehs
    features['type_meh']=type_meh
    features['sale_num']=sale_num
    features['sale_revenue']=sale_revenue
    features['poll_num']=poll_num
    return {**features, **ref_dict}


if __name__=='__main__':
    urls = get_all_urls()[1:]
    rows = []
    for i, url in enumerate(urls):
        print (i)
        columns.append(feature_scrapping(url))
        time.sleep(np.random.randint(3,10))
    data = pd.DataFrame(rows)
    data.to_csv('meh_data',sep='\t')
        
        
        
    