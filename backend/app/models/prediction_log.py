from app.database.db import db
from datetime import datetime

class PredictionLog(db.Model):
    __tablename__ = 'prediction_logs'
    id = db.Column(db.Integer, primary_key=True)
    request_data = db.Column(db.JSON)
    response_data = db.Column(db.JSON)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
