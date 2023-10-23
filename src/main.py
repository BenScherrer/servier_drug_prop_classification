# Public modules
from flask import Flask, request
import os
import sys

# Entry point
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

# Private modules
from src.scripts.train import train
from src.scripts.evaluate import predict
from src.scripts.evaluate import evaluate

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/train', methods=['GET'])
def api_train():
    data_path = request.args.get('data_path')
    method = request.args.get('method')
    train(data_path, method)
    return 'Training...'

@app.route('/predict', methods=['GET'])
def api_predict():
    instance = request.args.get('instance')
    model_folder = request.args.get('model_path')
    method = request.args.get('method')
    res = predict(model_folder, instance, method)
    return f'Predict is {res}'

@app.route('/evaluate')
def api_evaluate():
    return 'Model evaluated'


if __name__ == '__main__':
    app.run()