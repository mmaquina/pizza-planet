from flask_seeder import Seeder, generator, Faker
from app.repositories.models import Size


# All seeders inherit from Seeder
class SizeSeeder(Seeder):

# run() will be called by Flask-Seeder
     def run(self):

          faker = Faker(
               cls=Size,
               init={
                    "name": generator.String("(Small|Medium|Big|Stone Small|Stone Medium|Stone Big)"),
                    #"name": generator.Name(),
                    "price": generator.Integer(start=0, end=5)
                    }
               )     
          for s in faker.create(6):
               print("Adding size: %s" % s)
               self.db.session.add(s)