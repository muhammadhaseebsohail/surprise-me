Based on the given API endpoint code, below are the additional Pydantic models for request and response, and data transfer objects:

1. Pydantic Models for Request/Response:
```python
from pydantic import BaseModel

# Request Model
class TokenRequest(BaseModel):
    username: str
    password: str

# Response Model
class Token(BaseModel):
    access_token: str
    token_type: str
```

2. Data Transfer Objects:
```python
from pydantic import BaseModel

# Data Transfer Object for User
class UserDTO(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True

# Data Transfer Object for Token
class TokenDTO(BaseModel):
    access_token: str
    token_type: str
```

These models define the structure of the data that will be used for the request and response of the API endpoint. Pydantic models also provide data validation, serialization, and documentation (JSON Schema) for FastAPI.