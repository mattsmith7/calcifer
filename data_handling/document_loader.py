from pprint import pprint

from llama_index.readers.json import JSONReader

file_path='./data/exchange_content.json'

documents = JSONReader().load_data(file_path)

class JsonData:
    def __init__(self):
        self.data = documents

    def retrieve_json_data(self):
        return self.data