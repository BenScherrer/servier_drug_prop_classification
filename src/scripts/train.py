from sklearn.ensemble import RandomForestClassifier
import pickle

def train(X_train, y_train, hp, method):
    # Let's train the model, maybe include several methods for comparison
    if method == "RandomForest":
        clf = RandomForestClassifier(max_depth=1000, random_state=0)
        clf.fit(X_train, y_train)
        with open('random_forest_model.pkl','wb') as f:
            pickle.dump(clf,f)
    return 0