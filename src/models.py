from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    orderCode: str
    networkId: int
    txhash: Optional[str] = None 

class Deposit(BaseModel):
    orderCode: str
    networkId: int
    wallet: str
    txhash: str
    amount: int
    currency: str