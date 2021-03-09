from dataclasses import dataclass
from typing import List

from app.dataclasses.simple_stadium_dc import StadiumDC


@dataclass
class StadiumGroupDC:
    id: int
    name: str
    lat: float
    long: float
    stadiums: List[StadiumDC]
    stadium_ids = List[int]

    def __init__(self):
        pass
