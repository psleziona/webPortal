from app import login, db
from datetime import datetime, timedelta
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# App models

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    superuser = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    visible = db.Column(db.Boolean, default=True)
    category = db.Column(db.Integer, db.ForeignKey('post_category.id'))
    comments = db.relationship('Comment', backref='pos')

    def __repr__(self):
        return f'<Post {self.title}>'


class PostCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), default='Main', unique=True)
    posts = db.relationship('Post', backref='cat', lazy='dynamic')

    def __repr__(self):
        return f'<Category {self.name}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20), default='Anonymous')
    text = db.Column(db.Text)
    belong = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment {self.id}>'




#Todo models

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    todo = db.Column(db.String(200))
    add_time = db.Column(db.Date, default=datetime.utcnow)
    deadline = db.Column(db.Date)
    category = db.Column(db.Integer, db.ForeignKey('task_category.id'), default=1)
    workgroup = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return f'<Activity {self.name}>'

    def set_deadline(self, time):
        self.deadline = self.add_time.timedelta(days=int(time))


class TaskCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    tasks = db.relationship(
        'Task', backref='cat', lazy='dynamic')

    def __repr__(self):
        return f'<Category {self.name}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.Text)
    tasks = db.relationship('Task', backref='project', lazy='dynamic')

    def __repr__(self):
        return f'<Project {self.name}>'


@login.user_loader
def get_user(id):
    return User.query.get(id)
