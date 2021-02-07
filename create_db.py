from app import db
from app.models import Users, Project, PostCategory, TaskCategory


db.create_all()

admin = Users(username='pablo',email='gocio@vpszdjecia.online', superuser=True, is_active=True)
admin.set_password('a')

cat1 = PostCategory(name='main')
cat2 = PostCategory(name='personal')
cat3 = PostCategory(name='development')

proj1 = Project(name='Blog', description='Realizacja dalszych pomysłów co do owego bloga.')

proj2 = Project(name='Koło', description='Sieciowa gra w koło fortuny.')

taskcat = TaskCategory(name='todo')
taskcat1 = TaskCategory(name='in_progress')
taskcat2 = TaskCategory(name='finished')

db.session.add_all([admin, cat1, cat2, cat3, proj1, proj2, taskcat, taskcat1, taskcat2])
db.session.commit()