# test_app.py
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert b"API is Running" in response.data
