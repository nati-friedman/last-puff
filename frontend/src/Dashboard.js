import { useEffect, useState } from "react";
import axios from "axios";

function Dashboard({ userId }) {
  const [progress, setProgress] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:5000/progress/${userId}`)
      .then(res => setProgress(res.data));
  }, [userId]);

  if (!progress) return <p>Loading...</p>;

  return (
    <div>
      <h2>Your Progress</h2>
      <p>Days Smoke-Free: {progress.days_smoke_free}</p>
      <p>Cigarettes Avoided: {progress.cigarettes_avoided}</p>
      <p>Money Saved: ${progress.money_saved}</p>
    </div>
  );
}

export default Dashboard;