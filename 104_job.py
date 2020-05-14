import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

columns = ['jobName','comName','appearDate','salary','salaryMin','salaryMax','industry','hrName']
data = []
content_data=[]
jdata=[]

for page in range(1):
    url = 'https://www.104.com.tw/jobs/search/?'
    my_params = {'keyword': '大數據',\
                 'order':'15','asc':'0','page':page+1,'mode':'s'}

    res = requests.get(url,params=my_params ,headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    job_content = soup.find('div', {"id":"js-job-content"})

    #i = 0 # 
    for i in range(2):
    
        passw = job_content.find_all('div',{'class':'b-block__left'})[i].find('a')['href'][21:26]
        headers.update({'Referer':'https://www.104.com.tw/job/' + passw + '?jobsource=jolist_a_relevance'})
        print(headers)
        url2 = 'https://www.104.com.tw/job/ajax/content/' + passw
        print(url2)
        res2 = requests.get(url2,headers=headers)
        jdata = json.loads(res2.text)

        content_data.append(jdata['data']['header']['jobName'].replace('"', '_'))
        content_data.append(jdata['data']['header']['custName'])
        content_data.append(jdata['data']['header']['appearDate'])
        content_data.append(jdata['data']['jobDetail']['salary'])
        content_data.append(jdata['data']['jobDetail']['salaryMin'])
        content_data.append(jdata['data']['jobDetail']['salaryMax'])
        content_data.append(jdata['data']['industry'])
        content_data.append(jdata['data']['contact']['hrName'])

        #data.append(content_data)
        print(content_data)



df = pd.DataFrame(data = data, columns = columns)
df.to_csv('./104_work.csv', index = 0, encoding = 'utf-8-sig')

# thanks for Walali -- https://github.com/Walilei/Homeworks/blob/master/web%20crawler%20-%20104.py
