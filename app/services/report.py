from app.common.http_methods import GET
from flask import Blueprint

from .base import BaseService
from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/mri', methods=GET)
def get_most_requested_ingredient():
    ingredient, error = ReportController.get_most_requested_ingredient()
    return BaseService.adapt_response(ingredient, error)


@report.route('/month', methods=GET)
def get_month_with_most_revenue():
    month, error = ReportController.get_month_with_most_revenue()
    return BaseService.adapt_response(month, error)


@report.route('/top3', methods=GET)
def get_top3_customers():
    top3, error = ReportController.get_top3_customers()
    return BaseService.adapt_response(top3, error)
