from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate


from flask import current_app
import logging

chat_history = []

custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant.

Answer the user's question using ONLY the information provided in the context below.
If the answer cannot be found in the context, say exactly:
"I don't know based on the document."

Context:
{context}

Question:
{question}

Answer:
"""
)


def process_file(file_path):
    global qa_chain

    qa_chain = None
    vectorstore = None

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding = current_app.config["EMBEDDINGS"])

    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=current_app.config["LLM"],
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": custom_prompt}
    )

def answer_question(question):
    global qa_chain

    output = qa_chain.invoke({"query": question})
    answer = output["result"]

    return answer