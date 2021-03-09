from dataclasses import dataclass


@dataclass
class AddressDC:
    id: int
    region: str
    city: str
    zipcode: str
    street: str

    def __init__(self):
        pass

