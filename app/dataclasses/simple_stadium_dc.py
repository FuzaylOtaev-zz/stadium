from dataclasses import dataclass


@dataclass
class StadiumDC:
    id: int
    name: str
    status: str
    lat: float
    long: float

    def __init__(self):
        pass


