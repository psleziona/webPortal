from app.models import Task, TaskCategory
from app import db

def move_task(task_id, category_name):
    task = Task.query.get(task_id)
    category = TaskCategory.query.filter_by(name=category_name).first()
    task.cat=category
    db.session.commit()


def delete_task(task_id):
    task = Task.query.get(int(task_id))
    db.session.delete(task)
    db.session.commit()
    return True