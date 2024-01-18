import sys
sys.path.append("..")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from rdkit.Chem import DataStructs

from utils.feature_extractor import fingerprint_features

def preprocessing_smiles(data_path):
    '''
    Performs a custom One Hot Encoding on an input csv data and split it into training and testing datasets.
    Args :
        - data_path : path leading to the data you want to preprocess and split
    Returns :
        - X_train, X_test, y_train, y_test : the training and testing splitted data with its labels
        - preprocess_params : includes char_to_int (dictionnary used for One Hot Encoding) and 
        smile_max_length (the length of the longest smile in the training dataset)
    TODO : add parameters for test size
    '''
    data = pd.read_csv(data_path)
    all_smiles = ''
    # creating a dictionnary of existing character in the dataset smiles
    for idx, smile in enumerate(data["smiles"]):
        all_smiles = all_smiles + smile
    # getting unique chars
    strs = list(all_smiles)
    concatenated = ''.join(strs)
    unique_chars = ''.join(sorted(set(concatenated), key=concatenated.index))
    # for each unique char, give an int value for encoding
    char_to_int = dict((c, i + 1) for i, c in enumerate(unique_chars))
    data["smile_len"] = data["smiles"].apply(len)
    smile_max_length = max(data["smile_len"])
    data["encoded"] = data["smiles"].apply(lambda x : one_hot_encoding(x, char_to_int, unique_chars, smile_max_length))
    X = np.stack(data["encoded"], axis=0)
    y = np.stack(data["P1"], axis=0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    preprocess_params = {
        "char_to_int" : char_to_int,
        "smile_max_length" : smile_max_length 
    }
    return X_train, X_test, y_train, y_test, preprocess_params


def preprocessing_feature(data_path):
    '''
        Transform the string smiles of a csv dataset into a numpy array and split the dataset into training and testing datasets.
    Args :
        - data_path : path leading to the data you want to preprocess and split
    Returns :
        - X_train, X_test, y_train, y_test : the training and testing splitted data with its labels
    TODO : add parameters for test size
    '''
    data = pd.read_csv(data_path)
    # Since fingerprint_features transform a smile into an array of 2048 items
    X = np.empty((0,2048))
    y = data["P1"].to_numpy() # retrieve data labels
    for _, row in data.iterrows():
        np_arr = smiles_to_numpy(row["smiles"])
        X = np.concatenate((X, np_arr.reshape(1,2048)), axis = 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def smiles_to_numpy(smile):
    morganFP = fingerprint_features(smile)
    np_arr = np.zeros((0,), dtype=int)
    DataStructs.ConvertToNumpyArray(morganFP, np_arr)
    return np_arr

def morganFP_to_numpy(morganFP):
    np_arr = np.zeros((0,), dtype=int)
    DataStructs.ConvertToNumpyArray(morganFP, np_arr)
    return np_arr

# one hot encoding
def one_hot_encoding(smile, char_to_int, unique_chars, smile_max_length):
    onehot_encoded = list()
    # encoding the smile using the char_to_int dict
    integer_encoded = [char_to_int[char] for char in smile]
    # Adding padding for every smile length to match
    current_length = len(integer_encoded)
    if current_length < 74:
        zeros_to_add = 74 - current_length
        integer_encoded.extend([0] * zeros_to_add)
    # one hot encoding
    for value in integer_encoded:
        letter = [0 for _ in range(len(unique_chars))]
        if value != 0:
            letter[value - 1] = 1
        onehot_encoded.append(letter)
    return np.array(onehot_encoded)