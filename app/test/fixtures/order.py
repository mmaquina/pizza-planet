import pytest
from ..utils.functions import shuffle_list, fake


def client_data_mock() -> dict:
    return {
        'client_address': fake.address(),
        'client_dni': fake.ssn(),
        'client_name': fake.name(),
        'client_phone': fake.phone_number()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(create_ingredients, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    size_id = create_size.get('_id')
    return {
        **client_data_mock(),
        'ingredients': ingredients,
        'size_id': size_id
    }


@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_sizes) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    sizes = [size.get('_id') for size in create_sizes]
    new_order = client.post(order_uri, json={
        **client_data_mock(),
        'ingredients': shuffle_list(ingredients)[:5],
        'size_id': shuffle_list(sizes)[0]
    })
    return new_order


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_sizes) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    sizes = [size.get('_id') for size in create_sizes]
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'ingredients': shuffle_list(ingredients)[:5],
            'size_id': shuffle_list(sizes)[0]
        })
        orders.append(new_order)
    return orders
