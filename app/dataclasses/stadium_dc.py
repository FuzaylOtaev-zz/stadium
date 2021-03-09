from dataclasses import dataclass
from typing import List

from app.dataclasses.address_dc import AddressDC
from app.dataclasses.owner_dc import OwnerDC
from app.dataclasses.stadium_image_dc import StadiumImageDC


@dataclass
class StadiumFullDataDC:
    id: int
    name: str
    status: str
    lat: float
    long: float
    owner: OwnerDC
    address: AddressDC
    images: List[StadiumImageDC]

    def __init__(self):
        pass






