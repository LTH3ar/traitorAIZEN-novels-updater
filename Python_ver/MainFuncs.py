import shutil
from classes.novel import Novel
from output import Output
from input import Input
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
class MainFuncs:
    def __init__(self, novels_list, novels_list_seleted, new_update_list):
        self.novels_list = novels_list
        self.novels_list_seleted = novels_list_seleted
        self.new_update_list = new_update_list
        self.now = datetime.now()
        # self.index_lst = []
        self.output = Output(self.novels_list, self.novels_list_seleted)
        self.input = Input(self.novels_list, self.novels_list_seleted)


    def if_exist(self, file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                if len(data) == 0:
                    return False
                else:
                    return True
        except:
            return False

    # scraper function
    # scrape list of novels from a website(set last_update to "N/A")
    def scrape_novels_list(self, url):
        # check if the novels_list.json file is exist or empty
        # if empty run the scrape_novels_list function
        # if not the run the update_novels_list function
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("a", href=True, class_="bbc_link", target="_blank", rel="noopener")
        tmp_id = int(0)
        index = int(0)
        #reset list
        self.novels_list.clear()

        for result in results:
            tmp_url = result["href"]
            if "topic=" in tmp_url:
                id = str(result["href"].split("topic=")[1].split("&")[0])
            else:
                id = str("NoID_" + str(tmp_id))
                tmp_id += 1

            self.input.input_novel(index, id, str(result.text), str(result["href"]), str("N/A"), self.novels_list)
            index += 1


    # import list of novels from a file, run the scrape_novels_list function & add the last_update to the novels_list
    def update_novels_list(self, url, file_name):
        novels_list_temp = []
        self.input.load_novels_list(file_name, novels_list_temp)
        self.scrape_novels_list(url)
        for i in self.novels_list:
            for j in novels_list_temp:
                if i.get_id() == j.get_id():
                    i.set_last_update(j.get_last_update())
        self.output.save_novels_list(self.novels_list, file_name)



    # scrape the last_update of a novel from a website
    def scrape_novel_last_update(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("span", class_="smalltext modified floatright mvisible")
        time_array = []
        for result in results:
            if "by traitorAIZEN" in result.text and result.text is not None:
                time_array.append(str(result.text.split("by traitorAIZEN")[0].split(": ")[1]))
            elif result.text is None:
                time_array.append(str("N/A"))

        if len(time_array) > 0:
            return str(time_array)
        else:
            return str("N/A")

    # update the last_update of the novels_list
    def update_novels_list_last_update(self, file_name1, file_name2):
        self.load_novels_list(file_name1)
        self.novel_selected_import(file_name2)
        for i in self.novels_list_seleted:
            for novel in self.novels_list:
                if i.get_id() == novel.get_id():
                    update = self.scrape_novel_last_update(novel.get_url())
                    if novel.get_last_update() != update:
                        novel.set_last_update(update)
                        self.new_update_list.append(novel)
                        self.output.output_novel(novel)
                        self.output.save_novels_list(self.novels_list, file_name1)
        #self.output.save_novels_list("novels_list.json")

    # output the new_update_list, save it to a file
    def output_new_update_list(self):
        for item in self.new_update_list:
            print("Index: " + str(item.get_index()))
            print("ID: " + item.get_id())
            print("Title: " + item.get_title())
            print("URL: " + item.get_url())
            print("Last update: " + item.get_last_update())

        filename = str("Update_" + self.now.strftime("%d-%m-%Y_%H-%M-%S") + ".json")
        path = str("output/update/")
        with open(filename, "w") as f:
            json.dump(self.new_update_list, f, indent=4, default=lambda o: o.__dict__)
        shutil.move(filename, path)

    def save_novels_list(self, file_name):
        self.output.save_novels_list(self.novels_list, file_name)

    def load_novels_list(self, file_name):
        self.input.load_novels_list(file_name, self.novels_list)

    def output_novels_list(self, lst):
        self.output.output_novels_list(lst)

    def novel_selected_import(self, file_name):
        self.input.load_novels_list(file_name, self.novels_list_seleted)

    def novel_selected_export(self, file_name):
        self.output.save_novels_list(self.novels_list_seleted, file_name)

    # extra only use for testing and moving data
    '''
    def index_list_int(self, file_name): # txt, index(int)
        with open(file_name, "r") as f:
            for line in f:
                self.index_lst.append(int(line))

    def get_novel_saved(self):
        for index in self.index_lst:
            self.novels_list_seleted.append(self.novels_list[index])
        with open("novels_list_selected.json", "w") as f:
            json.dump(self.novels_list_seleted, f, indent=4, default=lambda o: o.__dict__)
    '''