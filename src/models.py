import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Follower(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    photo = Column(String(250), nullable=False)
    text = Column(String(250))
    likes = Column(Integer)

class Liked(Base):
    __tablename__ = 'liked_posts'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)

class Comment(Base):
    __tablename__ = 'comments'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    text = Column(String(250))
    
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e