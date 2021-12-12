from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World, this code was updated locally and pushed to Azure Devops repo!"

