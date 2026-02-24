""""
Simple training python script
- loads iris dataset from sklearn
- trains a Logistic Regression classifier on iris dataset
- saves model to model.pkl
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import json
import os

def main():
    iris = load_iris()
    x, y = iris.data, iris.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(x_train, y_train)

    # Save model
    os.makedirs("artifacts", exist_ok=True)
    model_path = os.path.join("artifacts", "model.pkl")
    joblib.dump(model, model_path)

    # Save a tiny metrics file
    accuracy = model.score(x_test, y_test)
    metrics = {"accuracy": float(accuracy)}

    with open(os.path.join("artifacts", "metrics.json"), "w") as f:
        json.dump(metrics, f)

    print(f"Saved model to {model_path}")
    print(f"Test accuracy is {accuracy}")

if __name__ == "__main__":
    main()