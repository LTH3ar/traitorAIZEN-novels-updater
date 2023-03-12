from classes.novel import Novel
import json

class Input:
    def __init__(self, novels_list, novels_list_selected):
        self.novels_list = novels_list
        self.novels_list_selected = novels_list_selected

    # novels_list
    def input_novel(self, index, novel_id, novel_title, novel_url, last_update, lst):
        novel = Novel()
        novel.set_index(index)
        novel.set_id(novel_id)
        novel.set_title(novel_title)
        novel.set_url(novel_url)
        novel.set_last_update(last_update)
        lst.append(novel)

    def load_novels_list(self, file_name, lst):
        #reset list
        lst.clear()
        with open(file_name, "r") as f:
            data = json.load(f)
            for novel in data:
                self.input_novel(novel["_Novel__index"], novel["_Novel__id"], novel["_Novel__title"], novel["_Novel__url"], novel["_Novel__last_update"], lst)