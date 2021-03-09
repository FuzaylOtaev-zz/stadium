from dataclasses import dataclass


@dataclass
class StadiumImageDC:
    id: int
    order_number: int
    is_default: bool
    path: str

    def __init__(self):
        pass

