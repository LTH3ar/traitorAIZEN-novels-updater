from os import system
import pandas
import json

def get_url_by_index(json_data, i):
    for dictionary in json_data:
        if dictionary['Index'] == int(i):
            return dictionary

# read data in novel_url_list.json
json_data = json.load(open("novel_url_list.json"))

#convert number in index_list.txt to a list of number
my_file = open("index_list.txt", "r")
index = my_file.read()
index_list_temp = index.split("\n")
my_file.close()
index_list = []
for i in index_list_temp:
    index_list.append(int(i))
del index_list_temp


old_data = pandas.read_csv ("html_database.csv", delimiter=',')
html_old = pandas.Series(old_data['html_data'])

new_data = pandas.read_csv ("html_database_2.csv", delimiter=',')
html_new = pandas.Series(new_data['html_data'])

confirmed_list = []

count = int(0)


for num in index_list:

    if html_new[count] != html_old[count]:
        confirmed_list.append(int(num))
    
    count += 1

for i in confirmed_list:
   updated_novel = get_url_by_index(json_data, int(i))
   print(updated_novel)
   print("\n")

print(confirmed_list)
