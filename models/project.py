# Database Models
from database import db


class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    github_link = db.Column(db.String(500))
    description = db.Column(db.Text)
    technologies = db.Column(db.String(500))
    
    def __repr__(self):
        return f'<Project {self.name}>'