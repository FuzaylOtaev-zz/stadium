from typing import List

from app.models.stadium import Stadium
from app.dataclasses.point_dc import PointDC
from app.dataclasses.simple_stadium_dc import StadiumDC
from app.repositories import stadium_repo


def get_stadiums_by_points(points: List[PointDC]):
    stadiums = stadium_repo.get_stadiums_by_points(points)
    stadiums_dc = _to_stadiums_dc(stadiums)

    return stadiums_dc


def _to_stadiums_dc(stadiums: List[Stadium]):
    stadiums_dc = []
    for stadium in stadiums:
        stadium_dc = _to_stadium_dc(stadium)
        stadiums_dc.append(stadium_dc)

    return stadiums_dc


def _to_stadium_dc(stadium: Stadium):
    dc = StadiumDC()
    dc.id = stadium.id
    dc.status = stadium.status
    dc.name = stadium.name
    dc.lat = stadium.lat
    dc.long = stadium.long

    return dc
