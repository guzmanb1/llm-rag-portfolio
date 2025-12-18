from flask import Flask
from .config import config
from .routes import task_routes
from .services.llm_client import init_llm, init_embeddings

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(task_routes)

    llm = init_llm()

    embeddings = init_embeddings()
    
    app.config["LLM"] = llm
    app.config["EMBEDDINGS"] = embeddings
    return app