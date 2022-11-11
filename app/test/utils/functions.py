import random
import string
from typing import Any, Union
from faker import Faker
from faker.providers import DynamicProvider


def get_random_string() -> str:
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters[:10])


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def get_random_price(lower_bound: float, upper_bound: float) -> float:
    return round(random.uniform(lower_bound, upper_bound), 2)


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy


def get_random_email() -> str:
    return f"{get_random_string()}@{get_random_choice(['hotmail.com', 'gmail.com', 'test.com'])}"


def get_random_sequence(length: int = 10) -> str:
    digits = list(map(str, range(10)))
    sequence = [digits[random.randint(0, 9)] for _ in range(length)]
    return ''.join(sequence)


def get_random_phone() -> str:
    return get_random_sequence(10)


fake = Faker()

sizes_provider = DynamicProvider(
     provider_name="size",
     elements=["Small", "Medium", "Big", "Stone Medium", "Stone Big" ],
)
fake.add_provider(sizes_provider)

beverages_provider = DynamicProvider(
     provider_name="beverage",
     elements=["Red Beer", "IPA Beer", "Golden Beer", "APA Beer", "Scotish Beer", "1.5L Water", "Cola", "Lemon Soda", "Orange Soda", "Stout Beer", "Bock Beer", "Wheat Beer"],
)
fake.add_provider(beverages_provider)

ingredients_provider = DynamicProvider(
     provider_name="ingredient",
     elements=["Garlic", "Oregano", "Mozzarella", "Blue Cheese", "Provolone", "Onions", "Tomato", "Pineapple", "Ham", "Pepperoni", "Eggs", "Bacon"],
)
fake.add_provider(ingredients_provider)


clients_provider = DynamicProvider(provider_name="client",
    elements=[{ 'client_address': fake.address(), 
    'client_dni': fake.ssn(), 
    'client_name': fake.name(), 
    'client_phone': fake.phone_number() } for i in range(20)]
    )

fake.add_provider(clients_provider)
