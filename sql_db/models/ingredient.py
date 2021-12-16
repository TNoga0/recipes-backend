from orator import Model
from orator.orm.utils import belongs_to_many

class Ingredient(Model):

    @belongs_to_many
    def recipes(self):
        from sql_db.models.recipe import Recipe
        return Recipe
