from orator.orm.model import Model
import strawberry
from dacite import from_dict

from sql_db.models.recipe import Recipe

@strawberry.type
class Recipes:
    id: int
    name: str
    url: str
    image_url: str

def get_recipe(id: strawberry.ID):
    return Recipe.find(id)
    