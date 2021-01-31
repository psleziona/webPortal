from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
Bootstrap(app)
migrate = Migrate(app, db)


from app.apps.todo import todo
app.register_blueprint(todo.todo, url_prefix='/todo')


from app import routes
