from flask import Flask, request, jsonify
from pathlib import Path
import joblib


app = Flask(__name__)
MODEL_PATH = Path("artifacts/model.pkl")

if not MODEL_PATH.exists():
    # convenience: train if model is missing
    import train as _train
    _train.main()

# joblib is being used to deserialize (load) a previously serialized (saved) machine learning model from disk (artifacts/model.pkl)
model = joblib.load(MODEL_PATH)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "send JSON with key 'features'"}), 400
    features = data["features"]
    try:
        prediction = model.predict([features])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
