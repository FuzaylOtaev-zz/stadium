from dataclasses import asdict

from flask import Blueprint, jsonify, abort

from app.decorators.response import response
from app.errors.not_found_error import NotFoundError
from app.services.get_stadium_full_data import get_stadium_full_data


bp = Blueprint("stadium", __name__, url_prefix='/stadium')


@bp.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404


@bp.route("/<stadium_id>", methods=["GET"])
@response
def get_stadium_groups(stadium_id: int):
    try:
        stadium_dc = get_stadium_full_data(int(stadium_id))
        stadium_dict = asdict(stadium_dc)

        return dict(stadium=stadium_dict)
    except NotFoundError as e:
        abort(404, e)
