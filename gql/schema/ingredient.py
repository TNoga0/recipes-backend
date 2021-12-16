from orator.orm.model import Model
import strawberry
from dacite import from_dict

from sql_db.models.ingredient import Ingredient

@strawberry.type
class Ingredients:
    id: int
    name: str

def get_ingredient(id: strawberry.ID):
    return Ingredient.find(id)
    