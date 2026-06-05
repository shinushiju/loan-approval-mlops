import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("loan.csv")

X = data[["income", "credit_score"]]
y = data["loan_status"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully")
