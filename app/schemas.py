from pydantic import BaseModel
from typing import List, Optional

class Value(BaseModel):
    unit: str
    value: str

class Item(BaseModel):
    name: str
    values: List[Value]

class WineData(BaseModel):
    description: str
    year: str
    data: List[Item]

class QueryParams(BaseModel):
    year: str
    opt: str
    sub_opt: Optional[str] = None

class Response(BaseModel):
    message: str
    data: WineData