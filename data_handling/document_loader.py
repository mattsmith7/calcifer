import json
from pathlib import Path
from pprint import pprint

file_path='./data/exchange_content.json'
data = json.loads(Path(file_path).read_text())

print(data)