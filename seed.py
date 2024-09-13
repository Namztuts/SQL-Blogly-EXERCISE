"""Seed file to make sample data for users db."""
   #run this file in ipython3 | %run seed.py
from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it | deletes all
User.query.delete()

# Add users
johnB = User(first_name='John', last_name='Bush', img_url='https://static.wixstatic.com/media/4c37a2_e5a09e4a8a1749ad9812a980042220df~mv2.jpg/v1/fill/w_920,h_554,al_c,q_85/JohnBush.jpg')
jeffC = User(first_name='Jeff', last_name='Collins', img_url='https://variety.com/wp-content/uploads/2024/05/Jeff-Collins-Headshot_Credit-Holly-Lynch-e1715988143879.jpg?w=1000&h=667&crop=1')
amyP = User(first_name='Amy', last_name='Phillips', img_url='https://thecomicscomic.com/wp-content/uploads/2018/11/amyphillips.png')

# Add new objects to session, so they'll persist
db.session.add(johnB)
db.session.add(jeffC)
db.session.add(amyP)

# Commit--otherwise, this never gets saved!
db.session.commit()
