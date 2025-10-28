import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "api_version" in data
    assert "model_version" in data

def test_predict_endpoint():
    # Test with valid data
    test_data = {
        "inputs": [{
            "PassengerId": 79,
            "Pclass": 2,
            "Name": "Caldwell, Master. Alden Gates",
            "Sex": "male",
            "Age": 0.83,
            "SibSp": 0,
            "Parch": 2,
            "Ticket": "248738",
            "Cabin": "A5",
            "Embarked": "S",
            "Fare": 29,
        }]
    }
    response = client.post("/api/v1/predict", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert "version" in data
    assert "errors" in data
    assert data["errors"] is None

def test_predict_endpoint_invalid_data():
    # Test with invalid data
    test_data = {
        "inputs": [{
            "PassengerId": "invalid",
            "Pclass": "invalid",
            "Name": 123,  # invalid type
            "Sex": "invalid",
            "Age": "invalid",
            "SibSp": "invalid",
            "Parch": "invalid",
            "Ticket": 123,  # invalid type
            "Cabin": 123,  # invalid type
            "Embarked": "X",  # invalid value
            "Fare": "invalid",
        }]
    }
    response = client.post("/api/v1/predict", json=test_data)
    assert response.status_code == 400  # Bad request