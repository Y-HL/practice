import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

columns = ['jobName','comName','appearDate','salary','salaryMin','salaryMax','industry','hrName']
data=[]
jdata=[]
url = 'https://www.104.com.tw/jobs/search/?'
my_params = {'keyword': '大數據',\  # set the search keyword
            'order':'15','asc':'0','mode':'s'}

for page in range(2):  # set total download pages
    res = requests.get(url,params=my_params.update({'page':page+1}) ,headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    job_content = soup.find('div', {"id":"js-job-content"})

    for i in range(15):  # there are 15 job items in 1 page
        urlp = job_content.find_all('article')[i].find('a')['href']
        headers.update({'Referer':'https://www.104.com.tw/job/' + urlp[21:26] + urlp[36:]})
        url2 = 'https://www.104.com.tw/job/ajax/content/' + urlp[21:26]
        jdata = json.loads(requests.get(url2,headers=headers).text)['data']
        #print(jdata)
        content_data=[jdata['header']['jobName'].replace('"', '_'),\
                      jdata['header']['custName'],\
                      jdata['header']['appearDate'],\
                      jdata['jobDetail']['salary'],\
                      jdata['jobDetail']['salaryMin'],\
                      jdata['jobDetail']['salaryMax'],\
                      jdata['industry'],\
                      jdata['contact']['hrName']]

        data.append(content_data)
        print(content_data)

df = pd.DataFrame(data = data, columns = columns)
df.to_csv('./104_work.csv', index = 0, encoding = 'utf-8-sig')

# Thanks for jimmyyang886 -- https://github.com/jimmyyang886/Club-TEB101-homework104/blob/master/hw_job104_json2pandas.ipynb
#            Yuting(Tiffany)       
#            Walilei -- https://github.com/Walilei/Homeworks/blob/master/web%20crawler%20-%20104.py
