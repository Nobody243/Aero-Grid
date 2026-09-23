# Aero-Grid Backend

High-performance, stateless FastAPI backend providing AI endpoints for weather classification, route optimization, pathfinding, and reinforcement learning.

---

## AI Architecture & Endpoints

| Endpoint | Method | Algorithm / Engine | Description |
|---|---|---|---|
| `/city/random` | `GET` | Deterministic Seed Generator | Generates a 40×40 city with obstacles, NFZs, depot, and targets. |
| `/city/validate` | `POST` | BFS Reachability Checker | Verifies graph connectivity between depot and all delivery targets. |
| `/weather` | `POST` | Gaussian Naive Bayes | Returns flight verdict (`Safe to Fly`, `Requires Altitude Drop`, `Grounded`) and class probabilities. |
| `/weather/compare` | `POST` | 3-Model Ensemble | Compares Naive Bayes, Logistic Regression, and Decision Tree predictions. |
| `/weather/metrics` | `GET` | scikit-learn Metrics | Returns accuracy, confusion matrices, and feature importances. |
| `/weather/training-data` | `GET` | Dataset Exposer | Returns training data for scatter plot visualization. |
| `/optimize` | `POST` | Genetic Algorithm (TSP) | Computes near-optimal tour order using Order Crossover (OX) and tournament selection. |
| `/fly` | `POST` | A\* Search Pathfinder | Calculates grid paths per delivery leg avoiding obstacles with octile/manhattan heuristics. |
| `/learn/train` | `POST` | Tabular Q-Learning | Trains an RL agent on grid states with reward shaping. Returns Q-table and convergence stats. |
| `/learn/replay` | `POST` | Greedy Q Policy Replay | Replays greedy actions from a trained Q-table. |
| `/learn/generalize` | `POST` | Perturbation Stress-Test | Tests policy generalization under obstacle perturbations (manual or random). |

---

## Local Development

### Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

- API Documentation (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative Docs (ReDoc): [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Testing & SQA

Run the automated SQA and Security test suite:

```bash
python tests_sqa_security.py
```

Run Phase 1 integration verification:

```bash
python _phase1_verify.py
```

---

## Production Deployment (Render)

The backend is configured via [`render.yaml`](../render.yaml) for deployment on Render.

**Environment Variables:**
- `ENVIRONMENT`: `production` *(disables `/docs` and enables rate limiting)*
- `ALLOWED_ORIGINS`: Comma-separated list of allowed frontend domains.
