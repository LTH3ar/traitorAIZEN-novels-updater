from os import system
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import time

index_list = []
title_list = []
url_list = []
index_no = -1
list_url = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869"


def get_title_list(list_url, index_no):
	list_page = requests.get(list_url)
	soup = BeautifulSoup(list_page.content,'html5lib')
	titles = soup.find_all('div',{"class":"inner", "id":"msg_38869"})
	for t in titles:
		title = t.find_all('a')
		for x in title:
			title_list.append(x.text)
			index_no += 1
			index_list.append(index_no)
	return title_list

def get_url_list(list_url):
	req = Request(list_url)
	html_page = urlopen(req).read()
	soup = BeautifulSoup(html_page, "lxml")
	href = soup.find_all('div',{"class":"inner", "id":"msg_38869"})
	for i in href:
		h = i.find_all('a')
		for x in h:
			url_list.append(x.get('href'))
	return url_list

start = time.time()

get_title_list(list_url, index_no)
get_url_list(list_url)

# Serializing json  
json_object = json.dumps([{'Index': index_list, 'Title': title_list, 'URL': url_list} for index_list, title_list, url_list in zip(index_list, title_list, url_list)], indent=4) 

jsonFile = open("novel_url_list.json", "w")
jsonFile.write(json_object)
jsonFile.close()

end = time.time()

print("Link scraping complete")
print(end - start)
