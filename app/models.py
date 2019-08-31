    

from app import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from base import Base,engine

class User(db.Model):
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
        self.password_hash= hash(password_hash)
        
Base.metadata.create_all(engine)