from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Task, TaskCategory, Project
from .forms import AddTask
from app import db
from .tasks_handle import move_task, delete_task

todo = Blueprint('todo', __name__)

@todo.route('/', methods=['POST', 'GET'])
def index():
    
    if not request.args.get('project'):
        return redirect(url_for('todo.index', project=Project.query.get(1).name))
    form = AddTask()
    if form.validate_on_submit():
        title = form.title.data
        action = form.task.data
        select_project = request.args.get('project')
        task = Task(name=title, todo=action, project=Project.query.filter_by(name=select_project).first())
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('todo.index', project=select_project))
    tables = TaskCategory.query.all()
    projects = Project.query.all()
    return render_template('todo.html', form=form, tables=tables, projects=projects)


@todo.route('/change', methods=['POST'])
def handle_task():
    task_id = int(request.form['task_id'])
    category_name = request.form['category']
    move_task(task_id, category_name)
    return 'Changed'


@todo.route('/delete_task/<id>', methods=['POST'])
def task_delete(id):
    if delete_task(id):
        return True
