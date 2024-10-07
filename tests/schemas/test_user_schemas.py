import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError
from app.schemas.user_schema import BaseUser, User
from app.core.enums import UserRoles


def test_base_user_valid():
    data = {
        "email": "test@example.com",
        "username": "testuser"
    }
    base_user = BaseUser(**data)
    assert base_user.email == "test@example.com"
    assert base_user.username == "testuser"


def test_base_user_invalid_email():
    data = {
        "email": "invalid-email",
        "username": "testuser"
    }
    with pytest.raises(ValidationError):
        BaseUser(**data)


def test_user_valid():
    data = {
        "email": "test@example.com",
        "username": "testuser",
        "id": uuid4(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_active": True,
        "role": UserRoles.ADMIN
    }
    user = User(**data)
    assert user.email == "test@example.com"
    assert user.username == "testuser"
    assert user.is_active is True
    assert user.role == UserRoles.ADMIN


def test_user_invalid_role():
    data = {
        "email": "test@example.com",
        "username": "testuser",
        "id": uuid4(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_active": True,
        "role": "invalid_role"
    }
    with pytest.raises(ValidationError):
        User(**data)
