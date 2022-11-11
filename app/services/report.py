from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/mri', methods=GET)
def get_most_requested_ingredient():
    ingredient, error = ReportController.get_most_requested_ingredient()
    response = ingredient if not error else {'error': error}
    status_code = 200 if ingredient else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/month', methods=GET)
def get_month_with_most_revenue():
    month, error = ReportController.get_month_with_most_revenue()
    response = month if not error else {'error': error}
    status_code = 200 if month else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/top3', methods=GET)
def get_top3_customers():
    top3, error = ReportController.get_top3_customers()
    response = top3 if not error else {'error': error}
    status_code = 200 if top3 else 404 if not error else 400
    return jsonify(response), status_code
