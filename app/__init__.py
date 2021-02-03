from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
Bootstrap(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app.apps.kanban.kanban import kanban
app.register_blueprint(kanban, url_prefix='/kanban')


from app import routes