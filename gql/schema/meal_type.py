import strawberry
from dacite import from_dict

from sql_db.models.meal_type import MealType

@strawberry.type
class MealTypes:
    id: int
    name: str

def get_meal_type(id: strawberry.ID):
    return MealType.find(id)
    