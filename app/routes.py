from flask import Blueprint, render_template, request
from .services.rag_pipeline import process_file, answer_question

task_routes = Blueprint('task_routes',__name__)


@task_routes.route('/upload', methods=['POST'])
def handle_file():
    file_data = ""
    return file_data

@task_routes.route('/')
def main():
    return render_template('index.html')

@task_routes.route('/api/chat', methods=['POST'])
def ask_question():
    question = request.json['question']
    print(question)
    answer = answer_question(question)

    return answer