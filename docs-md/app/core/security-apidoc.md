Certainly! Below is detailed documentation for the `security.py` file, which is part of a FastAPI microservices architecture. This file deals with authorization logic and token-based authentication using JWTs.

---

### File Overview

The `security.py` file contains functions and classes that manage authorization and authentication within a FastAPI application. It primarily focuses on verifying user roles and handling JSON Web Tokens (JWT) for secure API access.

### Imports

- **`functools.wraps`**: Used for preserving the metadata of decorated functions.
- **`typing.List`**: Utilized for type hinting, indicating that a function parameter is a list.
- **`aiohttp.ClientSession`**: Provides an asynchronous HTTP client session for making requests.
- **`aiohttp.client_exceptions.ClientConnectionError`**: Exception that's raised when there is a connection error with the client.
- **`fastapi.Request`**: Represents an incoming HTTP request in FastAPI.
- **`fastapi.security.HTTPAuthorizationCredentials`**: Used to handle HTTP Authorization headers.
- **`fastapi.security.HTTPBearer`**: A security scheme for HTTP Bearer token authentication.
- **`app.core.exceptions.AuthError`**: Custom exception for authentication-related errors.
- **`app.core.exceptions.BadRequestError`**: Custom exception for handling bad request errors.
- **`app.core.http_client.get_async_client`**: Function to obtain an asynchronous HTTP client, likely a context manager.
- **`app.core.settings.Settings`**: Configuration class for accessing application settings.
- **`app.schemas.user_schema.User`**: A Pydantic model for representing a user schema.

### Global Variables

- **`settings`**: An instance of the `Settings` class, used to access configuration values such as URLs for external services.

### Functions

#### `authorize(role: List[str], allow_same_id: bool = False)`

This function is a decorator factory that returns a decorator to enforce role-based authorization on endpoints.

- **Parameters:**
  - `role`: A list of strings representing roles that are allowed to access the decorated function.
  - `allow_same_id`: A boolean flag indicating if users can access resources where the user ID matches their own, even if their role is not listed.

- **Logic:**
  - The decorator checks if the current user's role is in the allowed roles.
  - If `allow_same_id` is `True`, the decorator also checks if the current user's ID matches the target `user_id`.
  - Raises `AuthError` if the authorization checks fail.

### Classes

#### `JWTBearer(HTTPBearer)`

This class is a custom implementation of the `HTTPBearer` authentication scheme, tailored for JWT tokens.

- **Constructor (`__init__`)**
  - Initializes the parent `HTTPBearer` class with an `auto_error` flag, which determines if an error should be automatically raised when authentication fails.

- **Asynchronous Call Method (`__call__`)**
  - **Parameters:**
    - `request`: An instance of `Request`, representing the incoming HTTP request.
  - **Returns:**
    - A `UserSchema` object if the token is valid, otherwise raises `AuthError`.
  - **Logic:**
    - Retrieves and validates the authorization credentials from the request.
    - Checks if the credentials use the "Bearer" scheme.
    - Uses an asynchronous client to communicate with an authentication service for token validation.
    - Raises `AuthError` if the token is invalid or if the authentication service returns an error.

- **`get_data_from_token(token: str, client: ClientSession) -> tuple[int, UserSchema]`**
  - **Parameters:**
    - `token`: The JWT token as a string.
    - `client`: An instance of `ClientSession` for making HTTP requests.
  - **Returns:**
    - A tuple containing the HTTP status code and a `UserSchema` object or raises an error.
  - **Logic:**
    - Attaches the token to the request headers and queries the authentication service to retrieve user information.
    - Converts the response to a `UserSchema` object if successful.
    - Handles connection errors by raising a `BadRequestError`.

### Key Logic

- **Role-based Authorization**: The `authorize` decorator ensures that only users with specified roles and, optionally, the same user ID can execute certain functions, enhancing security.
- **JWT Authentication**: The `JWTBearer` class implements bearer token authentication, verifying tokens against an external authentication service and ensuring users have valid credentials.
- **Error Handling**: Custom exceptions (`AuthError`, `BadRequestError`) are used to handle specific error scenarios, providing detailed feedback for debugging and client error responses.

This file effectively encapsulates the security mechanisms needed for a FastAPI application, supporting scalable and secure API interactions in a microservices environment.