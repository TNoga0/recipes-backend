from server.app import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


recipeIngredientJunctionTable = db.Table(
    "recipe_ingredient_map",
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id"), primary_key=True),
    db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredients.id"), primary_key=True)
)


recipeMealTypeJunctionTable = db.Table(
    "recipe_meal_type_map",
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id"), primary_key=True),
    db.Column("meal_type_id", db.Integer, db.ForeignKey("meal_types.id"), primary_key=True)
)


class MealTypes(db.Model):
    __tablename__ = "meal_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    recipes = db.relationship('Recipe', secondary=recipeMealTypeJunctionTable, lazy='subquery', backref=db.backref('meal_types', lazy=True))


class Recipes(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    url = db.Column(db.String(150), unique=True, nullable=False)
    image_url = db.Column(db.String(150), unique=True, nullable=False)
    ingredients = db.relationship('Ingredient', secondary=recipeIngredientJunctionTable, lazy='subquery', backref=db.backref('recipes', lazy=True))



