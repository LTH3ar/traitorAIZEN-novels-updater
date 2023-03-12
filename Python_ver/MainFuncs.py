from classes.novel import Novel
from output import Output
from input import Input
import requests
from bs4 import BeautifulSoup
import json

class MainFuncs:
    def __init__(self, novels_list, novels_list_seleted, new_update_list):
        self.novels_list = novels_list
        self.novels_list_seleted = novels_list_seleted
        self.new_update_list = new_update_list
        # self.index_lst = []
        self.output = Output(self.novels_list, self.novels_list_seleted)
        self.input = Input(self.novels_list, self.novels_list_seleted)


    # scraper function
    # scrape list of novels from a website(set last_update to "N/A")
    def scrape_novels_list(self, url):
        page = requests.get(url)
        # target inside <div class="inner" data-msgid="38869" id="msg_38869">
        # key: tag <a> with attribute href, class="bbc_link", target="_blank", rel="noopener"
        # get all <a> tags with attribute href, class="bbc_link", target="_blank", rel="noopener"
        # id(inside the url of the novel, ex: index.php?topic=2013.msg23919 so get what ever after topic=)
        # title is the text inside the <a> tag
        # url is the href attribute
        # last_update is "N/A"(there will be another function to update this)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("a", href=True, class_="bbc_link", target="_blank", rel="noopener")
        tmp_id = int(0)
        index = int(0)
        for result in results:
            tmp_url = result["href"]
            if "topic=" in tmp_url:
                id = str(result["href"].split("topic=")[1].split("&")[0])
            else:
                id = str("NoID_" + str(tmp_id))
                tmp_id += 1

            self.input.input_novel(index, id, str(result.text), str(result["href"]), str("N/A"))
            index += 1

    def save_novels_list(self, file_name):
        self.output.save_novels_list(file_name)

    def load_novels_list(self, file_name):
        self.input.load_novels_list(file_name)

    def output_novels_list(self):
        self.output.output_novels_list()

    def novel_selected_import(self, file_name):
        self.input.load_novels_list_selected(file_name)

    def novel_selected_export(self, file_name):
        self.output.save_novels_list_selected(file_name)

    def update_novels_list(self, url, file_name1, file_name2):
        self.load_novels_list(file_name1)
        self.novel_selected_import(file_name2)
        for novel_selected in self.novels_list_seleted:
            for novel in self.novels_list:
                if novel_selected.get_id() == novel.get_id():
                    novel_selected.set_last_update(novel_selected.get_last_update())
        self.novel_selected_export(file_name2)

        self.novels_list = []
        self.scrape_novels_list(url)
        for novel_selected in self.novels_list_seleted:
            for novel in self.novels_list:
                if novel_selected.get_id() == novel.get_id():
                    novel.set_last_update(novel_selected.get_last_update())
        self.output.save_novels_list(file_name1)

    def scrape_novel_last_update(self, url):
        #span class="smalltext modified floatright mvisible", text Ex: Last Edit</span>: February 11, 2023, 10:36:48 PM by traitorAIZEN
        # focus on the text after "Last Edit</span>: ", text must contains "by traitorAIZEN"

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


    def update_novels_list_last_update(self): # must run after novels_list_seleted is filled
        for i in self.novels_list_seleted:
            for novel in self.novels_list:
                if i.get_id() == novel.get_id():
                    update = self.scrape_novel_last_update(novel.get_url())
                    if novel.get_last_update() != update:
                        novel.set_last_update(update)
                        self.new_update_list.append(novel)
                        self.output.output_novel(novel)
                        self.output.save_novels_list("novels_list.json")
        #self.output.save_novels_list("novels_list.json")

    def output_new_update_list(self):
        for item in self.new_update_list:
            print("Index: " + str(item.get_index()))
            print("ID: " + item.get_id())
            print("Title: " + item.get_title())
            print("URL: " + item.get_url())
            print("Last update: " + item.get_last_update())
        with open("new_update_list.json", "w") as f:
            json.dump(self.new_update_list, f, indent=4, default=lambda o: o.__dict__)


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