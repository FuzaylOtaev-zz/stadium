from app.models.stadium_image import StadiumImage
from app.models import db


def get_stadium_images(stadium_id: int):
    return db.session.query(StadiumImage)\
            .filter(StadiumImage.stadium_id == stadium_id, StadiumImage.is_deleted == False)\
            .all()