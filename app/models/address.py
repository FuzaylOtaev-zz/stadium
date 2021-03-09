from app import db
from app.models.base import BaseModel


class Address(BaseModel):
    __tablename__ = "address"

    region = db.Column(db.String())
    city = db.Column(db.String())
    zipcode = db.Column(db.String())
    street = db.Column(db.String())
