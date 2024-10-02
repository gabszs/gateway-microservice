import pytest
from pydantic import ValidationError
from app.schemas.file_schema import FileMetadata, QueueMessage


def test_file_metadata_valid():
    data = {
        "file_name": "test_video.mp4",
        "content_type": "video/mp4"
    }
    metadata = FileMetadata(**data)
    assert metadata.file_name == "test_video.mp4"
    assert metadata.content_type == "video/mp4"


def test_file_metadata_invalid_content_type():
    data = {
        "file_name": "test_video.mp4",
        "content_type": "image/jpeg"
    }
    with pytest.raises(ValidationError):
        FileMetadata(**data)


def test_queue_message_valid():
    data = {
        "file_name": "test_video.mp4",
        "content_type": "video/mp4",
        "client_email": "test@example.com",
        "download_link": "http://example.com/download"
    }
    message = QueueMessage(**data)
    assert message.client_email == "test@example.com"
    assert message.download_link == "http://example.com/download"


def test_queue_message_invalid_email():
    data = {
        "file_name": "test_video.mp4",
        "content_type": "video/mp4",
        "client_email": "invalid-email",
        "download_link": "http://example.com/download"
    }
    with pytest.raises(ValidationError):
        QueueMessage(**data)
