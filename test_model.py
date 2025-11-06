# test_model.py
import pickle
import numpy as np

def test_model_loads():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    assert model.predict(np.array([[1]])).shape == (1,)
