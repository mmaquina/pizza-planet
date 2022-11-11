import pytest

from ..utils.functions import fake

@pytest.fixture
def report_uri():
    return '/report/'