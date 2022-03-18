import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas
import re
import json
import time

def get_url_by_index(json_data, i): #getting url from novel_url_list.json
    for dictionary in json_data:
        if dictionary['Index'] == i:
            return dictionary['URL']

def get_title_by_index(json_data, i): #getting title from novel_url_list.json
    for dictionary in json_data:
        if dictionary['Index'] == i:
            return dictionary['Title']

def get_data_from_web(url): # get the line of html code which contain "Last Edit:" and "by traitorAIZEN"
    update_data = str("")
    list_page = requests.get(url)
    soup1 = BeautifulSoup(list_page.content,'html5lib')
    titles = soup1.find_all('div', {"class":"smalltext modified"})
    
    for x in titles: #assign 'x' html code to 'update_data'
        if x.find(text=re.compile("Last Edit:")) and x.find(text=re.compile("by traitorAIZEN")):
            
            if x.find('strong') and x.find(text="Today"):
                update_data = str("< " + x.find(text=re.compile("Last Edit:")) + " Today " + x.find(text=re.compile("by traitorAIZEN")) + " >")
                break
            elif x.find(text="Yesterday"):
                update_data = str("< " + x.find(text=re.compile("Last Edit:")) + " Yesterday " + x.find(text=re.compile("by traitorAIZEN")) + " >")
                break
            else:
                update_data = str("<" + x.find(text=re.compile("by traitorAIZEN")) + ">")
                break

        else: # in case there is no html code containing these text
            update_data = str("none")
    
    # in case there is somthing wrong with the website
    if update_data == str(""):
        update_data = str("< No html data founded please check your website >")
        return update_data
    else:
        return update_data

start = time.time()

#convert number in index_list.txt to a list of number
my_file = open("index_list.txt", "r")
index = my_file.read()
index_list_temp = index.split("\n")
my_file.close()
index_list = []
for i in index_list_temp:
    index_list.append(int(i))
del index_list_temp

# read data in novel_url_list.json
json_data = json.load(open("novel_url_list.json"))


# put all the html code inside html_data_list
html_data_list = []
title_list = []
url_list = []
for i in index_list:
    url = get_url_by_index(json_data, int(i))
    get_data_from_web(url)
    html_data_list.append(get_data_from_web(url))
    title_list.append(get_title_by_index(json_data, int(i)))
    url_list.append(get_url_by_index(json_data, int(i)))

# save all the data from index_list and html_data_list to html_database.csv file
dict = {"ID": index_list ,"html_data": html_data_list}
df = pandas.DataFrame(dict)
df.to_csv('html_database_update.csv')
    
# Serializing json (optional)
json_object = json.dumps([{'Index': index_list, 'Title': title_list, 'URL': url_list, 'Last_update': html_data_list} for index_list, title_list, url_list, html_data_list in zip(index_list, title_list, url_list, html_data_list)], indent=4)
jsonFile = open("novel_last_update.json", "w")
jsonFile.write(json_object)
jsonFile.close()

end = time.time()

print("update complete")
print(end - start)
