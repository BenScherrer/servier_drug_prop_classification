import pandas as pd
import numpy as np
from src.utils.feature_extractor import fingerprint_features
from sklearn.model_selection import train_test_split
from rdkit.Chem import DataStructs

def preprocessing():
    data = pd.read_csv('../data/dataset_single.csv')
    # Since fingerprint_features transform a smile into an array of 2048 items
    X = np.empty((0,2048))
    y = data["P1"].to_numpy() # retrieve data labels
    for index, row in data.iterrows():
        fp = np.zeros((0,), dtype=int)
        feature_vector = fingerprint_features(row["smiles"])
        DataStructs.ConvertToNumpyArray(feature_vector, fp)
        X = np.concatenate((X, fp.reshape(1,2048)), axis = 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test