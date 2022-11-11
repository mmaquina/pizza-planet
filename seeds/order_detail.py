from flask_seeder import Seeder, generator, Faker

from app.repositories.models import OrderDetail


# All seeders inherit from Seeder
class IngredientSeeder(Seeder):
     # run() will be called by Flask-Seeder
     def run(self):
          faker = Faker(
               cls=OrderDetail,
               init={
                    "order_id": generator.Integer(start=0, end=100),
                    "ingredient_price": generator.Integer(start=0, end=5),
                    "ingredient_id": generator.Integer(start=0, end=10)
                    }
               )     

          for od in faker.create(500):
               print("Adding Order Detail: %s" % od)
               self.db.session.add(od)
