import pickle
import numpy as np

def load_models():
    with open("models/model_vec.pkl", "rb") as f:
        vec = pickle.load(f)
    
    with open("models/model_X.pkl", "rb") as f:
        X = pickle.load(f)

    return vec,X

def index_finder(query, vector, X):
    Q = vector.transform([query])
    Q = Q.toarray()

    R = X @ Q.T
    R = R.flatten()
    R = R[R>0.1]
    Rx = np.argsort(R)[::-1]

    return Rx[:10], R[Rx[:10]]
