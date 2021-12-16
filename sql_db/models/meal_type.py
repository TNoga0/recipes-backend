from orator import Model
from orator.orm import belongs_to_many

class MealType(Model):

    @belongs_to_many("recipe_meal_type_map")
    def recipes(self):
        from sql_db.models.recipe import Recipe
        return Recipe
