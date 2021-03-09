from app import db
from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    ACTIVE = "active"
    INACTIVE = "inactive"

    ROLE_USER = "user"
    ROLE_OWNER = "owner"

    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    phone_numbers = db.Column(db.ARRAY(db.String()))
    email = db.Column(db.String())
    status = db.Column(db.String(), default=ACTIVE)
    telegram = db.Column(db.String())
    facebook = db.Column(db.String())
    roles = db.Column(db.ARRAY(db.String()), default=[ROLE_USER])
