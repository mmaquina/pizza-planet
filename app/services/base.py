from flask import jsonify, request
from typing import Optional

from ..controllers.base import BaseController

class BaseService:
    controller: Optional[BaseController] = None

    @staticmethod
    def adapt_response(item, error):
        response = item if not error else {'error': error}
        status_code = 200 if item else 404 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def create(cls):
        item, error = cls.controller.create(request.json)
        return cls.adapt_response(item, error)

    @classmethod
    def get_all(cls):
        item, error = cls.controller.get_all()
        return cls.adapt_response(item, error)

        
    @classmethod
    def update(cls):
        item, error = cls.controller.update(request.json)
        return cls.adapt_response(item, error)


    @classmethod
    def get_by_id(cls, _id):
        item, error = cls.controller.get_by_id(_id)
        return cls.adapt_response(item, error)

