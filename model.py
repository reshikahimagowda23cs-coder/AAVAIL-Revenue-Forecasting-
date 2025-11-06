# model.py
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Example training data (months vs revenue)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([1000, 1500, 2000, 2500, 3000, 3500])

# Train simple model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("✅ Model trained and saved as model.pkl")
