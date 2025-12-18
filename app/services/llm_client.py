# Load model directly
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import logging
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import torch
from langchain_huggingface import HuggingFacePipeline

def init_llm():
    tokenizer = AutoTokenizer.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map = "auto",
        trust_remote_code=True
    )   
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
    )
    llm = HuggingFacePipeline(pipeline = pipe)
    logging.debug("Modelo inicializado")

    return llm

def init_embeddings():
    emb = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    logging.debug("Embeddings inicializados")

    return emb