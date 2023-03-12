from classes.novel import Novel
from output import Output
from input import Input
from MainFuncs import MainFuncs
from ExtraFuncs import ExtraFuncs
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
        self.extra_funcs = ExtraFuncs(self.novels_list, self.novels_list_seleted)
    def option_lst(self):
        print("1. Scrape novels list")
        print("2. print novels list")
        print("3. print novels list selected")
        print("3. save novels list")
        print("4. load novels list")
        print("5. save novels list selected")
        print("6. load novels list selected")
        print("7. update novels list")
        print("8. update novels list last update")
        print("9. add novel to selected list")
        print("10. exit")
        choice = int(input("option: "))
        if choice == 1:
            self.main_funcs.scrape_novels_list(self.main_url)
        elif choice == 2:
            self.main_funcs.output_novels_list(self.novels_list)
        elif choice == 3:
            self.main_funcs.output_novels_list(self.novels_list_seleted)
        elif choice == 4:
            self.main_funcs.load_novels_list(self.list_file)
        elif choice == 5:
            self.main_funcs.novel_selected_export(self.list_file_selected)
        elif choice == 6:
            self.main_funcs.novel_selected_import(self.list_file_selected)
        elif choice == 7:
            self.main_funcs.update_novels_list(self.main_url, self.list_file)
        elif choice == 8:
            self.main_funcs.update_novels_list_last_update(self.list_file)
        elif choice == 9:
            self.extra_funcs.novel_selected_add()
        elif choice == 10:
            exit()

