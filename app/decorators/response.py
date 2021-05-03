from flask import jsonify

from app.errors.validation_error import ValidationError


def response(func):
    def wrapper(**args):
        try:
            result = func(**args)
            return jsonify(dict(result=result, errors=dict()))
        except ValidationError as e:
            return dict(result=None, errors=e.args[0])

    return wrapper
