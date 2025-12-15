# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import torch


def init_llm():
    global tokenizer, model, embeddings
    
    model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
    logging.debug("Modelo inicializado")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    logging.debug("Embeddings inicializados")

