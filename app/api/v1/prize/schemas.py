from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class PlayerSchema(BaseModel):
    id: int
    username: str
    first_login: datetime 
    score: int


class BoostSchema(BaseModel):
    id: int
    name: str
    boost_type: str
    value: int


class PlayerBoostSchema(BaseModel):
    player_id: int
    boost_id: int
    acquired: datetime


class LevelSchema(BaseModel):
    id: int
    title: str
    order: int


class PrizeSchema(BaseModel):
    id: int
    title: str


class PlayerLevelSchema(BaseModel):
    player_id: int
    level_id: int
    completed: Optional[datetime]
    is_completed: bool
    score: int


class LevelPrizeSchema(BaseModel):
    level_id: int
    prize_id: int
    received: datetime