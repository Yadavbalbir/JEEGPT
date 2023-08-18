import pandas as pd
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
<<<<<<< HEAD
os.environ["OPENAI_API_KEY"] = "My_API_KEY"
=======
os.environ["OPENAI_API_KEY"] = ""
>>>>>>> 4770934458160b4633d04f17e6dc6e97916a1101


loader = DirectoryLoader('Dataset', glob="./*.txt", loader_cls=TextLoader)
documents = loader.load()
#splitting the text into
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)
# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

## here we are using OpenAI embeddings but in future we will swap out to local embeddings
embedding = OpenAIEmbeddings()

vectordb = Chroma.from_documents(documents=texts,
                                 embedding=embedding,
                                 persist_directory=persist_directory)
