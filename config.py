import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'd'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'vpszdjecia.online'
    MAIL_PORT = 25
    MAIL_USERNAME = 'gocio@vpszdjecia.online'
    MAIL_PASSWORD = 'gocio12345'
    HOST = 'https://fierce-eyrie-00435.herokuapp.com'