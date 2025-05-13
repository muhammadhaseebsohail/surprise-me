Sure, let's start by defining our Pydantic models and the database model.

```python
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# SQLAlchemy model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    is_featured = Column(Boolean, default=False)

# Pydantic models
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_featured: bool = False

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
```

Next, let's define our service layer code.

```python
from sqlalchemy.orm import Session
import models

def get_featured_products(db: Session):
    return db.query(models.Product).filter(models.Product.is_featured == True).all()

def search_products(db: Session, keyword: str):
    return db.query(models.Product).filter(models.Product.name.contains(keyword)).all()
```

Then, we can create the FastAPI endpoints:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products/featured", response_model=List[schemas.Product])
def read_featured_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Fetch the featured products from the database
    """
    products = crud.get_featured_products(db=db)
    return products

@app.get("/products/search/{keyword}", response_model=List[schemas.Product])
def search_products(keyword: str, db: Session = Depends(get_db)):
    """
    Search for products by keyword
    """
    products = crud.search_products(db=db, keyword=keyword)
    return products
```

Finally, let's implement some simple unit tests for these endpoints:

```python
from fastapi.testclient import TestClient

def test_read_featured_products():
    response = client.get("/products/featured")
    assert response.status_code == 200
    assert "products" in response.json()

def test_search_products():
    response = client.get("/products/search/test")
    assert response.status_code == 200
    assert "products" in response.json()
```

Note: This example assumes the existence of a `crud` module where the service layer code resides and a `schemas` module where the Pydantic models are defined. The `SessionLocal` and `engine` are assumed to be part of a `database` module.