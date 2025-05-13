Here is the complete FastAPI backend code for user authentication during login:

**Database Model:**

```python
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from passlib.context import CryptContext

Base = declarative_base()

# Password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)
```

**Service Layer:**

```python
from sqlalchemy.orm import Session
from . import models

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
```

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

**API Endpoints:**

```python
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schema, services
from passlib.context import CryptContext

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login", response_model=schema.UserInDB)
def login(user: schema.UserLogin, db: Session = Depends(get_db)):
    """Login endpoint that validates user credentials"""
    db_user = services.get_user(db, username=user.username)
    if db_user is None or not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return db_user
```

**Unit Test:**

```python
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_login():
    response = client.post(
        "/login",
        json={"username": "test", "password": "test"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "test"
```

In this solution, FastAPI is used to create an API endpoint for user login. SQLAlchemy is used to interact with the database and Pydantic for data validation. CryptContext from passlib is used for password hashing and verification. Error handling is done using FastAPI's `HTTPException`. A unit test is also created to ensure the correctness of the login endpoint.