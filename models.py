from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import func

class Raingage(db.Model):
    __tablename__ = 'srer_raingages'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())
    name = db.Column(db.String())
    latitude = db.Column(db.Numeric(15, 5, True))
    longitude = db.Column(db.Numeric(15, 5, True))
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return '<id: {}, code: {}, name: {}>'.format(self.id, self.code, self.name)