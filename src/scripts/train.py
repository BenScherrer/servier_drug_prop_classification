# Global packages
import pickle
import os
import randomname
import sys
sys.path.append("..")

# ML packages
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

# Private packages
from scripts.preprocess import preprocessing_feature, preprocessing_smiles


def train(data_path, method):
    if method == "RandomForest":
        print("------- Fetching data -------")
        X_train, X_test, y_train, y_test = preprocessing_feature(data_path)
        print("------- Creating model folder -------")
        folder_name = os.path.join("./models/", "model_" + str(randomname.generate('a/emotions')) + "_" + method)
        save_model(folder_name, X_train, X_test, y_train, y_test)
        print(f"------- Training model using {method} -------")
        clf = RandomForestClassifier(max_depth=1000, random_state=0)
        clf.fit(X_train, y_train)
        with open(os.path.join(folder_name, 'random_forest_model.pkl'),'wb') as f:
            pickle.dump(clf,f)
        print(f"------- Model saved in {folder_name}/random_forest_model.pkl -------")
    elif method == "LSTM":
        print("------- Fetching data -------")
        X_train, X_test, y_train, y_test, preprocess_params = preprocessing_smiles(data_path)
        print("------- Creating model folder -------")
        folder_name = os.path.join("./models/", "model_" + str(randomname.generate('a/emotions')) + "_" + method)
        save_model(folder_name, X_train, X_test, y_train, y_test)
        print(f"------- Training model using {method} -------")
        model = Sequential()
        model.add(LSTM(units=100, input_shape=(74,29), return_sequences=False))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X_train, y_train, epochs=3, batch_size=64)
        model.save(os.path.join(folder_name, 'LSTM_model.h5'))
        with open(os.path.join(folder_name, 'preprocess_params.pkl'), 'wb') as file:
            pickle.dump(preprocess_params, file)
        print(f"------- Model saved in {folder_name}/LSTM_model.h5 -------")
    elif method == "MLP":
        print("------- Fetching data -------")
        X_train, X_test, y_train, y_test = preprocessing_feature(data_path)
        print("------- Creating model folder -------")
        folder_name = os.path.join("./models/", "model_" + str(randomname.generate('a/emotions')) + "_" + method)
        save_model(folder_name, X_train, X_test, y_train, y_test)
        print(f"------- Training model using {method} -------")
        clf = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
        with open(os.path.join(folder_name, 'MLP_model.pkl'),'wb') as f:
            pickle.dump(clf,f)
        print(f"------- Model saved in {folder_name}/MLP_model.pkl -------")

def save_model(folder_name, X_train, X_test, y_train, y_test):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Model folder created at {folder_name}")
        print("------- Backing up training and testing data -------")
        with open(os.path.join(folder_name, 'X_train.pkl'), 'wb') as file:
            pickle.dump(X_train, file)
        with open(os.path.join(folder_name, 'X_test.pkl'), 'wb') as file:
            pickle.dump(X_test, file)
        with open(os.path.join(folder_name, 'y_train.pkl'), 'wb') as file:
            pickle.dump(y_train, file)
        with open(os.path.join(folder_name, 'y_test.pkl'), 'wb') as file:
            pickle.dump(y_test, file)