from typing import List

from sqlalchemy import func

from app import db
from app.dataclasses.point_dc import PointDC
from app.models.stadium import Stadium
from app.models.stadium_group import StadiumGroup
from app.models.address import Address
from app.models.user import User


def get_stadium_full_data(stadium_id: int):
    return db.session.query(Stadium, StadiumGroup, Address, User) \
        .select_from(Stadium)\
        .join(StadiumGroup, StadiumGroup.id == Stadium.stadium_group_id) \
        .join(Address, Address.id == StadiumGroup.address_id) \
        .join(User, User.id == StadiumGroup.owner_id) \
        .filter(Stadium.id == stadium_id, Stadium.is_deleted == False) \
        .first()


def get_stadiums_by_group_id(group_id: int):
    return db.session.query(Stadium) \
        .filter(Stadium.stadium_group_id == group_id) \
        .filter(Stadium.is_deleted == False) \
        .all()


def get_stadiums_by_points(points: List[PointDC]):
    return db.session.query(Stadium) \
        .filter(func.ST_Contains(func.ST_MakePolygon(func.ST_GeomFromText(
            f"LINESTRING("
            f"{points[0].lat} {points[0].long}, "
            f"{points[1].lat} {points[1].long}, "
            f"{points[2].lat} {points[2].long}, "
            f"{points[3].lat} {points[3].long}, "
            f"{points[0].lat} {points[0].long}  "
            f")"
        )), func.ST_MakePoint(Stadium.lat, Stadium.long))).all()

