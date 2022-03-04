from os import system
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas
import json

index_list = []
index_no = -1
#get title list
title_list = []
list_url = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869"
list_page = requests.get(list_url)
soup1 = BeautifulSoup(list_page.content,'html5lib')
titles = soup1.find_all('div',{"class":"inner", "id":"msg_38869"})
for t in titles:
    title = t.find_all('a')
    for x in title:
        title_list.append(x.text)
        index_no += 1
        index_list.append(index_no)


#get url list
url_list = []
req = Request("http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
href = soup.find_all('div',{"class":"inner", "id":"msg_38869"})
for i in href:
    h = i.findAll('a')
    for x in h:
        url_list.append(x.get('href'))




#save title_list and url_list to novel_url_list.csv file
'''dict = {
    "Title": title_list,
    "URL": url_list
    }'''
#df = pandas.DataFrame(dict)
#df.to_csv('novel_url_list.csv')

# Serializing json  
json_object = json.dumps([{'Index': index_list, 'Title': title_list, 'URL': url_list} for index_list, title_list, url_list in zip(index_list, title_list, url_list)], indent=4) 

jsonFile = open("novel_url_list.json", "w")
jsonFile.write(json_object)
jsonFile.close()

print(json_object)

