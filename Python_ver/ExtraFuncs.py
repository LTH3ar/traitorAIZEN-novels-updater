from input import Input
from output import Output
from datetime import datetime
from subprocess import call
import shutil

class ExtraFuncs:
    def __init__(self, novels_list, novels_list_selected):
        self.novels_list = novels_list
        self.novels_list_selected = novels_list_selected
        self.input = Input(self.novels_list, self.novels_list_selected)
        self.output = Output(self.novels_list, self.novels_list_selected)
        self.now = datetime.now()

    #user input
    def novel_selected_add(self):
        index = int(input("index: "))
        for novel in self.novels_list:
            if novel.get_index() == index:
                self.novels_list_selected.append(novel)


    def novel_selected_remove(self):
        index = int(input("index: "))
        for novel in self.novels_list_selected:
            if novel.get_index() == index:
                self.novels_list_selected.remove(novel)

    def novel_selected_clear(self):
        self.novels_list_selected.clear()

    def novels_list_clear(self):
        self.novels_list.clear()

    def user_seach(self): # search by index or id or case insensitive title
        print("Search by index, id or title")
        search = input("option: ")
        if search.isdigit():
            for novel in self.novels_list:
                if novel.get_index() == int(search):
                    self.output.output_novel(novel)
        else:
            for novel in self.novels_list:
                if novel.get_id() == search:
                    self.output.output_novel(novel)
                elif novel.get_title().lower() == search.lower():
                    self.output.output_novel(novel)

    def custom_novel_add(self):
        index = int(input("index: "))
        novel_id = input("id: ")
        novel_title = input("title: ")
        novel_url = input("url: ")
        last_update = input("last update: ")
        self.input.input_novel(index, novel_id, novel_title, novel_url, last_update, self.novels_list)

    def backup_novels_list(self):
        # copy file to backup folder shutil
        shutil.copy("novels_list.json", "output/backup/novels_list_" + self.now.strftime("%d-%m-%Y_%H-%M-%S") + ".json")
        shutil.copy("novels_list_selected.json", "output/backup/novels_list_selected_" + self.now.strftime("%d-%m-%Y_%H-%M-%S") + ".json")
