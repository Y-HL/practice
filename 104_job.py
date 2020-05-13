import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

page = 1
url = 'https://www.104.com.tw/jobs/search/?'
my_params = {'keyword': '大數據',\
             'order':'15','asc':'0','page':page,'mode':'s'}

res = requests.get(url,params=my_params ,headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

i = 0
passw = soup.find('div', {"id":"js-job-content"}).find_all('a')[i]['href'][21:26]

headers.update({'Referer':'https://www.104.com.tw/job/' + passw + '?jobsource=jolist_a_relevance'})
url2 = 'https://www.104.com.tw/job/ajax/content/' + passw
res2 = requests.get(url2,headers=headers)
jdata = json.loads(res2.text)

jobName = jdata['data']['header']['jobName'].replace('"', '_')
comName = jdata['data']['header']['custName']
appearDate = jdata['data']['header']['appearDate']
salary = jdata['data']['jobDetail']['salary']
salaryMin = jdata['data']['jobDetail']['salaryMin']
salaryMax = jdata['data']['jobDetail']['salaryMax']
industry = jdata['data']['industry']
hrName = jdata['data']['contact']['hrName']
