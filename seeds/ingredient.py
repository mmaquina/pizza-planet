from flask_seeder import Seeder, generator, Faker

from app.repositories.models import Ingredient


# All seeders inherit from Seeder
class IngredientSeeder(Seeder):
     # run() will be called by Flask-Seeder
     def run(self):
          faker = Faker(
               cls=Ingredient,
               init={
                    "name": generator.String("(Garlic|Oregano|Mozzarella|" + \
                         "BlueCheese|Provolone|Onions|Tomato|Pineapple|" + \
                         "Ham|Pepperoni|Eggs|Bacon|Longaniza|Mushrooms|" + \
                         "Anchovys|Black Olives|Spinach|Chard|Eggplant|Palm Hearts)"),
                    "price": generator.Integer(start=0, end=5)
                    }
               )     
          for ingredient in faker.create(10):
               print("Adding beverage: %s" % ingredient)
               self.db.session.add(ingredient)

     def __str__(self):
          return "Name=%s" % (self.name)