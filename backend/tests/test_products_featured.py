In order to test success cases, error cases, data validation, and edge cases, we need to make a few changes to our endpoint code to add error handling and validation. Let's add a check to make sure the keyword provided for the search is not empty and that the number of products requested is within a reasonable range:

```python
@app.get("/products/featured", response_model=List[schemas.Product])
def read_featured_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=400, detail="Invalid number of products requested")
    products = crud.get_featured_products(db=db)
    return products

@app.get("/products/search/{keyword}", response_model=List[schemas.Product])
def search_products(keyword: str, db: Session = Depends(get_db)):
    if not keyword:
        raise HTTPException(status_code=400, detail="Invalid keyword provided")
    products = crud.search_products(db=db, keyword=keyword)
    return products
```

Now we can write more comprehensive unit tests:

```python
def test_read_featured_products():
    # Test success case
    response = client.get("/products/featured?limit=10")
    assert response.status_code == 200
    assert "products" in response.json()

    # Test data validation
    response = client.get("/products/featured?limit=0")
    assert response.status_code == 400
    assert "detail" in response.json()

    # Test edge case
    response = client.get("/products/featured?limit=101")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_search_products():
    # Test success case
    response = client.get("/products/search/test")
    assert response.status_code == 200
    assert "products" in response.json()

    # Test error case
    response = client.get("/products/search/")
    assert response.status_code == 404

    # Test data validation
    response = client.get("/products/search/ ")
    assert response.status_code == 400
    assert "detail" in response.json()
```

These tests cover a variety of situations, including successful requests, requests with invalid data, and edge cases. In a real-world scenario, you would also want to add tests to ensure the correct data is returned by the endpoints, by comparing it to expected results.