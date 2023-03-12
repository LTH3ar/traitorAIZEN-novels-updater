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

    def output_novels_list(self):
        for novel in self.novels_list:
            self.output_novel(novel)
            print("\n")

    def save_novels_list(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.novels_list, f, indent=4, default=lambda o: o.__dict__)

    def save_novels_list_selected(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.novels_list_selected, f, indent=4, default=lambda o: o.__dict__)