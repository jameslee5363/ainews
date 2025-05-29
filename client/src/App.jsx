import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('http://localhost:8000/api/hello')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage('Error fetching message'));
  }, []);

  return (
    <div>
      <h1>Frontend + FastAPI</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;

// use npm run dev to start the frontend 