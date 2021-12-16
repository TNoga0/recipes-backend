import typing
import strawberry

from gql.schema.ingredient import Ingredients, get_ingredient
from gql.schema.meal_type import MealTypes, get_meal_type
from gql.schema.recipe import Recipes, get_recipe

@strawberry.type
class Query:
    ingredient: Ingredients = strawberry.field(resolver=get_ingredient)
    mealtype: MealTypes = strawberry.field(resolver=get_meal_type)
    recipe: Recipes = strawberry.field(resolver=get_recipe)