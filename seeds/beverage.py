from flask_seeder import Seeder 
from random import random
from faker import Faker

from app.controllers import BeverageController
from app.test.utils.functions import beverages_provider


fake = Faker()
fake.add_provider(beverages_provider)

# All seeders inherit from Seeder
class BeverageSeeder(Seeder):
     def __init__(self, db=None):
          super().__init__(db=db)
          self.priority = 1

     # run() will be called by Flask-Seeder
     def run(self):
          # Create 5 beverages
          for _ in range(5):
               beverage = {'name': fake.unique.beverage(), 'price': int(random()*500)/100}
               print("Adding beverage: %s" % beverage)
               
               BeverageController.create( beverage )
