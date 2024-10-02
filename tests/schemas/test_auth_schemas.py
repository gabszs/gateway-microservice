import pytest
from pydantic import ValidationError
from app.schemas.auth_schema import SignIn, SignInResponse


def test_sign_in_valid():
    data = {
        "email__eq": "user@example.com",
        "password": "securepassword123"
    }
    sign_in = SignIn(**data)
    assert sign_in.email__eq == "user@example.com"
    assert sign_in.password == "securepassword123"


def test_sign_in_invalid_email():
    data = {
        "email__eq": "invalid-email",
        "password": "securepassword123"
    }
    with pytest.raises(ValidationError):
        SignIn(**data)


def test_sign_in_missing_password():
    data = {
        "email__eq": "user@example.com"
    }
    with pytest.raises(ValidationError):
        SignIn(**data)


def test_sign_in_response_valid():
    data = {
        "access_token": "token_12345",
        "expiration": "2024-12-31T23:59:59"
    }
    sign_in_response = SignInResponse(**data)
    assert sign_in_response.access_token == "token_12345"
    assert sign_in_response.expiration == "2024-12-31T23:59:59"


def test_sign_in_response_missing_token():
    data = {
        "expiration": "2024-12-31T23:59:59"
    }
    with pytest.raises(ValidationError):
        SignInResponse(**data)
