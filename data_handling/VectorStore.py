import os
import getpass
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from JSONLoader import JSONLoader

class ChromaDB:
    def __init__(self, model="text-embedding-3-small", open_api_key=os.environ.get("OPENAI_API_KEY"), chroma_path="./data/chroma"):
        self.model = model
        self.open_api_key = open_api_key
        self.chroma_path = chroma_path

        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model_name="text-embedding-3-small"
        )

        self.persistent_client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.persistent_client.get_or_create_collection(name="calcifer_collection", embedding_function=self.embedding_function)

        # self.langchain_chroma = Chroma(
        #     client=self.persistent_client,
        #     collection_name="calcifer_collection",
        #     embedding_function=self.embedding_function,
        # )

    def get_collection(self, name: str):
        return self.persistent_client.get_collection(name)

    def get_collection_settings(self,):
        return self.persistent_client.get_settings()

    def add_docs(self, docs: list, ids: list, metadatas: list = None, embeddings: list = None):
        self.collection.add(
            documents=docs,
            ids=ids,
            metadatas=metadatas,
            embeddings=embeddings
        )

from pprint import pprint

docs = []
ids = []

for filename in os.listdir('./data/content'):
    f = os.path.join('./data/content', filename)

    docs.append(JSONLoader().json_data(f))

for filename in os.listdir('./data/content'):
    f = os.path.join('./data/content', filename)

    ids.append(JSONLoader().get_id(f))

pprint(docs[:3])

# ChromaDB().add_docs(docs, ids)

# pprint(ChromaDB().get_collection("calcifer_collection"))