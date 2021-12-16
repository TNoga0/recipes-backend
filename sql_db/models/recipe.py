from orator import Model
from orator.orm.utils import belongs_to_many


class Recipe(Model):

    @belongs_to_many
    def meal_types(self):
        from sql_db.models.meal_type import MealType
        return MealType
