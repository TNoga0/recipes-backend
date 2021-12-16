from orator import Model
from orator.orm import has_many




class MealType(Model):

    @has_many
    def recipes(self):
        from sql_db.models.recipe import Recipe
        return Recipe
