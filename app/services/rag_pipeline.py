from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate


from flask import current_app
import logging


custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant that receives documents as context and responds based on them.

Limit yourself to answering only what you are asked, no more and no less.

Use ONLY the information in the context below.
Do NOT use prior knowledge.
If the answer is not in the context, reply exactly:
"I don't know based on the document."

Context:
{context}

Question:
{question}

Answer:
"""
)


def process_file(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding = current_app.config["EMBEDDINGS"])

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    qa_chain = RetrievalQA.from_chain_type(
        llm=current_app.config["LLM"],
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": custom_prompt}
    )

    current_app.config["QA_CHAIN"] = qa_chain

def answer_question(question):
    qa_chain = current_app.config.get("QA_CHAIN")

    output = qa_chain.invoke({"query": question})
    answer = output["result"]

    return answer