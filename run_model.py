#!/usr/bin/env python3

""""
Usage:
    python run_model.py --input "[5.1, 3.5, 1.4, 0.2]"
"""
from sklearn.datasets import load_iris
from pathlib import Path
import argparse
import joblib
import json
import numpy as np

MODEL_PATH = Path("artifacts/model.pkl")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        required=True,
                        help="Feature list as JSON string. Example: \"[5.1,3.5,1.4,0.2]\"")

    args = parser.parse_args()

    # Parse input
    try:
        feature_list = json.loads(args.input)
    except json.JSONDecodeError:
        raise ValueError("Invalid input. Use JSON string. Example \"[5.1, 3.5, 1.4, 0.2]\"")

    X = np.array(feature_list).reshape(1, -1)

    model = load_model()
    prediction = model.predict(X)

    iris = load_iris()
    species_name = iris.target_names[prediction[0]]
    print(json.dumps({"prediction": species_name}))

if __name__ == "__main__":
    main()