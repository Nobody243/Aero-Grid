"""
AeroGrid FastAPI Backend Service
"""

from fastapi import FastAPI

app = FastAPI(title="AeroGrid API", version="0.1.0")

@app.get("/")
def root():
    return {"service": "AeroGrid Backend", "status": "online"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/status")
def api_status():
    return {"version": "0.1.0", "ready": True}
