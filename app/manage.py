from flask.cli import FlaskGroup
from server.app import app, db

cli = FlaskGroup(app)


@cli.command("create_database")
def create_database():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("add_initial")
def add_initial():
    from models.models import Ingredient
    db.session.add(Ingredient(name="Apple"))
    db.session.commit()


if __name__ == "__main__":
    cli()
