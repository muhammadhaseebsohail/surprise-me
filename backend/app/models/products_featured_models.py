We've already defined our Pydantic models in the previous steps (ProductBase, ProductCreate, Product). These models are used for validating incoming data and for structuring outgoing data. 

For instance, the ProductCreate model can be used as a request model for creating a new product:

```python
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product
    """
    db_product = crud.create_product(db=db, product=product)
    return db_product
```

Here, `schemas.ProductCreate` is used as a Pydantic model to validate the request body when creating a new product. The `response_model` parameter indicates that the endpoint response will be formatted according to the `schemas.Product` model.

On the service layer, the create_product function could look something like this:

```python
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
```

As for the response models, they are already specified in the endpoint definitions with the `response_model` parameter. 

The data transfer objects (DTOs) are the instances of the Pydantic models that we are passing around. For instance, in the example above, the `product` variable is a DTO. 

As for unit tests for the create_product endpoint, it could look something like this:

```python
def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "price": 19.99})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Test Product"
    assert response.json()["price"] == 19.99
```

This test checks the status code of the response, and verifies that the returned product has an "id" field and that the "name" and "price" fields match the input data.