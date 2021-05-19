"""
This is a Flask website template for a web tool or whatever
"""
import logging
import configparser
from waitress import serve
from flask import Flask, render_template, url_for,redirect,request
from routes import render_home, render_documentation, render_about
from os.path import join

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_home(session="testing_session", request=request)
    else:
        return render_home(session="testing_session")

@app.route('/documentation', methods=['GET'])
def documentation():
    if request.method == 'POST':
        return render_documentation(session="testing_session", request=request)
    else:
        return render_documentation(session="testing_session")

@app.route('/about',methods=['GET'])
def about():
    if request.method == 'POST':
        return render_about(session="testing_session",request=request)
    else:
        return render_about(session="testing_session")

@app.route('/', methods=['GET', 'POST'])
def initial():
    return redirect("/home")


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    general_path = "/home/damian/Documents/L3S/projects/learning_web"
    logging.basicConfig(filename=join(general_path,'genotoscope_website.log'), level=logging.DEBUG)
    app.secret_key = config["APP_INFO"]["secret_key"]
    serve(app, host='127.0.0.1', port=5000)
