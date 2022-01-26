from abc import update_abstractmethods
from os import system
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas
import re
import json

def get_url_by_index(json_data, i):
    for dictionary in json_data:
        if dictionary['Index'] == i:
            return dictionary['URL']

def get_data_from_web(url): # get the line of html code which contain "Last Edit:" and "by traitorAIZEN"
    global update_data # make sure python don't mistake 'update_data' as a new variable and only update this variable
    list_page = requests.get(url)
    soup1 = BeautifulSoup(list_page.content,'html5lib')
    titles = soup1.find_all('div', {"class":"smalltext modified"})
    
    for x in titles: #assign 'x' html code to 'update_data'
        if x.find(text=re.compile("Last Edit:")) and x.find(text=re.compile("by traitorAIZEN")):
            update_data = x
            break

#convert number in index_list.txt to a list of number
my_file = open("index_list.txt", "r")
index = my_file.read()
index_list = index.split("\n")
my_file.close()

# read data in novel_url_list.json
json_data = json.load(open("novel_url_list.json"))


# put all the html code inside html_data_list
html_data_list = []
update_data = "place holder"
for i in index_list:
    url = get_url_by_index(json_data, int(i))
    get_data_from_web(url)
    html_data_list.append(update_data)

# save all the data from index_list and html_data_list to html_database.csv file
dict = {"ID": index_list ,"html_data": html_data_list}
df = pandas.DataFrame(dict)
df.to_csv('html_database_update.csv')
    
