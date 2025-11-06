# app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "AAVAIL Revenue Forecasting API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    month = data.get("month", 1)
    prediction = model.predict(np.array([[month]]))[0]
    return jsonify({"predicted_revenue": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
