from langchain_community.callbacks.utils import load_json
import json
from pathlib import Path

class JSONLoader:
    def __init__(self):
        pass
    
    def json_data(self, path: str):
        return json.loads(Path(path).read_text())
    
    def str_data(self, path: str):
        return load_json(Path(path))
    
    def get_id(self, path: str):
        with open(path, "r") as file:
            data = json.load(file)

            id = data["id"]
        file.close()

        return id
    
    