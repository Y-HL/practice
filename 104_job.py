import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

url = 'https://www.104.com.tw/jobs/search/?'
my_params = {'keyword': '大數據','order':'1','asc':'0','page':1,'mode':'s'}

res = requests.get(url,params=my_params ,headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

passw = soup.find('div', {"id":"js-job-content"}).find_all('a')[0]['href'].split('job/')[1].split('?')[0]

i=0
headers.update({'Referer':'https://www.104.com.tw/job/{}?jobsource=jolist_a_relevance'.format(passw)})
url2 = 'https://www.104.com.tw/job/ajax/content/{}'.format(passw)
resp=requests.get(url2,headers=headers)

jdata=json.loads(resp.text)
print(jdata)
