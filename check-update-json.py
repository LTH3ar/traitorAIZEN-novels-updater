from os import system
import pandas
import json

def get_url_by_index(json_data, i):
    for dictionary in json_data:
        if dictionary['Index'] == int(i):
            return dictionary

def get_Last_update(json_data, i): #getting title from novel_url_list.json
    for dictionary in json_data:
        if dictionary['Index'] == int(i):
            return dictionary['Last_update']

# read data in novel_url_list.json
#json_data = json.load(open("novel_url_list.json"))

#convert number in index_list.txt to a list of number
my_file = open("index_list.txt", "r")
index = my_file.read()
index_list_temp = index.split("\n")
my_file.close()
index_list = []
for i in index_list_temp:
    index_list.append(int(i))
del index_list_temp


old_data = json.load(open("novel_last_update.json"))

new_data = json.load(open("novel_update.json"))

confirmed_list = []

for i in index_list:
    x = get_Last_update(old_data, int(i))
    y = get_Last_update(new_data, int(i))

    if x != y:
        confirmed_list.append(int(i))
    else:
        continue

for i in confirmed_list:
   updated_novel = get_url_by_index(new_data, i)
   print(updated_novel)
   print("\n")

print(confirmed_list)
