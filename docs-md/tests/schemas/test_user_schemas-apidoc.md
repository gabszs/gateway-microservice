# Detailed Documentation for `test_user_schemas.py`

This file contains a set of unit tests for user schema validation using Pydantic models. It is designed to ensure that the `BaseUser` and `User` schemas function correctly under various conditions. The tests utilize the `pytest` framework to manage test case execution and assertions.

## Imports

- `datetime`: A module from the Python standard library used for handling date and time objects.
- `uuid4`: A function from the `uuid` module that generates a random UUID (Universally Unique Identifier).
- `pytest`: A testing framework for Python that allows for simple syntax for writing tests.
- `ValidationError`: An exception from Pydantic that is raised when validation of input data fails.
- `UserRoles`: An enumeration imported from `app.core.enums` representing possible user roles.
- `BaseUser` and `User`: Pydantic models imported from `app.schemas.user_schema` that define the structure and validation rules for user-related data.

## Test Functions

### `test_base_user_valid`

This test function validates that a `BaseUser` can be successfully created with valid input data.

- **Data**: A dictionary containing a valid email and username.
- **Assertions**: 
  - Checks that the `email` attribute of the created `BaseUser` instance matches the input data.
  - Verifies that the `username` attribute is set correctly.

### `test_base_user_invalid_email`

This test function ensures that the `BaseUser` model raises a `ValidationError` when provided with an invalid email format.

- **Data**: A dictionary with an invalid email format (`"invalid-email"`) and a valid username.
- **Assertions**: 
  - Expects a `ValidationError` to be raised due to the invalid email format.

### `test_user_valid`

This test function verifies that a `User` instance can be successfully created with all required fields filled with valid data.

- **Data**: A dictionary containing:
  - A valid email and username.
  - A unique `id` generated using `uuid4()`.
  - `created_at` and `updated_at` fields set to the current datetime.
  - `is_active` set to `True`.
  - `role` set to `UserRoles.ADMIN`.
- **Assertions**: 
  - Verifies that the `email`, `username`, `is_active`, and `role` attributes match the input data.

### `test_user_invalid_role`

This test function checks that the `User` model raises a `ValidationError` when an invalid user role is provided.

- **Data**: A dictionary similar to `test_user_valid`, but with `role` set to `"invalid_role"`.
- **Assertions**: 
  - Expects a `ValidationError` to be raised due to the invalid role.

## Summary

These tests collectively ensure that:

- The `BaseUser` and `User` schemas correctly validate input data, enforcing constraints such as email format and valid user roles.
- Invalid inputs are appropriately handled by raising exceptions, preventing the creation of malformed user objects.

By utilizing Pydantic's validation capabilities and the `pytest` framework, these tests provide robust coverage for user schema validations in the application.