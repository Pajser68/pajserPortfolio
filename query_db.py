"""
Query script to view all projects in the PostgreSQL database
Run with: docker exec web python query_db.py
"""
from app import app
from database import db
from models.project import Project

def query_all_projects():
    with app.app_context():
        projects = Project.query.all()
        
        if not projects:
            print("No projects found in database.")
            return
        
        print(f"\n{'='*60}")
        print(f"Total Projects: {len(projects)}")
        print(f"{'='*60}\n")
        
        for project in projects:
            print(f"ID: {project.id}")
            print(f"Name: {project.name}")
            print(f"GitHub: {project.github_link}")
            print(f"Description: {project.description}")
            print(f"Technologies: {project.technologies}")
            print(f"{'-'*60}\n")

if __name__ == '__main__':
    query_all_projects()
