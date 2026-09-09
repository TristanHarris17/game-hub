from fastapi import Depends, APIRouter
from outapi.dependencies import get_db
from database.deal_repository import DealRepository
from schemas.game_response import GameResponse
from schemas.pricing_response import PricingResponse
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{game_id}", response_model=PricingResponse)
def get_pricing(
    game_id: int,
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_latest_price(game_id)

@router.get("/{game_id}/history", response_model=list[PricingResponse])
def get_pricing_history(
    game_id: int,
    db: Session = Depends(get_db)
):
    repository = DealRepository(db)
    return repository.get_price_history(game_id)
