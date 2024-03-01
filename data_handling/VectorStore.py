import os
import getpass
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from JSONLoader import JSONLoader
from JSONSplitter import JSONSplitter
from Embedder import Embedder

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

    def add_docs(self, docs: list, ids: list, embeddings: list = None, metadatas: list = None):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=docs,
        )

    # return all embeddings from Chroma colection
    def get_docs(self):
        return self.collection.get(include=['embeddings'])
    
    def query_matches(self, query: str):
        embedding = OpenAIEmbeddings(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model="text-embedding-3-small"
        )

        db = Chroma(
            client=self.persistent_client,
            collection_name="calcifer_collection",
            embedding_function=embedding,
        )

        return db.similarity_search(query, 10)

        # return self.collection.query(
        #     n_results=num,
        #     query_texts=texts
        # )