from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from ..controllers import SizeController
from .base import BaseService


size = Blueprint('size', __name__)


class SizeService(BaseService):
    controller = SizeController


@size.route('/', methods=POST)
def create_size():
    return SizeService.create()
    

@size.route('/', methods=GET)
def get_sizes():
    return SizeService.get_all()


@size.route('/', methods=PUT)
def update_size():
    return SizeService.update()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return SizeService.get_by_id(_id)
