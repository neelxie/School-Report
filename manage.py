import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from run import app
from app.models import db


# app.config.from_object()

migrate = Migrate()
migrate.init_app(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
