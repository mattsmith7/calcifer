import os
import pandas
import tiktoken

# set path for getting .env keys
path = os.environ["PATH"]

from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    model="text-embedding-3-small"
)

embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 8000  # the maximum for text-embedding-3-small is 8191

text = "This is a test document."

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    
    return num_tokens

tokens_count = num_tokens_from_string(text, embedding_encoding)

embeddings = embeddings_model.embed_documents(
    [
    text
    ]
)

embeddings_length = len(embeddings)


print("tokens count:", tokens_count)
print("embeddings length:", embeddings_length)
# print(embeddings)