import pytest
import requests

BASE_URL = "http://localhost:8000/"

def test_success_case():
    paremeter = {"string": "abcDEF"}
    response = requests.post(BASE_URL, json=paremeter)
    assert response.status_code == 200
    assert response.json() == {"swapped_string": "ABCdef"}

def test_missing_string_parameter():
    paremeter = {} 
    response = requests.post(BASE_URL, json=paremeter)
    assert response.status_code == 400
    assert response.json() == {"error": "Missing 'string' parameter."}

def test_invalid_string_parameter():
    paremeter = {"string": 123}  # Invalid 'string' parameter (not a string)
    response = requests.post(BASE_URL, json=paremeter)
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid 'string' parameter."}

if __name__ == "__main__":
    pytest.main()