import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router';

const RegisterForm = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/api/register/', {
        username,
        email,
        password,
      })
      .then(res => console.log('Registered:', res.data))
      .catch(err => console.error('Error:', err.response?.data));
      navigate('/login');
    } catch (error) {
      alert(error);
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <h2>Register</h2>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        />
      <button type="submit">Register</button>
    </form>
  );
};

export default RegisterForm;
