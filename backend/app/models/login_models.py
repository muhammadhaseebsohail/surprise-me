The request and response models have already been provided in the problem statement above. Here they are again for clarity:

**Pydantic Models:**

```python
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserLogin(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str
```

In the above code, `UserBase` is a base model with a single field `username`. `UserLogin` extends `UserBase` and adds a `password` field that is used for login request data validation. `UserInDB` is the response model which extends `UserBase` and adds a `hashed_password` field.

If you want to hide the `hashed_password` in response, you can create another Pydantic model for it, like:

```python
class UserOut(BaseModel):
    username: str
```

And use it in the `/login` endpoint like this:

```python
@app.post("/login", response_model=schema.UserOut)
```

In this case, even if your endpoint returns the user object with the hashed password, only the fields defined in the response model (i.e., `username`) will be included in the response payload.