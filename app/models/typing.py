from datetime import datetime
from app import db

class TypeTest(db.Model):
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Columns strictly matching your frontend payload
    words_typed = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Float, nullable=False)
    wpm = db.Column(db.Float, nullable=False)
    time_limit = db.Column(db.Float, nullable=True) # Changed to Float as elapsedTime is often a decimal
    notes = db.Column(db.String(255), nullable=True)

    # Standard Timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def serialize(self):
        return {
            'test_id': self.test_id,
            'words_typed': self.words_typed,
            'accuracy': self.accuracy,
            'wpm': self.wpm,
            'time_limit': self.time_limit,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }