from orator.migrations import Migration


class CreateMealTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('meal_types') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('meal_types')
