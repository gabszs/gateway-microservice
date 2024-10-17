Below is the detailed documentation for the provided `exceptions.py` file, which is part of a FastAPI-based project. This file defines custom exception classes that extend FastAPI's `HTTPException`. These custom exceptions are designed to provide more specific error handling within a microservices architecture, specifically for a gateway service:

### Imports

- `from typing import Any, Dict, Optional`: These imports bring in type hints from Python's typing module. `Any` allows for any data type, `Dict` specifies a dictionary with key-value pairs, and `Optional` indicates that a value can be of a specified type or `None`.
  
- `from fastapi import HTTPException, status`: These are FastAPI imports. `HTTPException` is a generic exception class for HTTP errors, and `status` provides constants representing standard HTTP status codes.

### Custom Exception Classes

Each custom exception class inherits from `HTTPException` and is designed to encapsulate specific error scenarios, using appropriate HTTP status codes.

1. **`BadRequestError`**

   - **Purpose**: Represents a generic HTTP 400 Bad Request error.
   - **Constructor Parameters**:
     - `detail`: Additional information about the error (of any type).
     - `headers`: Optional dictionary of HTTP headers to include in the response.
   - **Usage**: Raised when there is a client-side error in the request.

2. **`AuthError`**

   - **Purpose**: Represents an HTTP 403 Forbidden error.
   - **Constructor Parameters**:
     - `detail`: Details about the authentication error.
     - `headers`: Optional response headers.
   - **Usage**: Used for cases where the user is authenticated but does not have permission to access a resource.

3. **`NotFoundError`**

   - **Purpose**: Represents an HTTP 404 Not Found error.
   - **Constructor Parameters**:
     - `detail`: Information about the missing resource.
     - `headers`: Optional response headers.
   - **Usage**: Raised when a requested resource cannot be found.

4. **`ValidationError`**

   - **Purpose**: Represents an HTTP 422 Unprocessable Entity error.
   - **Constructor Parameters**:
     - `detail`: Details about validation errors.
     - `headers`: Optional response headers.
   - **Usage**: Used when input data fails validation checks.

5. **`DuplicatedError`**

   - **Purpose**: Represents an HTTP 409 Conflict error.
   - **Constructor Parameters**:
     - `detail`: Information about the duplication conflict.
     - `headers`: Optional response headers.
   - **Usage**: Raised when there's a conflict due to a duplicate resource.

6. **`InvalidCredentials`**

   - **Purpose**: Represents an HTTP 401 Unauthorized error.
   - **Constructor Parameters**:
     - `detail`: Contains details about why the credentials are invalid.
     - `headers`: Optional response headers.
   - **Usage**: Used when authentication fails due to invalid credentials.

7. **`ObjectStorageError`**

   - **Purpose**: Represents a generic HTTP 500 Internal Server Error related to object storage operations.
   - **Constructor Parameters**:
     - `detail`: Information about the storage error.
     - `headers`: Optional response headers.
   - **Usage**: Raised during general object storage failures.

8. **`ObjectNotFoundError`**

   - **Purpose**: Represents a specific HTTP 404 Not Found error for object storage.
   - **Constructor Parameters**:
     - `detail`: Details about the missing object (defaults to "Object not found in storage." if not provided).
     - `headers`: Optional response headers.
   - **Usage**: Used when an object is not found in storage.

9. **`ObjectAlreadyExistsError`**

   - **Purpose**: Represents an HTTP 409 Conflict error for object storage.
   - **Constructor Parameters**:
     - `detail`: Details about the existing object (defaults to "Object already exists in storage." if not provided).
     - `headers`: Optional response headers.
   - **Usage**: Raised when an object already exists in storage.

10. **`ObjectUploadError`**

    - **Purpose**: Represents an HTTP 500 Internal Server Error for failures in object upload.
    - **Constructor Parameters**:
      - `detail`: Details about the upload failure (defaults to "Failed to upload object to storage." if not provided).
      - `headers`: Optional response headers.
    - **Usage**: Used when an object upload operation fails.

11. **`ObjectDownloadError`**

    - **Purpose**: Represents an HTTP 500 Internal Server Error for failures in object download.
    - **Constructor Parameters**:
      - `detail`: Details about the download failure (defaults to "Failed to download object from storage." if not provided).
      - `headers`: Optional response headers.
    - **Usage**: Raised when an object download operation fails.

### Summary

This file provides a structured way to handle various HTTP error scenarios in a FastAPI application, particularly within a gateway service context. By defining specific exceptions, it enhances error handling and allows for more descriptive and meaningful responses to clients, improving the overall robustness and maintainability of the API.