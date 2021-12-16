from orator import DatabaseManager, Schema, Model
from pathlib import Path

# path = os.path.abspath(sql_db)
path = Path(__file__).parent.resolve()
# config = yaml.safe_load(open(f"{path}/sql_db/orator_config.yml"))

config = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "recipes",
        "user": "postgres",
        "password": "pass",
        "prefix": '',
        "port": "5432"
    }
}

db = DatabaseManager(config)
schema = Schema(db)

if __name__ == "__main__":
    class Ingredient(Model):
        pass

    # print(db.table('ingredients').get())
    # print(Ingredient.find(2).name)
