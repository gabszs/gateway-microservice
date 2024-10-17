Below is the detailed documentation for the provided Python file using the Pydantic library. This file defines schemas related to user data, particularly for use in a FastAPI application. The schemas are structured using Pydantic's BaseModel, which provides data validation and settings management.

### File Overview

This file is part of a FastAPI application and defines schema models related to user data. It is located at `C:\Users\g50034179\Documents\fastapi\microservices_mpe\gateway\app\schemas/user_schema.py`. The schemas are defined using Pydantic, which allows for easy data validation and parsing.

### Imports

```python
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
```

- **BaseModel**: This is a base class provided by Pydantic, used to define data models with automatic validation and parsing.
- **ConfigDict**: A configuration management tool from Pydantic, enabling custom model configuration.
- **EmailStr**: A specialized type for validating email addresses, extending Pydantic's standard types.

```python
from app.core.enums import UserRoles
from app.schemas.base_schema import ModelBaseInfo
```

- **UserRoles**: An enumeration likely defining the various roles a user can have within the application. This would be imported from the `app.core.enums` module.
- **ModelBaseInfo**: A base class imported from `app.schemas.base_schema`. This might include additional fields or methods that are common across multiple schema models.

### Class Definitions

#### BaseUser

```python
class BaseUser(BaseModel):
    email: EmailStr
    username: str
```

- **Description**: `BaseUser` is a fundamental schema model representing a user with basic details.
- **Attributes**:
  - `email`: A validated email address using `EmailStr`. This ensures that any email provided to a `BaseUser` instance is properly formatted.
  - `username`: A string representing the user's username.

#### User

```python
class User(BaseUser, ModelBaseInfo):
    model_config = ConfigDict(from_attributes=True)

    is_active: bool
    role: UserRoles
```

- **Description**: `User` extends `BaseUser` and `ModelBaseInfo`, adding more specific attributes for a user entity.
- **Attributes**:
  - `is_active`: A boolean indicating whether the user's account is active.
  - `role`: An instance of `UserRoles`, representing the user's role within the application.
  
- **Configuration**:
  - `model_config`: Configured with `ConfigDict(from_attributes=True)`. This option allows the model to be constructed from existing attributes of an object, enhancing flexibility in data handling.

### Key Points

- **Inheritance**: `User` inherits both from `BaseUser` and `ModelBaseInfo`. This indicates that `User` not only builds upon the basic user details but also incorporates additional base information defined in `ModelBaseInfo`.
- **Data Validation**: The use of Pydantic ensures that data is validated automatically, reducing the risk of errors due to invalid data.
- **Extensibility**: By leveraging class inheritance, the schema is easily extendable. New user-related models can inherit from `BaseUser` or `User`, promoting code reuse and maintainability.

This file plays a crucial role in ensuring that user data is correctly structured and validated in the FastAPI application, utilizing Pydantic's powerful features for data integrity and ease of use.