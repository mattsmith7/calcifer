import os
from pprint import pprint
from VectorStore import ChromaDB

docs = []
ids = []

for filename in os.listdir('./data/content'):
    f = os.path.join('./data/content', filename)

    docs.append(str(JSONLoader().json_data(f)))

for filename in os.listdir('./data/content'):
    f = os.path.join('./data/content', filename)

    ids.append(str(JSONLoader().get_id(f)))


# # ChromaDB().add_docs(docs, ids, embeds)