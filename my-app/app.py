from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static', 'assets')
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'img-upload' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['img-upload']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return jsonify({'success': True, 'file_path': file_path})
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)