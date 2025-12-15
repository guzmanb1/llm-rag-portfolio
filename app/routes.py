from flask import Blueprint, render_template

task_routes = Blueprint('task_routes',__name__)


@task_routes.route('/upload', methods=['POST'])
def handle_file():
    file_data = ""
    return file_data

@task_routes.route('/')
def main():
    return render_template('index.html')