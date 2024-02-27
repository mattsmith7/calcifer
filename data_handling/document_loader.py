from langchain_community.document_loaders import JSONLoader

import json
from pathlib import Path
from pprint import pprint

file_path='./data/exchange_content.json'
data = json.loads(Path(file_path).read_text())

class JsonData:
    def __init__(self):
        self.data = data

    def retrieve_json_data(self):
        return self.data