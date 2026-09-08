from fastapi import Depends, APIRouter
from outapi.dependencies import get_db
from database.deal_repository import DealRepository
from schemas.game_response import GameResponse

router = APIRouter()

@router.get("/", response_model=list[GameResponse])
def get_games(
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_games()

@router.get("/sales", response_model=list[GameResponse])
def get_sales(
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_games_on_sale()

@router.get("/{steam_app_id}", response_model=GameResponse)
def get_game_by_steam_app_id(
    steam_app_id: int,
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_game_by_steam_app_id(steam_app_id)

@router.get("/internal-id/{game_id}", response_model=GameResponse)
def get_game_by_id(
    game_id: int,
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_game_by_id(game_id)