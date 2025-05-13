Here is the complete code for the Login page component.

1. Component Code:

```jsx
import React, { useState } from "react";
import PropTypes from "prop-types";
import styles from "./LoginPage.module.css";

const LoginPage = ({ onLogin, onForgotPassword }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const validate = () => {
    return username.length > 0 && password.length > 0;
  };

  const handleSubmit = event => {
    event.preventDefault();

    if (validate()) {
      onLogin(username, password);
    } else {
      setError("Please fill in all fields.");
    }
  };

  return (
    <div className={styles.container}>
      {error && <div className={styles.error}>{error}</div>}
      <form className={styles.form} onSubmit={handleSubmit}>
        <input
          className={styles.input}
          type="text"
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <input
          className={styles.input}
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <button className={styles.button} type="submit">
          Login
        </button>
        <a className={styles.forgotPassword} onClick={onForgotPassword}>Forgot password?</a>
      </form>
    </div>
  );
};

LoginPage.propTypes = {
  onLogin: PropTypes.func.isRequired,
  onForgotPassword: PropTypes.func.isRequired
};

export default LoginPage;
```

2. CSS/Styling:

```css
/* LoginPage.module.css */

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.form {
  display: flex;
  flex-direction: column;
}

.input {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.error {
  color: red;
  margin-bottom: 10px;
}

.forgotPassword {
  color: #007bff;
  cursor: pointer;
  margin-top: 10px;
  text-decoration: underline;
}
```

3. PropTypes:

Already included in the component code.

4. Basic Unit Test Setup:

```jsx
import { render, fireEvent } from '@testing-library/react';
import LoginPage from './LoginPage';

test('renders login page', () => {
  const handleLogin = jest.fn();
  const handleForgotPassword = jest.fn();
  const { getByPlaceholderText, getByText } = render(<LoginPage onLogin={handleLogin} onForgotPassword={handleForgotPassword} />);

  fireEvent.change(getByPlaceholderText('Username'), { target: { value: 'TestUser' } });
  fireEvent.change(getByPlaceholderText('Password'), { target: { value: 'TestPassword' } });
  fireEvent.click(getByText('Login'));

  expect(handleLogin).toBeCalledWith('TestUser', 'TestPassword');
});
```