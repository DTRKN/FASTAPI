from pydantic import BaseModel
from enum import Enum
# from datetime import date
from typing import Optional
from decimal import Decimal

class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'
class Operation(BaseModel):
    id: int
    date: str
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

    class Config:
        orm_mode = True