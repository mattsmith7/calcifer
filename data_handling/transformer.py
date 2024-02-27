from llama_index.core import Settings
from llama_index.core.node_parser import JSONNodeParser
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
import tiktoken

from document_loader import JsonData

Settings.transformations = JSONNodeParser(chucnk_size=512)
Settings.chunk_size = 512
Settings.tokenizer = tiktoken.encoding_for_model("").encode
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

data = JsonData().retrieve_json_data()

index = VectorStoreIndex.from_documents(
    data, transformations=[JSONNodeParser(chunk_size=512)]
)