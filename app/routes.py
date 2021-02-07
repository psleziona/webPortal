from app import app, db, login
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from app.models import Users, Post, PostCategory, Comment
from app.forms import PostForm, RegisterForm, LoginForm, CommentForm
import jwt
from app.mails import send_auth_msg


@app.route('/', methods=['POST', 'GET'])
def index():
    print(request.form)
    form = PostForm()
    if form.validate_on_submit():
        cat = PostCategory.query.filter_by(name=form.category.data).first()
        post = Post(title=form.title.data, content=form.post.data,
                    author=current_user, cat=cat)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index', page=1, category=form.category.data))

    comment_form = CommentForm()

    if request.args.get('page') == None and request.args.get('category') == None:
        return redirect(url_for('index', page=1, category='main'))   
        
    page = request.args.get('page', type=int)
    category = request.args.get('category', type=str)
    cat = PostCategory.query.filter_by(name=category).first()
    posts = cat.posts.order_by(Post.time.desc()).paginate(page, 5, False)
    categories = PostCategory.query.all()
    return render_template('index.html', form=form, posts=posts, categories=categories, comment_form=comment_form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        auth_token = user.gen_auth_token()
        auth_link = app.config['HOST'] + url_for('auth', token=auth_token)
        send_auth_msg(auth_link, form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Register successfully')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data):
            login_user(user)
            flash('Success logged')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/features', methods=['GET', 'POST'])
@login_required
def features():
    posts = Post.query.all()
    users = Users.query.all()
    return render_template('features.html', posts=posts, users=users)



@app.route('/post_handler/<id>', methods=['POST'])
def post_handler(id):
    username = current_user.username if not current_user.is_anonymous else 'Anonymous'
    comment_content = request.form['comment']
    post = Post.query.get(id)
    comment = Comment(author=username, text=comment_content, pos=post)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/post_delete/<id>', methods=['POST'])
@login_required
def post_delete(id):
    if current_user.superuser:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return b'done'
    return redirect(url_for('index'))


@app.route('/auth/<token>')
def auth(token):
    try:
        data = jwt.decode(token, 'apka', 'HS256')
        user = data['username']
        user = Users.query.filter_by(username=user).first()
        user.confirm_user()
        db.session.commit()
        flash('Confirm success')
        return redirect(url_for('login'))
    except:
        return redirect(url_for('index'))

@app.route('/user/<user>')
def user_page(user):
    if current_user.username == user:
        return '<h1>Witaj na swojej stronie</h1>'
    return f'<h1>Jestes na stronie uzytkownika {user}</h1>'