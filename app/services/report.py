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
