from flask import Flask, render_template, request, url_for, redirect
from flask.helpers import send_file
import cv2 as cv
import os


UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path = ""

@app.route("/", methods=['GET', 'POST'])
def home():
    global path
    if request.method == "POST":
        img = request.files["img"]
        height = int(request.form.get("height"))
        width = int(request.form.get("width"))
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], img.filename))
        path = "static/uploads/"+img.filename
        imread = cv.imread(path)
        imread = cv.resize(imread, (width, height))
        cv.imwrite(path, imread)
        return render_template('index.html', filename = "uploads/"+img.filename)
    return render_template('index.html')
    

# @app.route('/download')
# def download():
#     return send_file(path, as_attachment=True)




if __name__ == '__main__':
    app.run(debug = True)