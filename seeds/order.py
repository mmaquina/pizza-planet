from flask_seeder import Seeder, generator, Faker
from flask_seeder.generator import Generator
from app.repositories.models import Order
from datetime import datetime


class Date(Generator):
    """ Random Date generator """

    def generate(self):
        """ Generate a random date
        """
        return datetime.utcnow() - datetime.timedelta( months = self.rnd.randint(0, 12) )


# All seeders inherit from Seeder
class OrderSeeder(Seeder):

# run() will be called by Flask-Seeder
     def run(self):

          faker = Faker(
               cls=Order,
               init={
                    "client_name": generator.Name() + generator.Name(),
                    "total_price": generator.Integer(start=0, end=30),
                    "size_id": generator.Integer(start=1, end=6),
                    "client_dni": generator.Integer(start=32132121, end=32132141),
                    "client_address": generator.Sequence(),
                    "client_phone": generator.Integer(start=4532132121, end=46000000),
                    "size": generator.Sequence(),
                    "date": Date.generate()
                    }
               )     
          for o in faker.create(200):
               print("Adding order: %s" % o)
               self.db.session.add(o)
               
          def __str__(self):
               return "Name=%s, Price=%d, Date=%s" % (self.client_name, self.total_price, self.date)