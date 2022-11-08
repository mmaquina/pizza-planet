import pytest
from faker import Faker
from faker.providers import DynamicProvider

from ..utils.functions import get_random_price


fake = Faker()

ingredients_provider = DynamicProvider(
     provider_name="ingredient",
     elements=["Garlic", "Oregano", "Mozzarella", "Blue Cheese", "Provolone", "Onions", "Tomato", "Pineapple", "Ham", "Pepperoni", "Eggs", "Bacon"],
)

fake.add_provider(ingredients_provider)


def ingredient_mock() -> dict:
    return {
        'name': fake.ingredient(),
        'price': get_random_price(0, 10)
    }


@pytest.fixture
def ingredient_uri():
    return '/ingredient/'


@pytest.fixture
def ingredient():
    return ingredient_mock()


@pytest.fixture
def ingredients():
    return [ingredient_mock() for _ in range(10)]


@pytest.fixture
def create_ingredient(client, ingredient_uri) -> dict:
    response = client.post(ingredient_uri, json=ingredient_mock())
    return response


@pytest.fixture
def create_ingredients(client, ingredient_uri) -> list:
    ingredients = []
    for _ in range(10):
        new_ingredient = client.post(ingredient_uri, json=ingredient_mock())
        ingredients.append(new_ingredient.json)
    return ingredients
