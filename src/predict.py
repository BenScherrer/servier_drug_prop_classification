import sys
sys.path.append("..")
import pickle
import numpy as np
from rdkit import DataStructs
import tensorflow as tf

from src.preprocess import smiles_to_numpy, morganFP_to_numpy, one_hot_encoding

def predict(model_folder, X_test, method):
    '''
        Predicts using given model, input and method.
        Args :
            - model_folder : path leading to the model you want to use
            - X_test : the instance you want to predict
            - method : the type of model used
        Returns :
            - res[0] : the binary label predicted
    '''
    if (method == "RandomForest"):
        X_test = smiles_to_numpy(X_test)
        X_test = X_test.reshape(1, -1)
        model = pickle.load(open(model_folder + "/random_forest_model.pkl", 'rb'))
        res = model.predict(X_test)[0]
    elif (method == "LSTM"):
        preprocess_params = pickle.load(open(model_folder + "/preprocess_params.pkl", 'rb'))
        model = tf.keras.models.load_model(model_folder + '/LSTM_model.h5')
        X_test = one_hot_encoding(X_test, preprocess_params["char_to_int"], preprocess_params["char_to_int"].keys(),  preprocess_params["smile_max_length"])
        X_test = np.array([X_test])
        res = model.predict(X_test)[0][0] > 0.5
    elif (method == 'MLP'):
        X_test = smiles_to_numpy(X_test)
        X_test = X_test.reshape(1, -1)
        model = pickle.load(open(model_folder + "/MLP_model.pkl", 'rb'))
        res = model.predict(X_test)[0]
    return res


def predict_numpy(model_folder, X_test, method):
    '''
        Predict from different inputs than a smile string. Numpy arrays or MorganFingerprint objects (from rdkit) are handled.
        Args :
            - model_folder : path leading to the model you want to use
            - X_test : the instance you want to predict
            - method : the type of model used
        Returns :
            - res[0] : the binary label predicted
    '''
    if(type(X_test).__module__ == np.__name__):
        pass
    elif(type(X_test).__module__ == DataStructs.cDataStructs.__name__):
        X_test = morganFP_to_numpy(X_test)
    elif(isinstance(X_test, str)):
        X_test = smiles_to_numpy(X_test)
    else:
        print("Input not recognized, please use smile string, RDKit MorganFingerprint or Numpy array")
    X_test = X_test.reshape(1, -1)