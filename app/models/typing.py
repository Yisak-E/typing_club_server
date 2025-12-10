"""
- Test ID
- Passage/Prompt
- Time Limit (min)
- Words Typed
- Errors
- Accuracy (%)
- WPM (Words per Minute)
- Notes
"""
from datetime import datetime

from app import db


class TypeTest(db.Model):
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    prompt = db.Column(db.String(10000), nullable=False)
    time_limit = db.Column(db.Integer, nullable=False)
    words_typed = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Float, nullable=False)
    errors = db.Column(db.Float, nullable=False)
    wpm = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def serialize(self):
        return {
            'test_id': self.test_id,
            'prompt': self.prompt,
            'time_limit': self.time_limit,
            'words_typed': self.words_typed,
            'accuracy': self.accuracy,
            'errors': self.errors,
            'wpm': self.wpm,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at

        }
