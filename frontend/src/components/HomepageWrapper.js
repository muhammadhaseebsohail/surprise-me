Here's a simplified example of how you might structure your components to create a homepage with the specified requirements. This example uses CSS-in-JS with styled-components.

```jsx
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

// Styled components
const HomepageWrapper = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const NavBar = styled.nav`
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 50px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const SearchBar = styled.input`
  width: 200px;
  height: 30px;
  padding: 5px;
`;

// Main component
const Homepage = ({ products, user }) => {
  const [search, setSearch] = useState('');

  // Error handling for the products prop
  useEffect(() => {
    if (!Array.isArray(products)) {
      throw new Error('Invalid prop: products must be an array');
    }
  }, [products]);

  return (
    <HomepageWrapper>
      <NavBar>
        <div>Main Navigation</div>
        <SearchBar 
          type="text" 
          placeholder="Search products..." 
          value={search} 
          onChange={e => setSearch(e.target.value)}
        />
        <div>User: {user.name}</div>
      </NavBar>
      <div>
        {products.map(product => (
          <div key={product.id}>{product.name}</div>
        ))}
      </div>
    </HomepageWrapper>
  );
};

// PropTypes
Homepage.propTypes = {
  products: PropTypes.array.isRequired,
  user: PropTypes.object.isRequired,
};

export default Homepage;
```

Here is a basic setup for unit testing using Jest and React Testing Library:

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import Homepage from './Homepage';

test('renders homepage', () => {
  render(<Homepage products={[]} user={{ name: 'John Doe' }} />);
  const linkElement = screen.getByText(/main navigation/i);
  expect(linkElement).toBeInTheDocument();
});
```

Please note that this is a simplified example and might need adjustments based on your specific project requirements.