from orator.migrations import Migration


class CreateRecipesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('recipes') as table:
            table.increments('id')
            table.string('name')
            table.string('url')
            table.string('image_url')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('recipes')
