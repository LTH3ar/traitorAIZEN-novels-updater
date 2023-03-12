class Novel:
    def __init__(self):
        self.__index = "N/A"
        self.__id = "N/A"
        self.__title = "N/A"
        self.__url = "N/A"
        self.__last_update = "N/A"

    def get_index(self):
        return self.__index

    def set_index(self, index):
        if isinstance(index, int):
            self.__index = index
        else:
            raise ValueError("Invalid index")

    def get_id(self):
        return self.__id

    def set_id(self, novel_id):
        if isinstance(novel_id, str) and len(novel_id) > 0:
            self.__id = novel_id
        elif novel_id == "":
            self.__id = "N/A"
        else:
            raise ValueError("Invalid novel ID")

    def get_title(self):
        return self.__title

    def set_title(self, novel_title):
        if isinstance(novel_title, str) and len(novel_title) > 0:
            self.__title = novel_title
        elif novel_title == "":
            self.__title = "N/A"
        else:
            raise ValueError("Invalid novel title")

    def get_url(self):
        return self.__url

    def set_url(self, novel_url):
        if isinstance(novel_url, str) and len(novel_url) > 0:
            self.__url = novel_url
        elif novel_url == "":
            self.__url = "N/A"
        else:
            raise ValueError("Invalid url")

    def get_last_update(self):
        return self.__last_update

    def set_last_update(self, last_update):
        if isinstance(last_update, str) and len(last_update) > 0:
            self.__last_update = last_update
        elif last_update == "" or last_update is None:
            self.__last_update = "N/A"
        else:
            raise ValueError("Invalid last update")
