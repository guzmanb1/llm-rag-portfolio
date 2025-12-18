# Load model directly
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import logging
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import torch
from langchain_huggingface import HuggingFacePipeline

def init_llm():
    tokenizer = AutoTokenizer.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    )
    model = AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device_map = "auto"
    )   
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.2,
        do_sample=True
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