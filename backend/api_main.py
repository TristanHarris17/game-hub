from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from outapi import games, pricing
from database.init_db import init_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield

app = FastAPI(
    title="Steam Deals API",
    lifespan=lifespan
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    games.router,
    prefix="/api/v1/games",
    tags=["games"]
)


app.include_router(
    pricing.router,
    prefix="/api/v1/pricing",
    tags=["pricing"]
)


@app.get("/")
def root():
    return {"message": "Welcome to the Steam Deals API!"}