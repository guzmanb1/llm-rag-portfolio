from flask import Flask
from .config import config
from .routes import task_routes
from .services.llm_client import init_llm

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(task_routes)

    init_llm()
    return app