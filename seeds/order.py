from flask_seeder import Seeder 
from faker import Faker
from random import random, randint

from app.test.utils.functions import clients_provider
from app.controllers import OrderController


fake = Faker()
fake.add_provider(clients_provider)


# All seeders inherit from Seeder
class OrderSeeder(Seeder):
     # run() will be called by Flask-Seeder
     def run(self):
          for _ in range(120):
               order = dict(fake.client(), **{'date': fake.date_time_this_year(), 
                    'size_id': int(random()*5 + 1), 
                    'ingredients': list(set([randint(1,11) for _ in range(randint(0,11))])), 
                    'beverages': list(set([randint(1,6) for _ in range(randint(0,6))])) 
                    })
               print("Adding order from: %s" % order['client_name'])
               OrderController.create( order )


