from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/render", methods=["GET"])
def render():
    return render_template("render.html")

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=80)