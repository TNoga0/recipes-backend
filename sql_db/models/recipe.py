from orator import Model
from orator.orm.utils import belongs_to_many


class Recipe(Model):

    @belongs_to_many("recipe_meal_type_map")
    def meal_types(self):
        from sql_db.models.meal_type import MealType
        return MealType

    @belongs_to_many("recipe_ingredient_map")
    def ingredients(self):
        from sql_db.models.ingredient import Ingredient
        return Ingredient
