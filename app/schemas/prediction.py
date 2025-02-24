from pydantic import BaseModel
from typing import Optional


class PredictionInput(BaseModel):
    tube: Optional[int] = None
    pind: Optional[float] = None
    korrus: Optional[int] = None
    korruseid: Optional[int] = None
    ehitusaasta: Optional[int] = None
    linn: Optional[str] = None
    maakond: Optional[str] = None
    linnaosa: Optional[str] = None
    seisukord: Optional[str] = None
    omandivorm: Optional[str] = None
    energiamärgis: Optional[str] = None

