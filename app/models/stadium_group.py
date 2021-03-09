from geoalchemy2 import Geometry

from app import db
from app.models.base import BaseModel


class StadiumGroup(BaseModel):
    __tablename__ = "stadium_group"

    name = db.Column(db.String())
    lat = db.Column(db.Float())
    long = db.Column(db.Float())
    geom = db.Column(Geometry("POINT,4326"))
    owner_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    address_id = db.Column(db.Integer())
