from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from . import db

class Appearance(db.Model, SerializerMixin):
   
   __tablename__ = 'appearances'

   db.id = db.Column(db.Integer)
   db.rating = db.Column(db.Integer)
   db.episode_id = db.Column(db.Integer)
   db.guest_id = db.Column(db.Integer)


   guest = db.relationship('Guest', back_populates = 'appearances')
   episode =db.relationship('Episode', back_populates = 'appearances')

   def __repr__ (self):
      return f'<Appearance {self.id}, {self.rating}>'







