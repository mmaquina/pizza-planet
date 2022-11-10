from flask_seeder import Seeder, generator, Faker
from app.repositories.models import Beverage


# All seeders inherit from Seeder
class BeverageSeeder(Seeder):

# run() will be called by Flask-Seeder
     def run(self):

          faker = Faker(
               cls=Beverage,
               init={
                    "name": generator.Name(),
                    "price": generator.Integer(start=0, end=5)
                    }
               )     
          # Create 5 beverages
          for beverage in faker.create(5):
               print("Adding beverage: %s" % beverage)
               self.db.session.add(beverage)