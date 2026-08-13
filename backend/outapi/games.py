from fastapi import Depends
from outapi.dependencies import get_db
from database.deal_repository import DealRepository
from schemas.game_response import GameResponse

@app.get("/api/v1/games", response_model=list[GameResponse])
def get_games(
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_games()