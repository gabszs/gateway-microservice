import pytest
from uuid import uuid4
from uuid import UUID
from datetime import datetime
from pydantic import ValidationError
from app.schemas.base_schema import Message, NoContent, ModelBaseInfo, FindDateRange, Blank


def test_message_valid():
    data = {"detail": "This is a test message"}
    message = Message(**data)
    assert message.detail == "This is a test message"


def test_message_missing_detail():
    with pytest.raises(ValidationError):
        Message()


def test_no_content_valid():
    no_content = NoContent()
    assert no_content.model_dump() == {}


def test_model_base_info_valid():
    data = {
        "id": uuid4(),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    model_info = ModelBaseInfo(**data)
    assert isinstance(model_info.id, UUID)
    assert isinstance(model_info.created_at, datetime)
    assert isinstance(model_info.updated_at, datetime)


def test_model_base_info_missing_fields():
    with pytest.raises(ValidationError):
        ModelBaseInfo()


def test_find_date_range_valid():
    data = {
        "created_at__lt": "2024-01-01T00:00:00",
        "created_at__lte": "2024-01-01T00:00:00",
        "created_at__gt": "2023-01-01T00:00:00",
        "created_at__gte": "2023-01-01T00:00:00",
    }
    date_range = FindDateRange(**data)
    assert date_range.created_at__lt == "2024-01-01T00:00:00"
    assert date_range.created_at__lte == "2024-01-01T00:00:00"
    assert date_range.created_at__gt == "2023-01-01T00:00:00"
    assert date_range.created_at__gte == "2023-01-01T00:00:00"


def test_find_date_range_missing_fields():
    with pytest.raises(ValidationError):
        FindDateRange()


def test_blank_valid():
    blank = Blank()
    assert blank.model_dump() == {}
