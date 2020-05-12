import requests
from bs4 import BeautifulSoup

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

url = 'https://www.104.com.tw/jobs/search/?keyword=%E5%A4%A7%E6%95%B8%E6%93%9A&order=1&jobsource=2018indexpoc&ro=0'
# https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E5%A4%A7%E6%95%B8%E6%93%9A  &order=15&asc=0&page=5&mode=s&  jobsource=2018indexpoc
res = requests.get(url, headers)
soup = BeautifulSoup(res.text, 'html.parser')

test = soup.find('div', {"id":"js-job-content"}).find_all('article')
i=0

'''
print(test[i].find_all('a')[0].text)
print(test[i].find_all('a')[1].text)
print(test[i].find_all('p')[0].text)
print(test[i].find_all('span',{"class":"b-tag--default"})[0].text)
print(test[i].find_all('span',{"class":"b-tag--default"})[1].text)
print(test[i].find_all('a')[1]['href'])
print(test[i].find_all('a')[1]['title'])
'''
print('=====')
print(test[i].find_all('a')[0].text)
print(test[i].find_all('a')[0]['href'])
print('=====')
url2 = test[i].find_all('a')[0]['href']
res2 = requests.get('https:'+url2, headers)
soup2 = BeautifulSoup(res2.text, 'html.parser')
print(soup2)
#print(test[i])
