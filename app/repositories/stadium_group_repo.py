from typing import List

from sqlalchemy import func

from app import db
from app.dataclasses.point_dc import PointDC
from app.models.stadium_group import StadiumGroup


def get_stadium_groups_by_points(points: List[PointDC]):
    return db.session.query(StadiumGroup) \
        .filter(func.ST_Contains(func.ST_MakePolygon(func.ST_GeomFromText(
            f"LINESTRING("
            f"{points[0].lat} {points[0].long}, "
            f"{points[1].lat} {points[1].long}, "
            f"{points[2].lat} {points[2].long}, "
            f"{points[3].lat} {points[3].long}, "
            f"{points[0].lat} {points[0].long}  "
            f")"
        )), func.ST_MakePoint(StadiumGroup.lat, StadiumGroup.long))).all()
