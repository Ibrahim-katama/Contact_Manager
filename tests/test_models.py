from src.models import validate_name, validate_number, validate_email

def test_validate_name_valid():
    assert validate_name("Jannet") is True
    assert validate_name("Deon") is True

def test_validate_name_invalid():
    assert validate_name("Deon990") is False
    assert validate_name("Deon_Wangari") is False

def test_validate_name_blank_handling():
    # Middle name allowed to be blank
    assert validate_name("", allow_blank=True) is True
    assert validate_name("", allow_blank=False) is False

def test_validate_number():
    assert validate_number("1234567890") is True
    assert validate_number("123") is False
    assert validate_number("12345678901") is False
    assert validate_number("abcdefghij") is False

def test_validate_email():
    assert validate_email("user@example.com") is True
    assert validate_email("invalid-email") is False
    assert validate_email("user@domain") is False