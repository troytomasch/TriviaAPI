import json
from flask import Flask, jsonify, request, redirect
from data import questions

app = Flask(__name__)


@app.route('/random', methods=['GET'])
def random():
    return jsonify(questions[1]), 200


@app.route('/', methods=['GET'])
def home():
    return redirect("/daily")


@app.route('/daily', methods=['GET'])
def daily():
    return questions[0], 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
