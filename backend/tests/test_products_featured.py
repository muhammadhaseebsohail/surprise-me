Here are the unit tests for the FastAPI endpoint:

```python
from fastapi.testclient import TestClient
from main import app, Product, ProductService
from unittest.mock import patch
import pytest

client = TestClient(app)

# Test data
test_products = [
    Product(id=1, name="product1", description="desc1", price=100.0, is_featured=True),
    Product(id=2, name="product2", description="desc2", price=200.0, is_featured=True),
]
test_product_service = ProductService()


# Success Case
@patch.object(test_product_service, "get_featured_products")
def test_get_featured_products_success(mock_get_featured_products):
    mock_get_featured_products.return_value = test_products

    response = client.get("/products/featured")
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert isinstance(response.json(), list)
    assert len(response.json()) == len(test_products)
    for product in response.json():
        assert 'id' in product
        assert 'name' in product
        assert 'description' in product
        assert 'price' in product
        assert 'is_featured' in product

# Error Case
@patch.object(test_product_service, "get_featured_products")
def test_get_featured_products_not_found(mock_get_featured_products):
    mock_get_featured_products.return_value = []

    response = client.get("/products/featured")
    assert response.status_code == 404
    assert response.json() == {"detail": "Featured products not found"}

# Edge Case
@patch.object(test_product_service, "get_featured_products")
def test_get_featured_products_empty(mock_get_featured_products):
    mock_get_featured_products.return_value = []

    response = client.get("/products/featured")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0

# Data validation
def test_get_featured_products_invalid_url():
    response = client.get("/products/invalid")
    assert response.status_code == 404
```

These tests cover:

- Success case: when there are featured products and the API returns them correctly.
- Error case: when there are no featured products and the API returns a 404 error.
- Edge case: when there are no products at all and the API returns an empty list.
- Data validation: when an invalid URL is supplied, the API returns a 404 error.