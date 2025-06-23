from sqlalchemy_serializer import SerializerMixin

from . import db

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    serialize_rules = ('-appearances.guest', )


    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance', back_populates = 'guest', cascade = 'all, delete-orphan')

    def __repr__(self):
        return f'<Guest {self.id}, {self.name}, {self.occupation}>'


