from dataclasses import asdict

from flask import Blueprint, request, jsonify

from app.decorators.response import response
from app.services.get_stadiums_by_points import get_stadiums_by_points
from app.dataclasses.point_dc import PointDC

bp = Blueprint("stadiums", __name__, url_prefix="/stadiums")


@bp.route("/points", methods=["GET"])
@response
def retrieve_stadiums_by_points():
    points = _query_params_to_points()
    stadiums = get_stadiums_by_points(points)

    return dict(stadiums=[asdict(s) for s in stadiums])


def _query_params_to_points():
    point1 = PointDC(request.args["lat1"], request.args["long1"])
    point2 = PointDC(request.args["lat2"], request.args["long2"])
    point3 = PointDC(request.args["lat3"], request.args["long3"])
    point4 = PointDC(request.args["lat4"], request.args["long4"])

    return [point1, point2, point3, point4]


