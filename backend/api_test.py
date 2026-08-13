from fastapi import FastAPI
from fastapi import Depends
from outapi.dependencies import get_db
from database.deal_repository import DealRepository
from schemas.game_response import GameResponse

app = FastAPI(title="Steam Deals API")

@app.get("/")
def root():
    return {"message": "Welcome to the Steam Deals API!"}

@app.get("/api/games", response_model=list[GameResponse])
def get_games(
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_games()

@app.get("/api/v1/deals", response_model=list[GameResponse])
def get_deals(
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_games_on_sale()