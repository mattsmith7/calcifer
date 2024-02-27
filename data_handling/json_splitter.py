import json
from pprint import pprint

from langchain.text_splitter import RecursiveJsonSplitter

from document_loader import JsonData

splitter = RecursiveJsonSplitter()

json_data = JsonData().retrieve_json_data()

# or a list of strings
texts = splitter.split_text(json_data=json_data, convert_lists=True)

pprint(texts[0])
pprint(texts[1])
pprint(texts[2])

print(len(texts))
print([len(text) for text in texts])