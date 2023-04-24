from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import secure_filename, redirect, send_from_directory

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads/"
app.config["SECRET_KEY"] = "This is not a secret"


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods=['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return render_template('content.html', message='No selected file')

        filename = secure_filename(file.filename)
        file.save(app.config['UPLOAD_FOLDER'] + filename)

        # You can do this for text files -
        # file = open(app.config['UPLOAD_FOLDER'] + filename, "r")
        # content = file.read()

        return render_template('content.html', filename=filename)

    # return render_template('content.html', message="ERROR")
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
