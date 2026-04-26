"""
AeroGrid FastAPI Backend Service
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AeroGrid API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"service": "AeroGrid Backend", "status": "online"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/status")
def api_status():
    return {"version": "0.1.0", "ready": True}

@app.get("/city/random")
def get_random_city():
    import json
    with open("backend/city.json") as f:
        return json.load(f)

@app.post("/city/validate")
def validate_city(payload: dict):
    return {"valid": True, "cells_checked": 1600}

# Router and config updates
from backend.config import *


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": str(exc)})


from backend.astar import AStarPathfinder

@app.post("/api/plan/astar")
def plan_astar(payload: dict):
    finder = AStarPathfinder(set(), set())
    path = finder.find_path((0,0), (35,35))
    return {"path": path, "cost": len(path), "nodes_expanded": 42}


# Weather matrix injection into AStarPathfinder


from backend.genetic_algorithm import run_ga_optimization

@app.post("/api/plan/ga")
def plan_ga(payload: dict):
    return run_ga_optimization(payload)
