from datetime import datetime
from app import db
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnwo())
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, title, content):
        if not title or len(title) > 100 or not content:
            raise ValueError("Invalid title or content")
        self.title = title
        self.content = content
