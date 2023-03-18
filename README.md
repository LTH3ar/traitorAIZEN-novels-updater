traitorAIZEN-novels-update-checking-tool
==============================================================

1. Scrape or update list of novels:
-> scrape the list of novels to novels.json file, if the file
already exist then the program load the existing file then
scrape the new list then write the old "last_update" to the
new scraped list then save the new list to novels.json

==============================================================

2. Scrape last update time of all novels in the selected list:
-> load novels.json, novels_selected.json, use the selected
list to get urls from novels_list then access each url to
scrape the last update text, compare the scraped elements with
"last_update" elements in novels.json if they are different
and scraped elements is not ["N/A"] the overwrite the
"last_update" and append novels to a tmp list and append full
checked list of novel to tmp list full; after that save the list
to Update_dd-mm-yyyy_hh-mm-ss.json and Update_Full_dd_mm_yyyy...json
respectively.

==============================================================

3. Print list of novels
==============================================================

4. Print list of selected novels
==============================================================

5. Search novel(title, id)
==============================================================

6. Backup all files(novels.json, novels_selected.json)
==============================================================

7. Exit

