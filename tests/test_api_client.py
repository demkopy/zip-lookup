import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api_client import fetch_location_data

def test_fetch_by_zip_code(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "post code": "90210",
        "places": [{"place name": "Beverly Hills", "state abbreviation": "CA"}]
    }
    mocker.patch('requests.get', return_value=mock_response)
    result = fetch_location_data({'zip_code': '90210'})
    assert result == "Beverly Hills, CA 90210" # <-- Змінено тут

def test_fetch_by_city_state(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "place name": "Houston",
        "state abbreviation": "TX",
        "places": [{"post code": "77052"}] 
    }
    mocker.patch('requests.get', return_value=mock_response)
    result = fetch_location_data({'city': 'Houston', 'state': 'TX'})
    assert result == "Houston, TX 77052" # <-- Змінено тут

def test_fetch_location_not_found(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)
    result = fetch_location_data({'zip_code': '99999'})
    assert result is None