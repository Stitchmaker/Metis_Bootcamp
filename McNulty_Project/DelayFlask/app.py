from flask import Flask, render_template, jsonify, request
from api import make_prediction

app = Flask('SeatacOntime')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def do_prediction():
    if not request.json:
        abort(400)
    data = request.json

    response = make_prediction(data)

    return jsonify(response)

app.run()