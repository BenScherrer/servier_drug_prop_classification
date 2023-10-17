import rdkit
from feature_extractor import fingerprint_features


def train(data, hp, method):

    # Let's train the model, maybe include several methods for comparison

    return 0

def evaluate(model, data, gt):
    
    # generate a prediction
    res = predict(model, data)

    # Confusion Matrix

    # ROC AOC

    # Heat map

    # F1-score

    # Maybe write all that in a folder ...

    return 0

def predict(model, data):
    return 0