from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from .base import BaseService
from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


class BeverageService(BaseService):
    controller = BeverageController


@beverage.route('/', methods=POST)
def create_beverage():
    return BeverageService.create()


@beverage.route('/', methods=PUT)
def update_beverage():
    return BeverageService.update()


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return BeverageService.get_by_id(_id)


@beverage.route('/', methods=GET)
def get_beverages():
    return BeverageService.get_all()
