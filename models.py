"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

def connect_db(app):
  db.app = app
  db.init_app(app)

DEFAULT_URL = 'https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png'

#user1 = User(first_name='Jacob',last_name='Man',img_url='www.google.com')
class User (db.Model):
  __tablename__ = 'users'
  
  id = db.Column(
    db.Integer, 
    primary_key=True, 
    autoincrement=True)
  
  first_name = db.Column(
    db.String(25),
    nullable=False)
  
  last_name = db.Column(
    db.String(25),
    nullable=False)
  
  img_url = db.Column(
    db.String(200),
    nullable=False,
    default=DEFAULT_URL)