from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/client')
def client():
    return render_template('client.html')

@app.route('/uploadVid1', methods=['POST'])
def uploadVid1():
        f = request.files['file1']
        f.save(secure_filename('video1.mp4'))
        return render_template('return.html')

@app.route('/uploadVid2', methods=['POST'])
def uploadVid2():
        f = request.files['file2']
        f.save(secure_filename('video2.mp4'))
        return render_template('return.html')


@app.route('/tv1', methods=['GET', 'POST'])
def tv1():
    if request.method == 'POST':
        if request.form.get('tv1') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv1.html")
            return render_template('return.html')
        elif request.form.get('tv1') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv1.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv1.html')

@app.route('/tv2', methods=['GET', 'POST'])
def tv2():
    if request.method == 'POST':
        if request.form.get('tv2') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv2.html")
            return render_template('return.html')
        elif request.form.get('tv2') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv2.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv2.html')

@app.route('/tv3', methods=['GET', 'POST'])
def tv3():
    if request.method == 'POST':
        if request.form.get('tv3') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv3.html")
            return render_template('return.html')
        elif request.form.get('tv3') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv3.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv3.html')

@app.route('/tv4', methods=['GET', 'POST'])
def tv4():
    if request.method == 'POST':
        if request.form.get('tv4') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv4.html")
            return render_template('return.html')
        elif request.form.get('tv4') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv4.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv4.html')

@app.route('/tv5', methods=['GET', 'POST'])
def tv5():
    if request.method == 'POST':
        if request.form.get('tv5') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv5.html")
            return render_template('return.html')
        elif request.form.get('tv5') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv5.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv5.html')

@app.route('/tv6', methods=['GET', 'POST'])
def tv6():
    if request.method == 'POST':
        if request.form.get('tv6') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv6.html")
            return render_template('return.html')
        elif request.form.get('tv6') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv6.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv6.html')

@app.route('/tv7', methods=['GET', 'POST'])
def tv7():
    if request.method == 'POST':
        if request.form.get('tv7') == 'vid1':
            os.system("copy c:\\xampp\\htdocs\\templates\\video1.html c:\\xampp\\htdocs\\templates\\tv7.html")
            return render_template('return.html')
        elif request.form.get('tv7') == 'vid2':
            os.system("copy c:\\xampp\\htdocs\\templates\\video2.html c:\\xampp\\htdocs\\templates\\tv7.html")
            return render_template('return.html')
        else:
            return "POST ERROR, Please Contact Administrator", 500
    else:
        return render_template('tv7.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=80)