Sure, here is a simple implementation of a homepage that consists of a navigation bar, search function, and a display of featured products. For simplicity, let's use hooks and CSS-in-JS styling with the styled-components library.

1. Component code:

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const NavBar = styled.div`
  display: flex;
  justify-content: space-between;
  padding: 20px;
  background-color: #f8f9fa;
`;

const SearchInput = styled.input`
  margin-right: 20px;
`;

const ProductsContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding: 20px;
`;

const ProductCard = styled.div`
  border: 1px solid #f8f9fa;
  padding: 20px;
`;

const HomePage = ({ products }) => {
  const [search, setSearch] = useState('');
  const [filteredProducts, setFilteredProducts] = useState([]);

  useEffect(() => {
    setFilteredProducts(
      products.filter((product) =>
        product.name.toLowerCase().includes(search.toLowerCase())
      )
    );
  }, [search, products]);

  return (
    <div>
      <NavBar>
        <h1>Our Store</h1>
        <div>
          <SearchInput
            type="text"
            placeholder="Search products"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>
      </NavBar>

      <ProductsContainer>
        {filteredProducts.map((product) => (
          <ProductCard key={product.id}>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
          </ProductCard>
        ))}
      </ProductsContainer>
    </div>
  );
};

HomePage.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default HomePage;
```

2. CSS/Styling is included in the component code itself using styled-components.

3. PropTypes:

```jsx
HomePage.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
    })
  ).isRequired,
};
```

4. Basic unit test setup:

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import HomePage from './HomePage';

test('renders homepage with products', () => {
  const products = [
    { id: '1', name: 'Product 1', description: 'This is product 1' },
    { id: '2', name: 'Product 2', description: 'This is product 2' },
  ];

  render(<HomePage products={products} />);

  expect(screen.getByText(/Our Store/i)).toBeInTheDocument();
  expect(screen.getByText(/Product 1/i)).toBeInTheDocument();
  expect(screen.getByText(/Product 2/i)).toBeInTheDocument();
});
```
This test checks if the homepage is rendered correctly with the provided products.