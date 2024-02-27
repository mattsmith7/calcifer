from langchain_community.callbacks.utils import load_json
import json
from pathlib import Path

class JSONLoader:
    def __init__(self):
        self.file_path='./data/exchange_content.json'

    def json_data(self):
        return json.loads(Path(self.file_path).read_text())
    
    def str_data(self):
        return load_json(Path(self.file_path))
    
    