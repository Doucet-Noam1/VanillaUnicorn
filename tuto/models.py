from .app import db

class Author (db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    name = db.Column (db.String (100))

    def __repr__(self):
        return "<Author (%d) %s>" % (self.id,self.name)
    
class Book(db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    img = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author",backref =db.backref("books",lazy = "dynamic"))

    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)
    
from flask_login import UserMixin
class User(db.Model , UserMixin ):
    username = db.Column(db.String (50) , primary_key =True)   
    password = db.Column(db.String (64))

    def get_id(self ):
        return self.username

def get_sample():
    return Book.query.all()

def get_author(id):
    return Author.query.get(id)

from .app import login_manager
@login_manager.user_loader
def load_user (username ):
    return User.query.get(username)