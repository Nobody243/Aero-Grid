# Aero-Grid Frontend

Interactive Next.js 15 visualization interface for the **Aero-Grid** Autonomous Drone Routing AI platform.

---

## Features

- **Interactive 40×40 City Canvas**: Real-time rendering of drone depot, customer delivery targets, obstacles/buildings, and No-Fly Zones (NFZ).
- **Interactive Multi-Phase AI Stepper**:
  1. **City Builder & Validator**: Interactive grid editor with reachability verification.
  2. **Weather Safety Radar**: Bayesian pre-flight classifier with multi-model comparison (GaussianNB, Logistic Regression, Decision Tree).
  3. **Route Optimizer (TSP)**: Genetic algorithm with generational animation and chromosome inspection.
  4. **A\* Pathfinding Visualizer**: Exploration frontier sweep with octile, manhattan, and euclidean heuristics.
  5. **Q-Learning Policy Explorer**: Tabular reinforcement learning with dynamic obstacle stress-testing & perturbation.
- **Global Mission State**: Powered by Zustand for atomic updates and stateless backend interoperability.
- **Smooth Animations**: High-performance UI transitions built with Framer Motion.

---

## Tech Stack

- **Framework**: Next.js 15 (App Router), React 19, TypeScript
- **State Management**: Zustand
- **Canvas / 3D**: HTML5 Canvas API + React Three Fiber / drei
- **Charts**: Recharts
- **Icons**: Lucide React
- **Styling**: Vanilla CSS Design Tokens & CSS Custom Properties

---

## Getting Started

### 1. Install Dependencies

```bash
npm install
```

### 2. Environment Variables

Create `.env.local` in the `frontend` folder:

```bash
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

> **Note**: In production builds, if `NEXT_PUBLIC_API_URL` is omitted, the client automatically falls back to `https://aero-grid.onrender.com`.

### 3. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to interact with the mission dashboard.

### 4. Build Production Bundle

```bash
npm run build
npm run start
```

### 5. Linting

```bash
npm run lint
```
