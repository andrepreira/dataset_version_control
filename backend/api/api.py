from crypt import methods
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "Welcome to our Machine Learning REST API"

if __name__ == '__main__':
    app.run(port=9090, debug=True)