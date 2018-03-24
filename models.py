from app import b
from sqlalchemy.dialects.postgresql import JSON

class Raingage(db.Model):
    __tablename__ = 'srer_raingages'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())
    name = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)