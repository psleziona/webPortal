from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
Bootstrap(app)
mail = Mail(app)

from app.apps.kanban.kanban import kanban
from app.apps.sudoku.app import sudoku
app.register_blueprint(kanban, url_prefix='/kanban')
app.register_blueprint(sudoku, url_prefix='/sudoku')

from app import routes