# Flask API
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/train')
def train():
    return 'Training...'

@app.route('/predict')
def predict():
    return 'Predict is...'

@app.route('/evaluate')
def evaluate():
    return 'Model evaluated'


if __name__ == '__main__':
    app.run()