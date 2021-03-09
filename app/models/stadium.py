from geoalchemy2 import Geometry

from app import db
from app.models.base import BaseModel


class Stadium(BaseModel):
    __tablename__ = "stadium"

    ACTIVE = "active"
    INACTIVE = "inactive"

    name = db.Column(db.String())
    status = db.Column(db.String())
    lat = db.Column(db.Float())
    long = db.Column(db.Float())
    geom = db.Column(Geometry("POINT,4326"))
    stadium_group_id = db.Column(db.ForeignKey("stadium_group.id"), nullable=False)
