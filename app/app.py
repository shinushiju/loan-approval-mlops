from flask import Flask
from flask import request
from flask import jsonify

import pandas as pd
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "ml",
    "model.pkl"
)

model = joblib.load(MODEL_PATH)

@app.route("/")
def health():
    return "Loan Approval API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON payload required"}), 400

    if "income" not in data:
        return jsonify({"error": "income missing"}), 400

    if "credit_score" not in data:
        return jsonify({"error": "credit_score missing"}), 400

    input_df = pd.DataFrame({
        "income": [data["income"]],
        "credit_score": [data["credit_score"]]
    })

    prediction = model.predict(input_df)

    return jsonify({
        "loan_approved": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
