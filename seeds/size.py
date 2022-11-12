from flask_seeder import Seeder
from faker import Faker
from random import random

from app.controllers import SizeController
from app.test.utils.functions import sizes_provider


fake = Faker()
fake.add_provider(sizes_provider)


# All seeders inherit from Seeder
class SizeSeeder(Seeder):
# run() will be called by Flask-Seeder
     def run(self):
          for _ in range(6):
               s = {'name': fake.unique.size(), 'price': int(random()*500)/100}
               print("Adding size: %s" % s)
               SizeController.create(s)
