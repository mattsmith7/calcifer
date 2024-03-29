import os
import tiktoken

from langchain_openai import OpenAIEmbeddings

class Embedder:
    def __init__(self, model="text-embedding-3-small", encoding="cl100k_base"):
        # max token limit for text-embedding-3-small is 8191 tokens
        self.model = model
        self.encoding = encoding
        self.embeddings = []

        self.embeddings_model = OpenAIEmbeddings(
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            model=self.model
        )

    def create_embeddings(self, data: list):
        self.embeddings = self.embeddings_model.embed_documents(data)

        return self.embeddings
    
    def total_tokens(self, data: list):
        # returns the number of tokens for each string in data list
        encoding = tiktoken.get_encoding(self.encoding)
        num_tokens = 0

        for item in data:
            num_tokens += len(encoding.encode(item))
            print(len(encoding.encode(item)))

        return num_tokens