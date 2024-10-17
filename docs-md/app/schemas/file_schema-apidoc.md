# File Documentation: `file_schema.py`

This file defines Pydantic models used for validating and handling data related to file metadata and messaging within a FastAPI microservice architecture. The file is structured to ensure that the data adheres to certain constraints and validations, particularly focusing on files that are video types and handling messaging queues.

## Imports

```python
from typing import Optional
from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import field_validator
```

- **typing.Optional**: Allows a type hint to specify that a variable can be of a certain type or `None`.
- **pydantic.BaseModel**: Base class for creating data models. Automatically handles data validation and parsing.
- **pydantic.constr**: A type for constraining strings with specific rules, such as minimum length.
- **pydantic.EmailStr**: A type that ensures a string is a valid email address.
- **pydantic.field_validator**: A decorator for adding custom validation logic to fields.

## Classes

### `FileMetadata`

```python
class FileMetadata(BaseModel):
    file_name: constr(min_length=1)  # type: ignore
    content_type: Optional[str]
```

- **Description**: This model represents the metadata associated with a file. It ensures that the file has a valid name and optionally specifies the content type.
- **Attributes**:
  - `file_name`: A constrained string with a minimum length of 1 character. This ensures that the file name cannot be empty.
  - `content_type`: An optional string that represents the MIME type of the file. This is used to determine the type of content in the file.

#### Method: `check_content_type`

```python
@field_validator("content_type")
def check_content_type(cls, extension):
    allowed_video_types = [
        "video/mp4",
        "video/x-matroska",  # .mkv
        "video/avi",
        "video/webm",
        "video/ogg",
    ]
    if extension not in allowed_video_types:
        raise ValueError("File Type not allowed, please send a video file")
    return extension
```

- **Purpose**: Validates the `content_type` field to ensure it is one of the allowed video types.
- **Parameters**:
  - `cls`: The class reference.
  - `extension`: The value of the `content_type` field being validated.
- **Logic**:
  - A list `allowed_video_types` is defined, containing the MIME types of acceptable video formats.
  - If the `extension` is not in the `allowed_video_types` list, a `ValueError` is raised, indicating that the file type is not allowed.
  - If valid, the `extension` is returned as is.

### `QueueMessage`

```python
class QueueMessage(FileMetadata):
    client_email: EmailStr
    download_link: Optional[str]
```

- **Description**: This model extends `FileMetadata` to represent a message that might be queued in a messaging system. It includes additional fields specific to client communication and download capabilities.
- **Attributes**:
  - `client_email`: An email field that must be a valid email address, representing the client's contact information.
  - `download_link`: An optional string that may contain a URL to download the file.

## Summary

The `file_schema.py` file is a critical component in a microservices architecture using FastAPI, providing structured and validated data models for handling file metadata and messaging. The use of Pydantic ensures robust data validation and parsing, while custom field validators enforce specific business rules, such as restricting file uploads to certain video formats. This facilitates safe and reliable data handling across the services interacting with these models.