from fastapi import FastAPI
from workout.routers import api_router

app=FastAPI(title="Workout")
app.include_router(api_router)