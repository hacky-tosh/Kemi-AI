from pydantic import BaseModel
from typing import List, Dict

class Chapter(BaseModel):
    name: str
    text: str
    ratings: Dict[str, int]

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
    average_rating: float 
