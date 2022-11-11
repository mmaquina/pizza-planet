from flask import jsonify, request
from typing import Optional

from ..controllers.base import BaseController

class BaseService:
    controller: Optional[BaseController] = None

    @classmethod
    def create(cls):
        item, error = cls.controller.create(request.json)
        response = item if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def get_all(cls):
        item, error = cls.controller.get_all()
        response = item if not error else {'error': error}
        status_code = 200 if item else 404 if not error else 400
        return jsonify(response), status_code
        
    @classmethod
    def update(cls):
        item, error = cls.controller.update(request.json)
        response = item if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @classmethod
    def get_by_id(cls, _id):
        item, error = cls.controller.get_by_id(_id)
        response = item if not error else {'error': error}
        status_code = 200 if item else 404 if not error else 400
        return jsonify(response), status_code
