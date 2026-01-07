from flask import Blueprint, request, jsonify, current_app,render_template
from .services.rag_pipeline import process_file, answer_question
from werkzeug.utils import secure_filename
import os

rag_routes = Blueprint('rag_routes',__name__)

def allowed_file(filename, allowed_extensions):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )


@rag_routes.route('/api/upload', methods=['POST'])
def handle_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename, current_app.config["ALLOWED_EXTENSIONS"]):
        return jsonify({"error": "Invalid file type"}), 400

    filename = secure_filename(file.filename)

    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    try:
        process_file(file_path)
    except Exception as e:
        return jsonify({"error": "Failed to process document"}), 500

    return jsonify({"message": "File uploaded successfully"})

@rag_routes.route('/')
def main():
    return render_template('index.html')

@rag_routes.route('/api/chat', methods=['POST'])
def ask_question():
    question = request.json['question']

    try:
        answer = answer_question(question)
    except RuntimeError as e:
        return jsonify({"error": "Failed to generate answer"}), 500


    return jsonify({"answer" : answer}), 200