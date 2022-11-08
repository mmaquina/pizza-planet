import pytest
from faker import Faker
from faker.providers import DynamicProvider

from ..utils.functions import get_random_price


fake = Faker()

beverages_provider = DynamicProvider(
     provider_name="beverage",
     elements=["Red Beer", "IPA Beer", "Golden Beer", "APA Beer", "Scotish Beer", "1.5L Water", "Cola", "Lemon Soda", "Orange Soda", "Stout Beer", "Bock Beer", "Wheat Beer"],
)

fake.add_provider(beverages_provider)

def beverage_mock() -> dict:
    return {
        'name': fake.beverage(),
        'price': get_random_price(0.5, 5)
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'


@pytest.fixture
def beverage():
    return beverage_mock()


@pytest.fixture
def beverages():
    return [beverage_mock() for _ in range(5)]


@pytest.fixture
def create_beverage(client, beverage_uri) -> dict:
    response = client.post(beverage_uri, json=beverage_mock())
    return response


@pytest.fixture
def create_beverages(client, beverage_uri) -> list:
    beverages = []
    for _ in range(10):
        new_beverage = client.post(beverage_uri, json=beverage_mock())
        beverages.append(new_beverage.json)
    return beverages
