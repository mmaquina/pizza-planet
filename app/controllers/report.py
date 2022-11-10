from ..repositories.managers import ReportManager
from .base import BaseController
from sqlalchemy.exc import SQLAlchemyError

class ReportController():
    manager = ReportManager

    @classmethod
    def get_most_requested_ingredient(cls):
        try:
            return cls.manager.get_most_requested_ingredient(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_month_with_most_revenue(cls):
        try:
            return cls.manager.get_month_with_most_revenue(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    @classmethod
    def get_top3_customers(cls):
        try:
            return cls.manager.get_top3_customers(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
            