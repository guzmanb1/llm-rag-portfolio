from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

import logging
from .llm_client import embeddings,model

chat_history = []

def process_file(file_path):
    global qa_chain

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=model,
        retriever=retriever,
        chain_type="stuff" 
    )

def answer_question(question):
    global chat_history
    global qa_chain

    output = qa_chain.invoke({"question": question, "chat_history": chat_history})
    answer = output["result"]

    # Update the chat history
    chat_history.append((question, answer))

    return answer