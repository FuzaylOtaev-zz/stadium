from dataclasses import dataclass
from typing import List


@dataclass
class OwnerDC:
    id: int
    first_name: str
    last_name: str
    phone_numbers: List[str]
    email: str
    status: str
    telegram: str
    facebook: str
    roles = List[str]

    def __init__(self):
        pass

