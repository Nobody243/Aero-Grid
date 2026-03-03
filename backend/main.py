"""
AeroGrid FastAPI Backend Service
"""

from fastapi import FastAPI

app = FastAPI(title="AeroGrid API", version="0.1.0")

@app.get("/")
def root():
    return {"service": "AeroGrid Backend", "status": "online"}
