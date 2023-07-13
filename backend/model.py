from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os
os.environ["OPENAI_API_KEY"] = "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"
persist_directory = 'db'
embedding = OpenAIEmbeddings()


vectordb = Chroma(persist_directory=persist_directory,
                  embedding_function=embedding,
                  )

retriever = vectordb.as_retriever(search_kwargs={"k": 7})
# Set up the turbo LLM
turbo_llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-3.5-turbo'
)


# create the chain to answer questions
qa_chain = RetrievalQA.from_chain_type(llm=turbo_llm,
                                       chain_type="stuff",
                                       retriever=retriever,
                                       return_source_documents=True)

qa_chain.combine_documents_chain.llm_chain.prompt.messages[0].prompt.template = '''
Use the following pieces of context to answer the users question. \
If you don't know the answer, just say that you don't know, don't try to make up an answer. \
{context}
'''


## Cite sources
def process_llm_response(llm_response):
    return llm_response['result']
    # print('\n\nSources:')
    # for source in llm_response["source_documents"]:
    #     print(source.metadata['source'])


def JEEGPT(query):
    query = query
    llm_response = qa_chain(query)
    return process_llm_response(llm_response)
