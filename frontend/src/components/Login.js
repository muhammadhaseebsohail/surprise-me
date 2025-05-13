Complete component code:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './Login.css';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await onLogin({ username, password });
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      {error && <div className="error">{error}</div>}
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Log In'}
      </button>
      <a href="/forgot-password">Forgot password?</a>
    </form>
  );
};

Login.propTypes = {
  onLogin: PropTypes.func.isRequired,
};

export default Login;
```

CSS/styling:

```css
/* Login.css */

.login-form {
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
}

.login-form input {
  margin-bottom: 10px;
  padding: 10px;
  font-size: 16px;
}

.login-form button {
  padding: 10px;
  font-size: 16px;
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
}

.login-form .error {
  color: red;
  margin-bottom: 10px;
}
```

PropTypes:

```jsx
Login.propTypes = {
  onLogin: PropTypes.func.isRequired,
};
```

Basic unit test setup:

```jsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Login from './Login';

test('renders login form', () => {
  const onLogin = jest.fn();
  const { getByPlaceholderText } = render(<Login onLogin={onLogin} />);

  const usernameInput = getByPlaceholderText('Username');
  const passwordInput = getByPlaceholderText('Password');

  fireEvent.change(usernameInput, { target: { value: 'testuser' } });
  fireEvent.change(passwordInput, { target: { value: 'testpass' } });
  
  fireEvent.click(getByText('Log In'));

  expect(onLogin).toBeCalledWith({ username: 'testuser', password: 'testpass' });
});
```