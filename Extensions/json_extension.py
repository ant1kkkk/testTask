import json


class JsonExtension:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def create_list_with_dict_search_values(self):
        with open(self.path_to_file, "r", encoding='UTF-8') as file:
            data = json.load(file)
        del data["search_type"]
        del data["format"]

        data_values = [value for value in data.values()]
        return data_values

    def crate_list_with_dict_values(self):
        data_values = [value for value in self.path_to_file.values()]
        return data_values
