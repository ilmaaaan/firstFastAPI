from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum




class Degreetype(Enum):
    newbie = "newbie"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: Degreetype

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []