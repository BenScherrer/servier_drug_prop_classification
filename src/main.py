# Public modules
from flask import Flask, request, json, render_template
import os
import sys

# Entry point
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

# Private modules
from scripts.train import train
from scripts.evaluate import predict
from scripts.evaluate import evaluate

app = Flask(__name__)


def load_models():
    with open('./data/models.json', 'r') as file:
        models = json.load(file)
    return models

@app.route('/')
def index():
    models = load_models()
    return render_template('index.html', models=models)

@app.route('/model_info', methods=['POST'])
def model_page():
    models = load_models()
    if request.method == 'POST':
        selected_model_name = request.form['model_id']
        selected_model = next((model for model in models if model['id'] == selected_model_name), None)
        if selected_model:
            return render_template('model_page.html', model=selected_model)
        else:
            return "Model not found"

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