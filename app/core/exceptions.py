from typing import Any
from typing import Dict
from typing import Optional

from fastapi import HTTPException
from fastapi import status


class BadRequestError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class AuthError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)


class NotFoundError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)


class ValidationError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_422_UNPROCESSABLE_ENTITY, detail, headers)


class DuplicatedError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_409_CONFLICT, detail, headers)


class InvalidCredentials(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)


class ObjectStorageError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_500_INTERNAL_SERVER_ERROR, detail, headers)


class ObjectNotFoundError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail or "Object not found in storage.", headers)


class ObjectAlreadyExistsError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_409_CONFLICT, detail or "Object already exists in storage.", headers)


class ObjectUploadError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(
            status.HTTP_500_INTERNAL_SERVER_ERROR, detail or "Failed to upload object to storage.", headers
        )


class ObjectDownloadError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(
            status.HTTP_500_INTERNAL_SERVER_ERROR, detail or "Failed to download object from storage.", headers
        )
