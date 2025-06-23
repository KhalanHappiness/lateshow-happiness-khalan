from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from . import db

class Appearance(db.Model, SerializerMixin):
   
   __tablename__ = 'appearances'

   serialize_rules = ('-guest.appearances', '-episode.appearances')

   id = db.Column(db.Integer, primary_key = True)
   rating = db.Column(db.Integer)
   episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable =False)
   guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable =False)


   guest = db.relationship('Guest', back_populates = 'appearances')
   episode =db.relationship('Episode', back_populates = 'appearances')

   def __repr__ (self):
      return f'<Appearance {self.id}, {self.rating}>'







