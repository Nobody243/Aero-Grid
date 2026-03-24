const API_BASE = 'http://127.0.0.1:8000';

export async function fetchCityRandom(seed = 7) {
  const res = await fetch(`${API_BASE}/city/random?seed=${seed}`);
  return res.json();
}


export async function fetchAStarPlan(payload: any) {
  const res = await fetch(`${API_BASE}/api/plan/astar`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  return res.json();
}
