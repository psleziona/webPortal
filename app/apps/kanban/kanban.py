from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Task, TaskCategory, Project
from .forms import AddTask, AddProject
from app import db
from .tasks_handle import move_task, delete_task
from flask_login import current_user, login_required

kanban = Blueprint('kanban', __name__)

@kanban.route('/', methods=['POST', 'GET'])
@login_required
def index():
    if not request.args.get('project'):
        return redirect(url_for('kanban.index', project=Project.query.get(1).name))

    form = AddTask()

    if form.validate_on_submit():
        title = form.title.data
        action = form.task.data
        select_project = request.args.get('project')
        author = current_user
        task = Task(name=title, todo=action, project=Project.query.filter_by(name=select_project).first(), author=author)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('kanban.index', project=select_project))

    tables = TaskCategory.query.all()
    projects = current_user.project
    return render_template('kanban.html', form=form, tables=tables, projects=projects)


@kanban.route('/add_project', methods=['POST', 'GET'])
@login_required
def add_project():
    form = AddProject()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        project = Project(name=name, description=description)
        project.users.append(current_user)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('kanban.index', project=project.name))
    return render_template('add_project.html', form=form)


@kanban.route('/change', methods=['POST'])
def handle_task():
    task_id = int(request.form['task_id'])
    category_name = request.form['category']
    move_task(task_id, category_name)
    return 'Changed'


@kanban.route('/delete_task/<id>', methods=['POST'])
def task_delete(id):
    if delete_task(id):
        return True
