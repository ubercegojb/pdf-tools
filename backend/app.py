from flask import Flask, request, send_file
import os
from utils.pdf_utils import convert_pdf_to_word, merge_pdfs, compress_pdf, protect_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/convert-to-word', methods=['POST'])
def convert_to_word():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    output_path = convert_pdf_to_word(filepath)
    return send_file(output_path, as_attachment=True)

@app.route('/merge-pdfs', methods=['POST'])
def merge_pdfs_route():
    files = request.files.getlist('files')
    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    filepaths = []
    for file in files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        filepaths.append(filepath)

    output_path = merge_pdfs(filepaths)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)