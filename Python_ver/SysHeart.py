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
        self.main_url = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869"
        self.main_funcs = MainFuncs(self.novels_list, self.novels_list_seleted, self.new_update_list)
        self.extra_funcs = ExtraFuncs(self.novels_list, self.novels_list_seleted)
    def option_lst(self):
        while True:
            print("\n1. Scrape novels list(new) or update novels list(existing file)")
            print("2. scrape last update of novels (save to file)")
            print("3. add novel to selected list")
            print("4. remove novel from selected list")
            print("5. show selected list")
            print("6. save selected list to file")
            print("7. load selected list from file")
            print("8. show new update list")
            print("9. backup all")
            print("10. exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                # reset novels_list_seleted, new_update_list, novels_list
                self.novels_list_seleted = []
                self.new_update_list = []
                self.novels_list = []
                if self.main_funcs.if_exist(self.list_file):
                    self.main_funcs.update_novels_list(self.main_url, self.list_file)
                else:
                    self.main_funcs.scrape_novels_list(self.main_url)
                    self.main_funcs.save_novels_list(self.list_file)

            elif choice == "2":
                self.main_funcs.update_novels_list_last_update(self.list_file, self.list_file_selected)
            elif choice == "3":
                self.extra_funcs.novel_selected_add()
            elif choice == "4":
                self.extra_funcs.novel_selected_remove()
            elif choice == "5":
                self.main_funcs.output_novels_list(self.novels_list_seleted)
            elif choice == "6":
                self.main_funcs.novel_selected_export(self.list_file_selected)
            elif choice == "7":
                self.main_funcs.novel_selected_import(self.list_file_selected)
            elif choice == "8":
                self.main_funcs.output_novels_list(self.new_update_list)
                self.main_funcs.output_new_update_list()
            elif choice == "9":
                self.extra_funcs.backup_novels_list()
            elif choice == "10":
                exit()
            else:
                print("Invalid choice")


