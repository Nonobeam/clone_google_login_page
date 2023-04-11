from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def fptwebsite():
        return render_template("")