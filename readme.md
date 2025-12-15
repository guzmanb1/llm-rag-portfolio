# RAG System with LLM and Flask

Proyecto personal orientado a inteligencia artificial aplicada.
Implementa un sistema de Retrieval-Augmented Generation (RAG)
utilizando un modelo de lenguaje local y una base vectorial.

## Features
- LLM local con Transformers
- Retrieval-Augmented Generation (RAG)
- Base vectorial con Chroma
- Backend en Flask
- Interfaz web simple (HTML + CSS + JS)

## Tech Stack
- Python
- Flask
- HuggingFace Transformers
- ChromaDB
- Sentence-Transformers

## How it works
1. Los documentos se vectorizan y almacenan en Chroma
2. El usuario realiza una consulta
3. Se recuperan los fragmentos más relevantes
4. El LLM genera una respuesta basada en el contexto

## Setup
```bash
pip install -r requirements.txt
python run.py
