# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
import torch

emb = None
model = None

def init_llm():
    global model, emb
    
    model = AutoTokenizer.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        trust_remote_code=True
    )
    logging.debug("Modelo inicializado")
    emb = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    logging.debug("Embeddings inicializados")

