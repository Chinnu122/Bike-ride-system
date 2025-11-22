from app.database.db import db
from datetime import datetime

class Ride(db.Model):
    __tablename__ = 'rides'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pickup = db.Column(db.String(100), nullable=False)
    drop = db.Column(db.String(100), nullable=False)
    ride_time = db.Column(db.DateTime, default=datetime.utcnow)
    predicted_price = db.Column(db.Float)
