// import { useEffect, useState } from 'react';

// function App() {
//   const [message, setMessage] = useState('Loading...');

//   useEffect(() => {
//     fetch('http://localhost:8000/api/hello')
//       .then((res) => res.json())
//       .then((data) => setMessage(data.message))
//       .catch(() => setMessage('Error fetching message'));
//   }, []);

//   return (
//     <div>
//       <h1>Frontend + FastAPI</h1>
//       <p>{message}</p>
//     </div>
//   );
// }

// export default App;

// // use npm run dev to start the frontend 

import { Routes, Route, Navigate } from "react-router-dom"
import Home from "./pages/Home"
import Story from "./pages/Story"

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/story/:id" element={<Story />} />
      {/* fallback for unknown paths */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}

export default App

