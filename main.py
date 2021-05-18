"""
This is a Flask website template for a web tool or whatever
"""
import logging
import configparser
from waitress import serve
from flask import Flask, render_template, url_for,redirect,request
from routes import render_home, render_faq
from os.path import join

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_home(session="testing_session", request=request)
    else:
        return render_home(session="testing_session")

@app.route('/faq', methods=['GET'])
def faq():
    if request.method == 'POST':
        return render_faq(session="testing_session", request=request)
    else:
        return render_faq(session="testing_session")

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
