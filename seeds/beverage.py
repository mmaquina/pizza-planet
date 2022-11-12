from flask_seeder import Seeder 
from random import random
from faker import Faker

from app.controllers import BeverageController
from app.test.utils.functions import beverages_provider


fake = Faker()
fake.add_provider(beverages_provider)

# All seeders inherit from Seeder
class BeverageSeeder(Seeder):
     # run() will be called by Flask-Seeder
     def run(self):
          # Create 5 beverages
          for _ in range(5):
               b = {'name': fake.unique.beverage(), 'price': int(random()*500)/100}
               print("Adding beverage: %s" % b)
               BeverageController.create( b )
