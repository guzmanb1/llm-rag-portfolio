from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from flask import current_app
import logging

chat_history = []

def process_file(file_path):
    global qa_chain

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding = current_app.config["EMBEDDINGS"])

    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=current_app.config["LLM"],
        retriever=retriever,
        chain_type="stuff" 
    )

def answer_question(question):
    global chat_history
    global qa_chain

    output = qa_chain.invoke({"query": question})
    answer = output["result"]

    # Update the chat history
    chat_history.append((question, answer))

    return answer