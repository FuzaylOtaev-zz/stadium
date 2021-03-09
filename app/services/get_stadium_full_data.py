from typing import List

from app.errors.not_found_error import NotFoundError
from app.models.stadium_image import StadiumImage
from app.dataclasses.address_dc import AddressDC
from app.dataclasses.owner_dc import OwnerDC
from app.dataclasses.stadium_dc import StadiumFullDataDC
from app.dataclasses.stadium_image_dc import StadiumImageDC
from app.models.address import Address
from app.models.user import User
from app.repositories import stadium_repo
from app.repositories.stadium_image_repo import get_stadium_images


def get_stadium_full_data(stadium_id: int) -> StadiumFullDataDC:
    result = _get_and_validate_stadium(stadium_id)
    stadium_dt = _to_stadium_dc(result)

    stadium_images = get_stadium_images(stadium_id)
    stadium_dt.images = _to_stadium_images_dc(stadium_images)

    return stadium_dt


def _get_and_validate_stadium(stadium_id: int):
    stadium = _get_stadium(stadium_id)
    _validate_stadium(stadium)

    return stadium


def _get_stadium(stadium_id: int):
    return stadium_repo.get_stadium_full_data(stadium_id)


def _validate_stadium(result):
    if result is None:
        raise NotFoundError("stadium not found.")


def _to_stadium_dc(result) -> StadiumFullDataDC:
    stadium = _extract_stadium(result)
    dc = StadiumFullDataDC()
    dc.id = stadium.id
    dc.name = stadium.name
    dc.status = stadium.status
    dc.long = stadium.long
    dc.lat = stadium.lat
    dc.owner = _to_owner_dc(_extract_owner(result))
    dc.address = _to_address_dc(_extract_address(result))

    return dc


def _extract_stadium(result):
    if hasattr(result, "Stadium"):
        return result.Stadium


def _extract_owner(result):
    if hasattr(result, "User"):
        return result.User


def _extract_address(result):
    if hasattr(result, "Address"):
        return result.Address


def _to_owner_dc(owner: User):
    if owner is None:
        raise Exception("owner not found.")

    dc = OwnerDC()
    dc.id = owner.id
    dc.first_name = owner.first_name
    dc.last_name = owner.last_name
    dc.status = owner.status
    dc.email = owner.email
    dc.phone_numbers = owner.phone_numbers
    dc.telegram = owner.telegram
    dc.facebook = owner.facebook

    return dc


def _to_address_dc(address: Address):
    if address is None:
        return None

    dt = AddressDC()
    dt.id = address.id
    dt.zipcode = address.zipcode
    dt.city = address.city
    dt.region = address.region
    dt.street = address.street

    return dt


def _to_stadium_images_dc(images: List[StadiumImage]):
    dc_images = []
    for image in images:
        dc_image = _to_stadium_image_dc(image)
        dc_images.append(dc_image)

    return dc_images


def _to_stadium_image_dc(image: StadiumImage):
    if image is None:
        return None

    dc = StadiumImageDC()
    dc.id = image.id
    dc.order_number = image.order_number
    dc.is_default = image.is_default
    dc.path = image.path

    return dc

