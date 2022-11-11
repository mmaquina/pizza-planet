from app.common.http_methods import GET, POST
from flask import Blueprint

from .base import BaseService
from ..controllers import OrderController


order = Blueprint('order', __name__)


class OrderService(BaseService):
    controller = OrderController


@order.route('/', methods=POST)
def create_order():
    return OrderService.create()


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return OrderService.get_by_id(_id)


@order.route('/', methods=GET)
def get_orders():
    return OrderService.get_all()
