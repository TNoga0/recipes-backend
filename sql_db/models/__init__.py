from orator.orm.model import Model
from sql_db.db import db

Model.set_connection_resolver(db)
