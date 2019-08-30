    

from app import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from base import Base,engine

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin
from app import login




class User(UserMixin, db.Model):
    __tablename__ ='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(10),index=True , unique=True)
    email=Column(String(120),index=True , unique=True)
    password_hash=Column(String(20))
 
    def __repr__(self):
        return'<User {}>'.format(self.username)
    
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password_hash=set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


Base.metadata.create_all(engine)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))