from classes.novel import Novel
import json

class Output:
    def __init__(self, novels_list, novels_list_selected):
        self.novels_list = novels_list
        self.novels_list_selected = novels_list_selected

    def output_novel(self, novel):
        print("Index: " + str(novel.get_index()))
        print("ID: " + novel.get_id())
        print("Title: " + novel.get_title())
        print("URL: " + novel.get_url())
        print("Last update: " + novel.get_last_update())

    def output_novels_list(self, lst):
        for novel in lst:
            self.output_novel(novel)
            print("\n")

    def save_novels_list(self, lst, file_name):
        with open(file_name, "w") as f:
            json.dump(lst, f, indent=4, default=lambda o: o.__dict__)
