from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

from VectorStore import ChromaDB
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import chromadb
import os

class ChainConstructor:
    def __init__(self):
        pass

from pprint import pprint

model = Ollama(model="llama2:7b")
query = 'Products with the "Cloud Processing" tag'
# docs = ChromaDB().query_matches(10, query)

embedding = OpenAIEmbeddings(
    api_key=os.environ.get("OPENAI_API_KEY"),
    model="text-embedding-3-small"
)

persistent_client = chromadb.PersistentClient(path="./data/chroma")

vectorstore = Chroma(
    client=persistent_client,
    collection_name="calcifer_collection",
    embedding_function=embedding,
)

retriever = vectorstore.as_retriever(fetch_k=55, k=10)

template = """From the JSON context provided, list the name of every product that matches the request:
{context}

request: {question}
"""

prompt = PromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

pprint(chain.invoke(query))
