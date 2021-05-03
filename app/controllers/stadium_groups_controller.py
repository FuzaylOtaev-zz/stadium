from dataclasses import asdict

from flask import Blueprint, request, jsonify

from app.dataclasses.point_dc import PointDC
from app.decorators.response import response
from app.services.get_stadium_groups_by_points import get_stadium_groups_by_points

bp = Blueprint("stadium_groups", __name__, url_prefix="/stadium_groups")


@bp.route("/points", methods=["GET"])
@response
def retrieve_stadium_groups_by_points():
    points = _query_params_to_points()
    stadium_groups = get_stadium_groups_by_points(points)

    return dict(stadium_groups=[asdict(sg) for sg in stadium_groups])


def _query_params_to_points():
    point1 = PointDC(request.args["lat1"], request.args["long1"])
    point2 = PointDC(request.args["lat2"], request.args["long2"])
    point3 = PointDC(request.args["lat3"], request.args["long3"])
    point4 = PointDC(request.args["lat4"], request.args["long4"])

    return [point1, point2, point3, point4]


