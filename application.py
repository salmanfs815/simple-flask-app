from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello, World!"

@application.route("/send", methods=["POST"])
def send():
    return "Success. Message: " + request.form['message']
