from orator.migrations import Migration


class CreateRecipeIngredientMapsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('recipe_ingredient_maps') as table:
            table.increments('id')
            table.integer('ingredient_id').unsigned()
            table.foreign('ingredient_id').references('id').on('ingredients')
            table.integer('recipe_id').unsigned()
            table.foreign('recipe_id').references('id').on('recipes')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('recipe_ingredient_maps')
