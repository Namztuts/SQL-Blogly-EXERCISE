"""Blogly application."""
from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = "SupaSecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.app_context().push()
connect_db(app)
db.create_all()


@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def show_users():
    '''Show list of all users in db'''
    users = User.query.order_by(User.first_name, User.last_name).all()
    return render_template('home.html', users=users)


@app.route('/users/new')
def new_user():
    '''Goes to a user creation form'''
    return render_template('new_user.html')

@app.route('/users/new', methods=['POST']) #on submit, the form does this
def add_user():
    '''Creates user based on user input'''
    first = request.form['first_name'].strip() #removing any leading or trailing spaces from user input
    last = request.form['last_name'].strip()
    url = request.form['img_url'].strip() or None
    
    if not first or not last:
        flash('First and last name are required!')
        return redirect('/users/new')
    
    new_user = User(first_name=first,last_name=last,img_url=url)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')


@app.route('/users/<int:user_id>')
def user_details(user_id):
    '''Shows details for a specific user'''
    user = User.query.get_or_404(user_id)
    return render_template('details.html',user=user)


@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST']) #when initially going to this URL (GET) grabbing data and auto filling the inputs
def user_update(user_id):
    '''Edits user based on user edits'''
    user = User.query.get_or_404(user_id)
    
    if request.method =='POST': #on submit of the form, this URL does this
        user.first_name= request.form['edit_first_name'].strip() #removing any leading or trailing spaces from user input
        user.last_name= request.form['edit_last_name'].strip()
        user.img_url= request.form['edit_img_url'].strip()
    
        db.session.commit()
        return redirect('/users')
    
    return render_template('edit_user.html', user=user) 


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    '''Deletes a specific user'''
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/users')



'''
table.query.filter_by(hunger=45).delete()       | 1. grabbing what we want to delete via the filter (or any other filter type)
db.session.commit()                             | 2. deleting that entry | no need to add() first

**DELETE**
DELETE FROM books WHERE page_count > 500; | deleting entries where page count is greater than 500
DELETE FROM books WHERE author ILIKE 'S%' OR author ILIKE 'T%'; | deleting entries if author starts with an 's' or 't'
'''