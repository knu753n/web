import os
from flask import Flask, request, redirect, render_template

navbar = os.listdir('/home/bjrnktip/mywebapp/templates')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", navbar=navbar)

@app.route("/om")
def om():
    return render_template("om.html", navbar=navbar)