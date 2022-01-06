import os
from flask import Flask, request, redirect, render_template
from datetime import date

navbar = os.listdir('/home/bjrnktip/mywebapp/templates')

app = Flask(__name__)

def alder(fdag):
    idag = date.today()
    alder = idag.year - fdag.year - ((idag.month, idag.day) < (fdag.month, fdag.day))
    return alder

@app.route("/")
def index():
    return render_template("index.html", navbar=navbar, alder = alder(date(1990,7,31)))

@app.route("/om")
def om():
    return render_template("om.html", navbar=navbar)