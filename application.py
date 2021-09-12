from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/send", methods=["POST"])
def send():
    return "Success. Message: " + request.form['message']
