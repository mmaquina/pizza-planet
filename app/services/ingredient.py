from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from .base import BaseService
from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


class SizeService(BaseService):
    controller = IngredientController


@ingredient.route('/', methods=POST)
def create_ingredient():
    return SizeService.create()


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return SizeService.update()


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return SizeService.get_by_id(_id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return SizeService.get_all()
