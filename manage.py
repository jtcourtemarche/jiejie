from app import db
from models import User
import sqlite3
import os

# Initializes Sqlite3 Database
def init_db():
    with sqlite3.connect('watch.db') as conn:
        conn.commit()

    db.create_all()
    u = User(username='test')
    u.setpass('test')
    db.session.add(u)
    db.session.commit()
    print 'Complete'

def destroy_db():
    os.remove('watch.db')
    print 'Complete'

def add_user(username, password):
    u = User(username=username)
    u.setpass(password)

    db.session.add(u)
    db.session.commit()

    print 'Added user: {}'.format(u)

def del_user(username='', user_id=None):
    if username:
        u = User.query.filter_by(username=username).first()
        db.session.delete(u)
        db.session.commit()
    elif user_id:
        u = User.query.get(user_id)
        db.session.delete(u)
        db.session.commit()
    else:
        print 'Invalid parameters'