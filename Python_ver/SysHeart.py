from classes.novel import Novel
from output import Output
from input import Input
from MainFuncs import MainFuncs
import requests
from bs4 import BeautifulSoup
import json

class SysHeart:
    def __init__(self):
        self.novels_list = []
        self.novels_list_seleted = []
        self.new_update_list = []
        self.list_file = "novels_list.json"
        self.list_file_selected = "novels_list_selected.json"
        self.list_file_new_update = "new_update_list.json"
        self.main_url = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869"
        self.main_funcs = MainFuncs(self.novels_list, self.novels_list_seleted, self.new_update_list)
    def option_lst(self):
        choice = int(input("1. Scrape novels list \n2. print novels list \n3. save novels list \n4. load novels list \n5. test \n6. exit \n"))
        if choice == 1:
            self.main_funcs.scrape_novels_list(self.main_url)
        elif choice == 2:
            self.main_funcs.output_novels_list()
        elif choice == 3:
            self.main_funcs.save_novels_list(self.list_file)
        elif choice == 4:
            self.main_funcs.load_novels_list("novels_list.json")

        elif choice == 5:
            self.main_funcs.load_novels_list("novels_list.json")
            self.main_funcs.novel_selected_import(self.list_file_selected)
            self.main_funcs.update_novels_list_last_update()
            self.main_funcs.output_new_update_list()

        elif choice == 6:
            self.main_funcs.update_novels_list(self.main_url, self.list_file, self.list_file_selected)

        elif choice == 7:
            exit()
