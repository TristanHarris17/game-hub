from pydantic import BaseModel

from datetime import datetime
from decimal import Decimal

class PricingResponseBase(BaseModel):
    game_id: int

class PricingResponse(PricingResponseBase):
    normal_price: float
    sale_price: float | None
    savings: float
    timestamp: datetime
