To implement the functionality for displaying featured products on the homepage, we will create an API endpoint that fetches featured products from the database. 

First, let's define our database model for the product and the Pydantic model for the product.

```python
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Database Model
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_featured: bool

app = FastAPI()

# Pydantic Models
class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    is_featured: bool = False

class Product(ProductBase):
    id: int
    is_featured: bool

    class Config:
        orm_mode = True
```
Now, let's create a service layer to handle the database operations.

```python
# Service Layer
class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_featured_products(self) -> List[Product]:
        result = await self.session.execute(select(Product).where(Product.is_featured == True))
        return result.scalars().all()
```

Now, let's create our API endpoint for retrieving the featured products.

```python
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

# Dependency
def get_db():
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    async_session = session()
    try:
        yield async_session
    finally:
        await async_session.close()

@app.get("/products/featured", response_model=List[Product])
async def get_featured_products(session: AsyncSession = Depends(get_db)):
    """
    Retrieve featured products
    """
    product_service = ProductService(session)
    products = await product_service.get_featured_products()
    if not products:
        raise HTTPException(status_code=404, detail="Featured products not found")
    return products
```

And finally, let's create a test case for our API endpoint.

```python
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

def test_get_featured_products():
    response = client.get("/products/featured")
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert isinstance(response.json(), list)
```

Note: For simplicity, the example above doesn't include the setup code for the SQLAlchemy ORM or async engine, and assumes that these are created elsewhere in your application. Please ensure to setup your database connection and session properly.