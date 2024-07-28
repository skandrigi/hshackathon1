from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import model
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD'] = './uploads'
 
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")
 
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def upload_file():
    result = ""
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join('./uploads', secure_filename(file.filename))) # Then save the file
        # results holds whether it is curly hair or straight hair
        result = model.learn.predict('uploads/' + file.filename)[0]
        if result == 'curly hair':
            return render_template('curly.html', result=result)
        elif result == 'straight hair':
            return render_template('straight.html', result=result)
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8001)

