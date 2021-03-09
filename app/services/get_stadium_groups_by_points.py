from typing import List

from app.dataclasses.stadium_group import StadiumGroupDC
from app.models.stadium_group import StadiumGroup
from app.models.stadium import Stadium
from app.dataclasses.point_dc import PointDC
from app.dataclasses.simple_stadium_dc import StadiumDC
from app.repositories import stadium_group_repo
from app.repositories import stadium_repo


def get_stadium_groups_by_points(points: List[PointDC]):
    stadium_groups = stadium_group_repo.get_stadium_groups_by_points(points)
    if not stadium_groups:
        return []

    stadium_groups_dc = _to_stadium_groups_dc(stadium_groups)
    for sg in stadium_groups_dc:
        stadiums = stadium_repo.get_stadiums_by_group_id(sg.id)
        stadiums_dc = _to_stadiums_dc(stadiums)
        sg.stadiums = stadiums_dc

    return stadium_groups_dc


def _to_stadium_groups_dc(stadium_groups: List[StadiumGroup]):
    stadium_groups_dc = []
    for stadium_group in stadium_groups:
        stadium_group_dc = _to_stadium_group_dc(stadium_group)
        stadium_groups_dc.append(stadium_group_dc)

    return stadium_groups_dc


def _to_stadium_group_dc(stadium_group: StadiumGroup):
    dc = StadiumGroupDC()
    dc.id = stadium_group.id
    dc.name = stadium_group.name
    dc.lat = stadium_group.lat
    dc.long = stadium_group.long

    return dc


def _to_stadiums_dc(stadiums: List[Stadium]):
    stadiums_dc = []
    for stadium in stadiums:
        stadium_dc = _to_stadium_dc(stadium)
        stadiums_dc.append(stadium_dc)

    return stadiums_dc


def _to_stadium_dc(stadium: Stadium):
    dc = StadiumDC()
    dc.id = stadium.id
    dc.name = stadium.name
    dc.status = stadium.status
    dc.long = stadium.long
    dc.lat = stadium.lat

    return dc
