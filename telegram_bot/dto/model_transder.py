from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: List[str]