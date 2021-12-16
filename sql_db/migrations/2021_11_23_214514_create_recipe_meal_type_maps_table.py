from orator.migrations import Migration


class CreateRecipeMealTypeMapTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('recipe_meal_type_map') as table:
            table.increments('id')
            table.integer('meal_type_id').unsigned()
            table.foreign('meal_type_id').references('id').on('meal_types')
            table.integer('recipe_id').unsigned()
            table.foreign('recipe_id').references('id').on('recipes')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('recipe_meal_type_maps')
