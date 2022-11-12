from flask_seeder import Seeder
from faker import Faker
from random import random

from app.controllers import IngredientController
from app.test.utils.functions import ingredients_provider


fake = Faker()
fake.add_provider(ingredients_provider)


# All seeders inherit from Seeder
class IngredientSeeder(Seeder):
     # run() will be called by Flask-Seeder
     def run(self):
          for _ in range(10):
               ing = {'name': fake.unique.ingredient(), 'price': int(random()*500)/100}
               print("Adding ingredient: %s" % ing)
               IngredientController.create(ing)
