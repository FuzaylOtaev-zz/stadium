from app import db
from app.models.base import BaseModel


class StadiumImage(BaseModel):
    __tablename__ = "stadium_image"

    order_number = db.Column(db.Integer)
    is_default = db.Column(db.Boolean(), default=False)
    path = db.Column(db.String())
    stadium_id = db.Column(db.ForeignKey("stadium.id"), nullable=False)
