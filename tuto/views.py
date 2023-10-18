from .app import app
from flask import render_template
from .models import *
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms.validators import DataRequired
from flask import url_for,redirect
from .app import db
from wtforms import PasswordField
from .models import User
from hashlib import sha256
from flask_login import login_user , current_user
from flask import request

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="My books !",
        books = get_sample())
    
@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    return render_template(
    "detail.html",
    book=book)

class AuthorForm ( FlaskForm ):
    id = HiddenField('id')
    name = StringField('Nom', validators =[DataRequired()])

@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template("edit-author.html",author =a, form=f)


@app.route("/save/author/", methods =("POST" ,))
def save_author ():
    a = None
    f = AuthorForm ()
    if f. validate_on_submit ():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db. session .commit ()
        return redirect (url_for('detail', id=a.id))
    a = get_author(int(f.id.data ))
    return render_template (
    "edit - author.html",
    author =a, form=f)

class LoginForm(FlaskForm):
    username=StringField('Username')
    password=PasswordField("Password")
    next=HiddenField()
    
    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m=sha256()
        m.update(self.password.data.encode())
        passwd= m.hexdigest()
        return user if passwd == user.password else None

@app.route("/login/", methods=("GET","POST",))
def login():
    f =LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next = f.next.data or url_for("home")
            return redirect(next)
    return render_template(
        "login.html",form=f
    )