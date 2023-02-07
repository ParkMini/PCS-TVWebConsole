from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload1():
    f = request.files['file']
    f.save("./static/" + secure_filename("video.mp4"))
    return "true"

@app.route("/getvid")
def getvid():
    return send_file("video.mp4")

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=80)