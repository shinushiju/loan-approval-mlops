import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.app import app

def test_health():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

def test_prediction():

    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "income": 70000,
            "credit_score": 750
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "loan_approved" in data
