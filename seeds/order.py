from flask_seeder import Seeder, generator, Faker
from flask_seeder.generator import Generator
from app.repositories.models import Order
from faker import Faker as realFaker


fake = realFaker()


class fakerGenerator(Generator):
     """ Random Date generator 
     """

     def __init__(self, method, **kwargs):
          super().__init__(**kwargs)
          self._method = method

     def generate(self):
          return self._method()


# All seeders inherit from Seeder
class OrderSeeder(Seeder):

# run() will be called by Flask-Seeder
     def run(self):
          faker = Faker(
               cls=Order,
               init={
                    "client_name": fakerGenerator(fake.name),
                    "total_price": generator.Integer(start=0, end=30),
                    "size_id": generator.Integer(start=1, end=6),
                    "client_dni": generator.Integer(start=32132121, end=32132141),
                    "client_address": fakerGenerator(fake.address),
                    "client_phone": fakerGenerator(fake.phone_number),
                    "date": fakerGenerator(fake.date_time_this_year)
                    }
               )     
          for o in faker.create(100):
               print("Adding order: %s" % o)
               self.db.session.add(o)

