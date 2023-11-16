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
    try:
        with open('./data/models.json', 'r') as file:
            models = json.load(file)
    except:
        models = {}
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

@app.route('/train')
def train_page():
    with open('./utils/model_options.json', 'r') as file:
        methods = json.load(file)
    file_list = os.listdir('./data')
    print(file_list)
    return render_template('train.html', methods=methods, data_path=file_list)

# TODO : Add loading screen or something that indicates that code is running, maybe include logs ?
@app.route('/trigger_train', methods=['POST'])
def api_train():
    data_path = './data/' + request.form['data_path']
    method = request.form['method']
    print(data_path)
    print(method)
    train(data_path, method)
    return render_template('training_loading.html', method=method, data_path=data_path)


# TODO : add a predict_page to view model info and predict using this model.
@app.route('/predict', methods=['GET'])
def api_predict():
    instance = request.args.get('instance')
    model_folder = request.args.get('model_path')
    method = request.args.get('method')
    res = predict(model_folder, instance, method)
    return f'Predict is {res}'

# TODO : let's start with a simple confusion matrix
@app.route('/evaluate')
def api_evaluate():
    return 'Model evaluated'


if __name__ == '__main__':
    app.run()