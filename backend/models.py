from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    resource_type = db.Column(db.String(50), nullable=False)  # e.g., video, document, etc.
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Resource {self.title}>'
