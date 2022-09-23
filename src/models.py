import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(50))
    email = Column(String(50), nullable=False)
    user_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    follower = relationship("Follower")
    favorites = relationship("Favorites")

    def follower(self):
        return None
    
    def update(self):
        return None


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    media = relationship("Media")
    favorites = relationship("Favorites")

    def update(self):
        return None


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    content = Column(String(250), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    favorites = relationship("Favorites")

    def update(self):
        return None


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    url = Column(String(250), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    favorites = relationship("Favorites")

    def update(self):
        return None


class Favorites(Base):
    __tablename__ = 'add_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def update(self):
        return None
    

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    id_from_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    id_to_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def update(self):
        return None

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')