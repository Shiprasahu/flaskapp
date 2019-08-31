    

from app import db,login
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from base import Base,engine

##### login ####
from flask_login import UserMixin

##passwordhashing##
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ ='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(10),index=True , unique=True)
    email=Column(String(120),index=True , unique=True)
    password_hash=Column(String(20))
 
    def __repr__(self):
        return'<User {}>'.format(self.username)
    
    def __init__(self,username,email, password_hash):
        self.username=username
        self.email=email
        
    def set_password(self, password):
        self.password_hash= generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))
