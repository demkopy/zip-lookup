import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.text_parser import parse_location_text

@pytest.mark.parametrize("input_text, expected", [
    # Базові тести
    ("  77077  ", {"city": None, "state": None, "zip_code": "77077"}),
    ("Houston, TX", {"city": "Houston", "state": "TX", "zip_code": None}),
    ("Houston Texas", {"city": "Houston", "state": "TX", "zip_code": None}),
    ("Houston TX 77077", {"city": "Houston", "state": "TX", "zip_code": "77077"}),
    ("TX 77077", {"city": None, "state": "TX", "zip_code": "77077"}),
    ("77077 Houston", {"city": "Houston", "state": None, "zip_code": "77077"}),
    ("Texas Houston", {"city": "Houston", "state": "TX", "zip_code": None}),
    ("Houston 77077", {"city": "Houston", "state": None, "zip_code": "77077"}),
    ("77077 TX", {"city": None, "state": "TX", "zip_code": "77077"}),
    ("New York, NY", {"city": "New York", "state": "NY", "zip_code": None}),
    
    # Тести з різними розділовими знаками
    ("Houston,TX", {"city": "Houston", "state": "TX", "zip_code": None}),
    ("TX, 77077", {"city": None, "state": "TX", "zip_code": "77077"}),
    ("Houston, 77077", {"city": "Houston", "state": None, "zip_code": "77077"}),
    ("Houston, Texas, 77077", {"city": "Houston", "state": "TX", "zip_code": "77077"}),
    ("77077, Houston", {"city": "Houston", "state": None, "zip_code": "77077"}),
    ("TX, Houston", {"city": "Houston", "state": "TX", "zip_code": None}),
    ("Houston, 77077 TX", {"city": "Houston", "state": "TX", "zip_code": "77077"}), # <-- ВАШ НОВИЙ ТЕСТ

    # Негативні тести
    ("some random text", None),
    ("1234", None)
])
def test_parse_various_formats(input_text, expected):
    assert parse_location_text(input_text) == expected