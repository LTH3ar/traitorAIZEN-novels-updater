# traitorAIZEN-novels-update-checking-tool
This is just a product of my laziness and it's only job is to check whether there is any new upload in the list of traitorAIZEN novels

This is how it works: 

'index_list.txt': store the index number of your novel list (you can find these number in 'novel_url_list.json')

step 1: 

run 's1-get-novels-list-from-website.py', this python file get a list of novels from http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869 and save it to 'novel_url_list.json'.



step 2: 

run 's2-get-html-code.py', this file will go through all number in 'index_list.txt' and use these number to get the url of novels from 'novel_url_list.json' which have matched index number --> access each of these url and get a specific line of html code from each of these website which have 'Last Edit:' and 'by traitorAIZEN'
and save all these data to 'html_database_update.csv'

IF YOU RUN THIS FILE FOR THE FISRT TIME rename the file to 'html_database.csv' this file serves as the original data to compare with the new 'html_database_update.csv' file the next time you run 's2-get-html-code.py' and BE PATIENT because the amount of time this process will take depend on how many novel in your list 



step 3:

run 's3-check-update.py', this program will compare data from 'html_database.csv' and 'html_database_update.csv' row by row and if there is any different it's going to output the info of the new update novels which including 'Title', 'URL'


after finish all these step delete the old 'html_database.csv' and replace it with 'html_database_update.csv'
