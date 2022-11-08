import pytest
from faker import Faker
from faker.providers import DynamicProvider

from ..utils.functions import get_random_price


fake = Faker()

sizes_provider = DynamicProvider(
     provider_name="size",
     elements=["Judas", "Peter", "John", "Mark", "Matthew", "Luke" ],
)

fake.add_provider(sizes_provider)


def size_mock() -> dict:
    return {
        'name': fake.size(),
        'price': get_random_price(.5, 5)
    }


@pytest.fixture
def size_uri():
    return '/size/'


@pytest.fixture
def size():
    return size_mock()


@pytest.fixture
def sizes():
    return [size_mock() for _ in range(5)]


@pytest.fixture
def create_size(client, size_uri) -> dict:
    response = client.post(size_uri, json=size_mock())
    return response


@pytest.fixture
def create_sizes(client, size_uri) -> list:
    sizes = []
    for _ in range(10):
        new_size = client.post(size_uri, json=size_mock())
        sizes.append(new_size.json)
    return sizes
